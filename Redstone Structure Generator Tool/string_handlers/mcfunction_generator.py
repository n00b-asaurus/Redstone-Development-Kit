from minecraft_environment.minecraft import mcfunctions_require_forwardslash

class McFunctionGenerator:
	def __init__(self,):
		print("Saving structure to structure.mcfunction")
		self.file = open("structure.mcfunction", "w")
		
	def handle(self, commands):
		if mcfunctions_require_forwardslash():
			commands = ["/" + command for command in commands]
		self.file.write("\n".join(commands))
		
	def close(self,):
		self.file.close()
		print("Structure saved!")
		
		