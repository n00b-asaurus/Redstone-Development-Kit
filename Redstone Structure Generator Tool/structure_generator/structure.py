'''
Structures should be built from a single point out towards the +x, +y, and +z directions.
Assume the structure is facing the +x direction
Translations and rotations are handled outside of the structure.
'''

class Structure:
	def __init__(self):
		self.commands = []
	
	def generate_build(self, *arguments):
		raise NotImplementedError("generate_build method must be overwritten by a child class")
	
	def register_arguments(self):
		raise NotImplementedError("register_arguments method must be overwritten by a child class")
		
	def _add_command(self, command):
		self.commands.append(command)
	
	def get_build_commands(self):
		string_commands = []
		for command in self.commands:
			string_commands.append(command.get_string())
		return string_commands
	
	def _rotate(self, amount):
		for command in self.commands:
			command.rotate(amount)
		
	def _translate(self, x, y, z):
		for command in self.commands:
			command.translate(x, y, z)
