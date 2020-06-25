from logic_analyzer.signal import Signal

class WordSignal(Signal):
	def __init__(self, name, raw_signal, length):
		self.name = name
		self.raw_signal = raw_signal
		self.length = length
		'''
		Example: 
			{22:254,24:-18,26:-78,52:0,}
		'''
	
	@staticmethod
	def match_input(input):
		word_pattern = compile(r'^\d+$')
		return search(word_pattern, input) != None
		
	@staticmethod
	def format_input(input):
		return int(input)
	
	def render_channel(self, screen):
		screen.draw_line([(0.0,0.0),(self.length, 0.0)],fill=GRID)
		screen.draw_line([(0.0,1.0),(self.length, 1.0)],fill=GRID)
		def render_wave(signal, start,stop):
			if signal == None:
				screen.draw_line([(start,0.5),(stop,0.5)])
			elif stop - start < 2:
				screen.draw_line([(start,0.5),(stop,0.5)])
			else:
				screen.draw_line([(start,0.5),(start+1.0,0.0)])
				screen.draw_line([(start,0.5),(start+1.0,1.0)])
				
				screen.draw_line([(start+1.0,0.0),(stop-1.0,0.0)])
				screen.draw_line([(start+1.0,1.0),(stop-1.0,1.0)])
					
				
				screen.draw_line([(stop-1.0,0.0),(stop,0.5)])
				screen.draw_line([(stop-1.0,1.0),(stop,0.5)])
				
				halfway_point = int((stop - start) / 2 + start)
				screen.draw_text("0x{:04X}".format(signal), (halfway_point,0.5))
			return stop
		
		last_signal = None
		pointer = 0.0
		for timestamp, signal in self.raw_signal.items():
			pointer = render_wave(last_signal, pointer, timestamp)
			last_signal = signal
		pointer = render_wave(last_signal, pointer, self.length)
		
from re import compile, search
from logic_analyzer.colors import GRID