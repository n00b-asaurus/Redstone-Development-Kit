class Signal:
	def __init__(self, name, raw_signal, length):
		self.name = name
		self.raw_signal = raw_signal
		self.length = length
	
	@staticmethod
	def match_input(input):
		raise Excpetion("Signal Interface Class Being Used ")
	
	@staticmethod	
	def format_input(input):
		raise Excpetion("Signal Interface Class Being Used ")
		
	def render_channel(self, screen):
		raise Excpetion("Signal Interface Class Being Used ")