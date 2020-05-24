from structure_generator.block import Block

class Air(Block):
	def __init__(self):
		self.block_name = "minecraft:air"
		
	def __repr__(self):
		return "{}".format(self.block_name)