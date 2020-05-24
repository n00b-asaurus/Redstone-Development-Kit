from structure_generator.version import Version
from structure_generator.blocks.base_block_1 import BaseBlock
from structure_generator.blocks.redstone_dust_1 import RedstoneDust
from structure_generator.blocks.redstone_torch_1 import RedstoneTorch
from structure_generator.blocks.repeater_1 import Repeater
from structure_generator.blocks.air_1 import Air
from structure_generator.commands.clone_1 import Clone
from structure_generator.commands.fill_1 import Fill
from structure_generator.commands.setblock_1 import SetBlock

class VersionJE1152(Version):
	def __init__(self):
		pass
	
	def clone(self, pos1, pos2, pos3):
		return Clone(pos1, pos2, pos3)
		
	def fill(self, pos1, pos2, block):
		return Fill(pos1, pos2, block)
		
	def setblock(self, pos, block):
		return SetBlock(pos, block)
		
	def base_block(self):
		return BaseBlock()
		
	def redstone_dust(self):
		return RedstoneDust()
		
	def redstone_torch(self, facing):
		return RedstoneTorch(facing)
		
	def repeater(self, facing):
		return Repeater(facing)
	
	def air(self):
		return Air()