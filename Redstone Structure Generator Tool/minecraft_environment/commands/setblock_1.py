from minecraft_environment.command import Command

class SetBlock(Command):
	def __init__(self, pos, block):
		self.pos = pos
		self.block = block
		
	def get_string(self):
		return "setblock {} {}".format(self.pos, self.block)
		
	def translate(self, x, y, z):
		self.pos.translate(x,y,z)
		
	def rotate(self, amount):
		self.pos.rotate(amount)
		self.block.rotate(amount)