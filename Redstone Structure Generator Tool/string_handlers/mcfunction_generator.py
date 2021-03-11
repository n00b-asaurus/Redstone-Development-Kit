class McFunctionGenerator:
	def __init__(self,):
		print("Saving structure to structure.mcfunction")
		self.file = open("structure.mcfunction", "w")
		
	def handle(self, commands):
		self.file.write("\n".join(commands))
		
	def close(self,):
		self.file.close()
		print("Structure saved!")
		
		