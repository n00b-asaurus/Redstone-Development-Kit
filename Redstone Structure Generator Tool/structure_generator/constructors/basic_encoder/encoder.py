from structure_generator.constructor import Constructor
from structure_generator.datatypes.position import Position
from structure_generator.minecraft import fill, clone, setblock, base_block, redstone_dust, redstone_torch, repeater

import logging
log = logging.getLogger()

class Encoder(Constructor):
	def __init__(self, file, inputs_from):
		with open(file) as f:
			self.table = f.readlines()
		self.inputs_side = inputs_from
		
		self.width = len(self.table[0].strip())*2-1
		self.height = 4
		self.length = len(self.table)*2-1
		
	def generate_commands(self):
		expected_width = len(self.table[0].strip())
		for row in self.table:
			if len(row.strip()) != expected_width:
				raise Exception("Uneven row lengths")
		commands = []
		commands += self.__build_outputs()
		commands += self.__build_inputs()
		commands += self.__place_torches()
		return commands
	
	@staticmethod
	def register():
		return "basic_encoder"
		
	def __build_outputs(self):
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
		if self.inputs_side == 'left':
			for command in commands:
				command.translate(0,0,1)
		return commands
		
	def __build_inputs(self):
		commands = []
		for x in range(self.length+1):
			if x%2==0:
				continue
			elif x == 1:
				commands.append(fill(Position(x,2,0), Position(x,2,self.width), base_block()))
				commands.append(fill(Position(x,3,0), Position(x,3,self.width), redstone_dust()))
				if self.inputs_side == 'left':
					for z in range(0, self.width, 16):
						commands.append(setblock(Position(x,3,z), repeater(facing = '+z')))
				if self.inputs_side == 'right':
					for z in range(self.width, 0, -16):
						commands.append(setblock(Position(x,3,z), repeater(facing = '-z')))
			else:
				commands.append(clone(Position(1,2,0), Position(1,3,self.width), Position(x,2,0)))
		return commands
		
	def __place_torches(self):
		commands = []
		for x in range(self.length):
			if x%2 == 1:
					continue
			for z in range(self.width):
				if z%2 == 1:
					continue
				if self.table[int(x/2)][int(z/2)] == '1':
					commands.append(setblock(Position(x,2,z), redstone_torch(facing = '-x')))
		if self.inputs_side == 'left':
			for command in commands:
				command.translate(0,0,1)
		return commands