from structures.properinglish19_decoder.build_handler import BuildHandler
from minecraft_environment.position import Position
from minecraft_environment.minecraft import fill, clone, setblock, base_block, redstone_dust, redstone_torch, repeater, air

class SingleNC(BuildHandler):
	def __init__(self):
		pass
	
	def type(self):
		return "single no connection build handler"
	
	def build_structure(self, commands, x, z):
		commands.append(fill(Position(x+1,0,z+0), Position(x+1,0,z+1), base_block()))
		commands.append(fill(Position(x+1,1,z+0), Position(x+1,1,z+1), redstone_dust()))
		commands.append(setblock(Position(x+0,1,z+0), base_block()))
		commands.append(fill(Position(x+0,2,z+0), Position(x+1,2,z+0), base_block()))
		commands.append(fill(Position(x+0,3,z+0), Position(x+1,3,z+0), redstone_dust()))
		
	def place_input_repeater(self, commands, x, z):
		commands.append(setblock(Position(x+0,3,z+0), repeater('+x')))
		
	
	def place_output_repeater(self, commands, x, z, direction, left, left_downline):
		commands.append(setblock(Position(x+1,1,z+1), repeater(direction)))