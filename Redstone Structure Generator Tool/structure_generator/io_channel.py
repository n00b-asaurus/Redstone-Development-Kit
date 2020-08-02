def singleton(cls):
	instances = {}
	def wrapper(*args, **kwargs):
		if cls not in instances:
			instances[cls] = cls(*args, **kwargs)
		return instances[cls]
	return wrapper
	
@singleton
class IOChannel:
	def __init__(self,):
		pass
	
	def print(self, message):
		print(message)
		
	def input(self, header = ""):
		return input(header)