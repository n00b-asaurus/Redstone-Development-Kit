from minecraft_environment.version import Version
from minecraft_environment.blocks.base_block_1 import BaseBlock
from minecraft_environment.blocks.redstone_dust_1 import RedstoneDust
from minecraft_environment.blocks.redstone_torch_1 import RedstoneTorch
from minecraft_environment.blocks.repeater_1 import Repeater
from minecraft_environment.blocks.air_1 import Air
from minecraft_environment.commands.clone_1 import Clone
from minecraft_environment.commands.fill_1 import Fill
from minecraft_environment.commands.setblock_1 import SetBlock



class VersionJE1152(Version):
	def __init__(self):
		self.mcfunctions_require_forwardslash = False
	
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