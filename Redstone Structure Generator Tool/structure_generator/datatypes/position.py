class Position:
	def __init__(self, x, y ,z):
		self.x = x
		self.y = y
		self.z = z
		
	def translate(self, x, y, z):
		self.x += x
		self.y += y
		self.z += z
	
	def rotate(self, amount):
		for i in range(amount % 4):
			self.x, self.z = -self.z, self.x
		
	def __repr__(self):
		return "~{} ~{} ~{}".format(self.x, self.y, self.z)