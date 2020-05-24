from structure_generator.block import Block

class BaseBlock(Block):
	def __init__(self):
		self.block_name = "minecraft:iron_block"
		
	def __repr__(self):
		return "{}".format(self.block_name)