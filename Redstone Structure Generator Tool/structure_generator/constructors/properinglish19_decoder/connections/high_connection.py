from structure_generator.constructors.properinglish19_decoder.connection import Connection
from structure_generator.constructors.properinglish19_decoder.build_handlers.single_on import SingleOn

class HighConnection(Connection):	
	def __init__(self, x, z):
		self.x = x
		self.z = z
		self.build_handler = SingleOn()
	
	def type(self):
		return "high connection with {}".format(self.build_handler.type())