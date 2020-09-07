class Connection:
	def __init__(self, x, z):
		self.x = x
		self.z = z
		self.build_handler = None
	
	def type(self):
		return "abstract connection"	
	
	def solve(self, right, downline, right_line):
		pass
		
	def build_structure(self, commands):
		self.build_handler.build_structure(commands, self.x, self.z)
			
	def place_input_repeater(self, commands):
		self.build_handler.place_input_repeater(commands, self.x, self.z)
		
	def place_output_repeater(self, commands, direction, left, left_downline):
		self.build_handler.place_output_repeater(commands, self.x, self.z, direction, left, left_downline)