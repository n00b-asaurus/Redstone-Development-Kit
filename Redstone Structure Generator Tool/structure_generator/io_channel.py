from toolbox.singleton.singleton import singleton

@singleton
class IOChannel:
	def __init__(self,):
		pass
	
	def print(self, message):
		print(message)
		
	def input(self, header = ""):
		return input(header)