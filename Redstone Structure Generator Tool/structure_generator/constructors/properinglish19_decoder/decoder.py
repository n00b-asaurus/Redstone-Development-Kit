from structure_generator.constructor import Constructor
from structure_generator.datatypes.position import Position
from structure_generator.minecraft import fill, clone, setblock, base_block, redstone_dust, redstone_torch, repeater, air
from structure_generator.constructors.properinglish19_decoder.connections.high_connection import HighConnection
from structure_generator.constructors.properinglish19_decoder.connections.low_connection import LowConnection
from structure_generator.constructors.properinglish19_decoder.connections.no_connection import NoConnection
import logging
log = logging.getLogger()

class Decoder(Constructor):
	def __init__(self, file, outputs_to):
		with open(file) as f:
			table = f.readlines()
			log.debug(table)
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
			
			self.commands = []
			
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
				if outputs_to == 'right':
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
		
	def generate_commands(self):
		return self.commands
		
	@staticmethod
	def register():
		return "properinglish19_decoder"