from minecraft_environment.block import Block

class RedstoneDust(Block):
	def __init__(self):
		self.block_name = "minecraft:redstone_wire"
		
	def __repr__(self):
		return "{}".format(self.block_name)