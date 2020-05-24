from structure_generator.block import Block

class RedstoneTorch(Block):
	def __init__(self, facing):
		facing_dict = {'+x':2,'+z':3,'-x':0,'-z':1}
		self.block_name = "minecraft:redstone_wall_torch"
		self.block_nbt_pointer = facing_dict[facing]
		self.block_nbt = ["facing=west","facing=north","facing=east","facing=south"]
		
	def rotate(self, amount):
		self.block_nbt_pointer += amount
		self.block_nbt_pointer %= 4
		
	def __repr__(self):
		return "{}[{}]".format(self.block_name,self.block_nbt[self.block_nbt_pointer])