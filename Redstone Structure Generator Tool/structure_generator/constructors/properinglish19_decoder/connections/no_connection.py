from structure_generator.constructors.properinglish19_decoder.connection import Connection
from structure_generator.constructors.properinglish19_decoder.build_handlers.single_nc import SingleNC

class NoConnection(Connection):	
	def __init__(self, x, z):
		self.x = x
		self.z = z
		self.build_handler = SingleNC()
		
	def type(self):
		return "no connection with {}".format(self.build_handler.type())