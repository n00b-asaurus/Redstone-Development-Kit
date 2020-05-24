from logic_analyzer.signal import Signal

class BitSignal(Signal):
	def __init__(self, name, raw_signal, length):
		self.name = name
		self.raw_signal = raw_signal
		self.length = length
		'''
		Example: 
			{206:False,280:True,282:False,}
		'''
	
	@staticmethod
	def match_input(input):
		boolean_pattern = compile(r'^(true|false)$')
		return search(boolean_pattern, input) != None
		
	@staticmethod
	def format_input(input):
		if input == 'true': return True
		if input == 'false': return False
		
	def render_channel(self, screen):
		screen.draw_line([(0.0,0.0),(self.length, 0.0)],fill=GRID)
		screen.draw_line([(0.0,1.0),(self.length, 1.0)],fill=GRID)
		state = {None:"",False:"",True:""}
		line_y = {None:0.5,False:1.0,True:0.0}
		def render_wave(last_signal, signal, start, stop):
			#halfway_point = int((stop - start) / 2 + start)
			screen.draw_line([(start,line_y[last_signal]),(stop,line_y[last_signal])])
			screen.draw_line([(stop,line_y[last_signal]),(stop,line_y[signal])])
				#if start == halfway_point:
				#	screen.draw_text("{}".format(self.state[signal]),(halfway_point, 0.5))
				#start += 1
		
		last_signal = None
		pointer = 0.0
		for timestamp, signal in self.raw_signal.items():
			render_wave(last_signal, signal, pointer, timestamp)
			pointer = timestamp
			last_signal = signal
		pointer = render_wave(last_signal, last_signal, pointer, self.length)
			
from re import compile, search
from logic_analyzer.colors import GRID