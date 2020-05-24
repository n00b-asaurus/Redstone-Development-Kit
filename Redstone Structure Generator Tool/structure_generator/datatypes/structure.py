from structure_generator.io_channel import IOChannel
console = IOChannel()

'''
Structures should be built from a single point out towards the +x, +y, and +z directions.
Assume the structure is facing the +x direction
Translations and rotations are handled outside of the structure.
'''

class Structure:
	def __init__(self, constructor):
		self.commands = constructor.generate_commands()
		self.size = (constructor.length, constructor.height, constructor.width) 
		
	def rotate(self, amount):
		for command in self.commands:
			command.rotate(amount)
		
	def translate(self, x, y, z):
		for command in self.commands:
			command.translate(x, y, z)
	
	def build(self, command_handler):
		for count, command in enumerate(self.commands):
			console.print("Executing commands {} of {}".format(count+1, len(self.commands)))
			command_handler.handle(command.get_string())
		command_handler.close()
			
	def size(self):
		return self.size
		
	