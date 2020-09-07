from structure_generator.structure import Structure
from structure_generator.argument import Argument
from minecraft_environment.position import Position
from minecraft_environment.minecraft import fill, clone, setblock, base_block, redstone_dust, redstone_torch, repeater


class Encoder(Structure):
	def _init_(self):
		pass
		
	def generate_build(self, file, facing, input_side, build_to, offset):
		with open(file.replace('"','')) as f:
			self.table = f.readlines()
		self.width = len(self.table[0].strip())*2-1
		self.height = 4
		self.length = len(self.table)*2-1
		self.facing = {'east':0,'west':2,'south':1,'north':3}[facing]
		self.input_side = input_side
		self.build_to = build_to
		self.offset = int(offset.split(',')[0]),int(offset.split(',')[1]),int(offset.split(',')[2])
		expected_width = len(self.table[0].strip())
		for row in self.table:
			if len(row.strip()) != expected_width:
				raise Exception("Uneven row lengths")
		self.commands += self._build_outputs()
		self.commands += self._build_inputs()
		self.commands += self._place_torches()
		if self.build_to == 'left': self._translate(0,0,-self.width)
		self._rotate(self.facing)
		self._translate(*self.offset)
	
	def register_arguments(self):
		return [
			Argument("FILE", "Where's the source file?"),
			Argument("FACING", "What direction are you facing?", ['north','south','east','west']),
			Argument("INPUT_SIDE", "What side do the inputs build towards?", ['left', 'right']),
			Argument("BUILD_TO", "What direction is the structure being built towards?", ['left', 'right']),
			Argument("OFFSET", "Where is the structure being moved to?"),
		]
	
		
	def _build_outputs(self):
		commands = []
		for z in range(self.width):
			if z%2==1:
				continue
			elif z == 0:
				commands.append(fill(Position(0,0,z), Position(self.length,0,z), base_block()))
				commands.append(fill(Position(0,1,z), Position(self.length,1,z), redstone_dust()))
				for x in range(15, self.length, 16):
					commands.append(setblock(Position(x,1,0), repeater(facing = '-x')))
			else:
				commands.append(clone(Position(0,0,0), Position(self.length,1,0), Position(0,0,z)))
		if self.input_side == 'left':
			for command in commands:
				command.translate(0,0,1)
		return commands
		
	def _build_inputs(self):
		commands = []
		for x in range(self.length+1):
			if x%2==0:
				continue
			elif x == 1:
				commands.append(fill(Position(x,2,0), Position(x,2,self.width), base_block()))
				commands.append(fill(Position(x,3,0), Position(x,3,self.width), redstone_dust()))
				if self.input_side == 'left':
					for z in range(0, self.width, 16):
						commands.append(setblock(Position(x,3,z), repeater(facing = '+z')))
				if self.input_side == 'right':
					for z in range(self.width, 0, -16):
						commands.append(setblock(Position(x,3,z), repeater(facing = '-z')))
			else:
				commands.append(clone(Position(1,2,0), Position(1,3,self.width), Position(x,2,0)))
		return commands
		
	def _place_torches(self):
		commands = []
		for x in range(self.length):
			if x%2 == 1:
					continue
			for z in range(self.width):
				if z%2 == 1:
					continue
				if self.table[int(x/2)][int(z/2)] == '1':
					commands.append(setblock(Position(x,2,z), redstone_torch(facing = '-x')))
		if self.input_side == 'left':
			for command in commands:
				command.translate(0,0,1)
		return commands