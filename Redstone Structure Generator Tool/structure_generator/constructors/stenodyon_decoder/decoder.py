from toolbox.class_collector.class_collector import collect_child_classes
from structure_generator.constructor import Constructor
from structure_generator.datatypes.position import Position
from structure_generator.minecraft import fill, clone, setblock, base_block, redstone_dust, redstone_torch, repeater, air
import logging
log = logging.getLogger()

class Decoder(Constructor):
	def __init__(self, file, outputs_to):
		with open(file) as f:
			table = f.readlines()
			log.debug(table)
			self.width = len(table[0].strip())*2-1
			self.height = 7
			self.length = len(table)*2-1
		self.right = outputs_to == 'right'
		self.modules = self._parse_modules(table)
		self._solve_modueles()
		self.moduleLocationX = [0] * 8
		self.moduleLocationY = [0] * 8
		self.commands = []
		self._build_outputs()
		self._build_modules()
		self._place_repeaters()
		
	def generate_commands(self):
		return self.commands
		
	@staticmethod
	def register():
		return "stenodyon_decoder"
	
	def _parse_modules(self, table):  
		modules = [[0 for j in range(len(table[0].strip()))] for i in range(len(table))]
		log.debug(modules)
		expected_width = len(table[0].strip())
		for x, row in enumerate(table):
			if len(row.strip()) != expected_width:
				raise Exception("Uneven row lengths")
			for z, bit in enumerate(row.strip()):
				if bit == '0': modules[x][-z-1] = 2
				elif bit == '1': modules[x][-z-1] = 1
				elif bit in ['x','X','-']: modules[x][-z-1] = 0
				else: raise Exception("Unrecognized character {}".format(bit))
		log.debug(modules)
		return modules
		
	def _solve_modueles(self):
		for x in range(len(self.modules)-2, 0, -1):
			for z in range(len(self.modules[x])-1):
				if self.modules[x][z] == 2 and self.modules[x-1][z] == 2:
					self.modules[x-1][z] = 0;
					self.modules[x][z] = 3;
		
		for x in range(len(self.modules)-2, 0, -1):
			for z in range(len(self.modules[x])-1):
				if self.modules[x][z] == 3 and self.modules[x][z+1] == 3:
					self.modules[x][z] = 6
					self.modules[x][z+1] = 7
					self.modules[x-1][z] = 4
					self.modules[x-1][z+1] = 5
		log.debug(self.modules)
					
	def _build_output_lane(self, Y):	
		length = len(self.modules[0]) * 2;
		self.commands.append(fill(Position(length + 2, -4, Y + 1), Position(2, -4, Y + 1), base_block()))
		self.commands.append(fill(Position(length + 2, -3, Y + 1), Position(2, -3, Y + 1), redstone_dust()))
		torchX = length + 3
		if self.right: torchX = 1
		torchDir = '+x'
		if self.right: torchDir = '-x'
		#self.commands.append(setblock(Position(torchX, -4, Y + 1), redstone_torch(torchDir)))
		
	def _copy_output_lanes(self, count, Y):
		length = len(self.modules[0]) * 2;
		depth = count * 2 - 1;
		self.commands.append(clone(
			Position(1, -3, 2),
			Position(length + 3, -4, 2 + depth),
			Position(1, -4, Y)))
	
	def _build_outputs(self):
		self._build_output_lane(2)
		availableLanes = 1;
		leftToBuild = len(self.modules) - 1;
		y = 1;
		while leftToBuild > 0:
			toCopy = min(availableLanes, leftToBuild);
			self._copy_output_lanes(toCopy, y * 2 + 2);
			availableLanes += toCopy;
			leftToBuild -= toCopy;
			y += toCopy;
	
	def _copy_module(self, xsrc, ysrc, xdest, ydest):
		Xsrc = xsrc * 2
		Ysrc = ysrc * 2
		Xdest = xdest * 2
		Ydest = ydest * 2
		self.commands.append(clone(
				Position(Xsrc, -4, Ysrc),
				Position(Xsrc + 1, 1, Ysrc + 1),
				Position(Xdest, -4, Ydest)))

	def _copy_module_line(self, xsrc, ysrc, count, xdest, ydest):
		Xsrc = xsrc * 2
		Ysrc = ysrc * 2
		Xdest = xdest * 2
		Ydest = ydest * 2
		self.commands.append(clone(
				Position(Xsrc, -4, Ysrc),
				Position(Xsrc + 2 * count + 1, 1, Ysrc + 1),
				Position(Xdest, -4, Ydest)))
	
	def _build_modules(self):
		self.moduleLocationX = [0] * 8
		self.moduleLocationY = [0] * 8
		for y  in range(len(self.modules)):
			for x in range(len(self.modules[y])):
				besty = 0;
				bestcount = 0;
				for py in range(y-1, -1, -1): # for every module below this one
					if self.modules[y][x] == self.modules[py][x]: # if the module below matches
						px = x;
						while px < len(self.modules[y]) and self.modules[y][px] == self.modules[py][px]: px += 1 # find the first pair of self.modules to the right that doesn't match
						count = px - x - 1; #get the difference between the two
						if count > bestcount:
							bestcount = count
							besty = py #take the greatest count and lock in that line 
					 	# in other words, this algorithm finds the longest pair of matching lines
						# this of course happens every iteration
				if bestcount > 1: #clone the line to save on some commands
					self._copy_module_line(x + 1, besty + 1, bestcount,
							x + 1, y + 1);
					x += bestcount
					if x >= len(self.modules[y]): # skip the line if it was successfully able to copy it in it's entirty
						break
				
				module = self.modules[y][x];
				builder_function = [self._build_module_0,self._build_module_1,self._build_module_2,self._build_module_3,self._build_module_4,self._build_module_5,self._build_module_6,self._build_module_7]
				if self.moduleLocationX[module] == 0 and self.moduleLocationY[module] == 0: 
					builder_function[module](x + 1, y + 1)
					self.moduleLocationX[module] = x + 1
					self.moduleLocationY[module] = y + 1
				else: 
					self._copy_module(self.moduleLocationX[module], self.moduleLocationY[module], x + 1, y + 1) #these copy the module if it was built before
					if module == 3:
						self.commands.append(setblock(Position(x * 2 + 4, -3, y * 2 + 2), base_block()))
		self._build_inputs()
		
	def _build_module_0(self, x, y):
		X = x * 2
		Y = y * 2
		self.commands.append(fill(Position(X, -2, Y), Position(X, -2, Y + 1), base_block()))
		self.commands.append(fill(Position(X, -1, Y), Position(X, -1, Y + 1), redstone_dust()))
	
	def _build_module_1(self, x, y):
		self.commands.append(fill(Position(x * 2, -2, y * 2), Position(x * 2, -2, y * 2 + 1), base_block()))
		self.commands.append(fill(Position(x * 2, -1, y * 2), Position(x * 2, -1, y * 2 + 1), redstone_dust()))
		self.commands.append(setblock(Position(x * 2 + 1, -2, y * 2 + 1), redstone_torch('+x')))
	
	def _build_module_2(self, x, y):
		self.commands.append(setblock(Position(x * 2, -2, y * 2 + 1), base_block()))
		self.commands.append(setblock(Position(x * 2, -3, y * 2), base_block()))
		self.commands.append(setblock(Position(x * 2, -2, y * 2), repeater('+z')))
		self.commands.append(fill(Position(x * 2, -1, y * 2), Position(x * 2, -1, y * 2 + 1), base_block()))
		self.commands.append(fill(Position(x * 2, 0, y * 2), Position(x * 2, 0, y * 2 + 1), redstone_dust()))
		
	def _build_module_3(self, x, y):
		X = x * 2
		Y = y * 2
		self.commands.append(setblock(Position(X, -2, Y + 1), base_block()))
		self.commands.append(setblock(Position(X, -3, Y), base_block()))
		self.commands.append(setblock(Position(X, -1, Y + 1), redstone_dust()))
		self.commands.append(setblock(Position(X, -2, Y), redstone_dust()))
		self.commands.append(setblock(Position(X + 1, -4, Y), base_block()))
		self.commands.append(setblock(Position(X + 1, -3, Y), repeater('+x')))
		self.commands.append(setblock(Position(X + 2, -3, Y), base_block()))
	
	def _build_module_4(self, x, y): 
		X = x * 2
		Y = y * 2
		self.commands.append(setblock(Position(X, -1, Y), base_block()))
		self.commands.append(setblock(Position(X, 0, Y), redstone_dust()))

		self.commands.append(fill(Position(X + 1, -2, Y + 1), Position(X, -2, Y + 1), base_block()))
		self.commands.append(fill(Position(X + 1, -1, Y + 1), Position(X, -1, Y + 1), redstone_dust()))

		self.commands.append(setblock(Position(X, 0, Y + 1), base_block()))
		self.commands.append(setblock(Position(X, 1, Y + 1), redstone_dust()))
	
	def _build_module_5(self, x, y):
		X = x * 2
		Y = y * 2
		self.commands.append(setblock(Position(X, -1, Y), base_block()))
		self.commands.append(setblock(Position(X, 0, Y), redstone_dust()))

		self.commands.append(setblock(Position(X, -2, Y + 1), base_block()))
		self.commands.append(setblock(Position(X, -1, Y + 1), redstone_dust()))

		self.commands.append(setblock(Position(X, 0, Y + 1), base_block()))
		self.commands.append(setblock(Position(X, 1, Y + 1), redstone_dust()))
	
	def _build_module_6(self, x, y):
		X = x * 2
		Y = y * 2
		self.commands.append(fill(Position(X, -3, Y), Position(X, -1, Y), base_block()))
		self.commands.append(setblock(Position(X, -2, Y), repeater('-z')))
		self.commands.append(setblock(Position(X, 0, Y), redstone_dust()))

		self.commands.append(setblock(Position(X, -2, Y + 1), base_block()))
		self.commands.append(setblock(Position(X, -1, Y + 1), redstone_dust()))
		self.commands.append(setblock(Position(X + 1, -3, Y), base_block()))
		self.commands.append(setblock(Position(X + 1, -2, Y), redstone_dust()))
		
	def _build_module_7(self, x, y):
		X = x * 2
		Y = y * 2
		self.commands.append(fill(Position(X, -3, Y), Position(X, -1, Y), base_block()))
		self.commands.append(setblock(Position(X, -2, Y), repeater('-z')))
		self.commands.append(setblock(Position(X, 0, Y), redstone_dust()))

		self.commands.append(setblock(Position(X, -2, Y + 1), base_block()))
		self.commands.append(setblock(Position(X, -1, Y + 1), redstone_dust()))
	
		
	def _build_inputs(self):
		self.commands.append(fill(Position(2, -2, 0), Position(2, -2, 1), base_block()))
		self.commands.append(setblock(Position(2, -1, 0), repeater('+z')))
		self.commands.append(setblock(Position(2, -1, 1), redstone_dust()))
		availableLanes = 1
		leftToBuild = len(self.modules[0]) - 1
		x = 1
		while leftToBuild > 0:
			toCopy = min(availableLanes, leftToBuild)
			depth = toCopy * 2 - 1
			self.commands.append(clone(Position(2, -2, 0), Position(2 + depth, -1, 1), Position(x * 2 + 2, -2, 0)))
			availableLanes += toCopy
			leftToBuild -= toCopy
			x += toCopy
		
	def _place_repeaters(self):
		# Input Lanes
		for x in range(len(self.modules[0])):
			X = x * 2 + 2
			for y in range(7,len(self.modules),7):
				module = self.modules[y][x]
				if module == 4 or module == 5: y -= 1
				module = self.modules[y][x]
				Y = y * 2 + 2
				if module == 0 or module == 1:
					self.commands.append(setblock(Position(X, -1, Y), repeater('+z')))
				elif module == 2:
					self.commands.append(fill(Position(X, 0, Y), Position(X, -1, Y + 1), air()))
					self.commands.append(setblock(Position(X, -1, Y + 1), redstone_dust()))
				elif module == 3:
					self.commands.append(setblock(Position(X, -1, Y - 1), repeater('+z')))
					self.commands.append(setblock(Position(X, -1, Y), base_block()))
				elif module == 6 or module == 7:
					self.commands.append(setblock(Position(X, 0, Y), repeater('+z')))
					self.commands.append(setblock(Position(X, 0, Y + 1), base_block()))
		# Output Lanes
		repeaterDir = '+x'
		if self.right: repeaterDir = '-x'
		for x in range(7, len(self.modules[0]), 7):
			X = x * 2 + 2
			for y in range(len(self.modules)):
				Y = y * 2 + 2
				module = self.modules[y][x]
				if module == 1 or module == 6:
					self.commands.append(setblock(Position(X, -3, Y + 1), repeater(repeaterDir)))
				else:
					self.commands.append(setblock(Position(X + 1, -3, Y + 1), repeater(repeaterDir)))