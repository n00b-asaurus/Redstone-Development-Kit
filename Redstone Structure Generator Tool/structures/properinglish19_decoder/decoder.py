from structure_generator.structure import Structure
from structure_generator.argument import Argument
from minecraft_environment.position import Position
from minecraft_environment.minecraft import fill, clone, setblock, base_block, redstone_dust, redstone_torch, repeater
from structures.properinglish19_decoder.connections.high_connection import HighConnection
from structures.properinglish19_decoder.connections.low_connection import LowConnection
from structures.properinglish19_decoder.connections.no_connection import NoConnection


class Decoder(Structure):
	def register_arguments(self):
		return [
			Argument("FILE", "Where's the source file?"),
			Argument("FACING", "What direction are you facing?", ['north','south','east','west']),
			Argument("OUTPUT_SIDE", "What side do the outputs build towards?", ['left', 'right']),
			Argument("BUILD_TO", "What direction is the structure being built towards?", ['left', 'right']),
			Argument("OFFSET", "Where is the structure being moved to?"),
		]
	
	def generate_build(self, file, facing, output_side, build_to, offset):
		with open(file.replace('"','')) as f:
			table = f.readlines()
			expected_width = len(table[0].strip())
			add_dummy_row = expected_width % 2 == 1
			for row in table:
				if len(row.strip()) != expected_width:
					raise Exception("Uneven row lengths")
				if add_dummy_row:
					row = "x" + row
					
			self.number_of_inputs = len(table[0].strip())
			self.number_of_outputs = len(table)
			self.width = self.number_of_inputs * 2
			self.height = 5
			self.length = self.number_of_outputs * 2
			self.facing = {'east':0,'west':2,'south':1,'north':3}[facing]
			self.output_side = output_side
			self.build_to = build_to
			self.offset = int(offset.split(',')[0]),int(offset.split(',')[1]),int(offset.split(',')[2])
			
			connections = [[None for j in range(self.number_of_inputs)] for i in range(self.number_of_outputs)]
			for x, row in enumerate(connections):
				for z, connection in enumerate(row):
					if table[x][z] == '1':
						connections[x][z] = HighConnection(x*2,z*2)
					elif table[x][z] == '0':
						connections[x][z] = LowConnection(x*2,z*2)
					elif table[x][z] in ['x','X','-']:
						connections[x][z] = NoConnection(x*2,z*2)
			for x, row in enumerate(connections):
				for z, connection in reversed(list(enumerate(row))):
					downline = None
					right_line = None
					right = z%2==1
					try: downline = connections[x+1][z]
					except Exception: pass
					try: right_line = connections[x][z+1]
					except Exception: pass
					connection.solve(right, downline, right_line)	
			for row in connections:
				for connection in row:
					connection.build_structure(self.commands)
			for x in range(0, self.number_of_outputs, 8):
				for z in range(0, self.number_of_inputs, 1):
					connections[x][z].place_input_repeater(self.commands)	
			for x in range(0, self.number_of_outputs, 1):
				left = None
				left_downline = None
				if self.output_side == 'right':
					for z in range(self.number_of_inputs-7, -1, -7):
						try: left = connections[x][z-1]
						except Exception: pass
						try: left_downline = connections[x+1][z-1]
						except Exception: pass
						connections[x][z].place_output_repeater(self.commands, '+z', left, left_downline)
				else:
					for z in range(7, self.number_of_inputs, 7):
						connections[x][z].place_output_repeater(self.commands, '-z', left, left_downline)
						try: left = connections[x][z-1]
						except Exception: pass
						try: left_downline = connections[x+1][z-1]
						except Exception: pass
		if self.build_to == 'left': self._translate(0,0,-self.width)
		self._rotate(self.facing)
		self._translate(*self.offset)