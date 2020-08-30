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
		self.line_y_values = {None:0.5,False:1.0,True:0.0}
		self.screen = None
	
	@staticmethod
	def match_input(input):
		boolean_pattern = compile(r'^(true|false)$')
		return search(boolean_pattern, input) != None
		
	@staticmethod
	def format_input(input):
		if input == 'true': return True
		if input == 'false': return False
		
	def render_channel(self, screen):
		self.screen = screen 
		self._render_grid()
		self._render_wave()
		
	
	def _render_grid(self):
		self.screen.draw_line([(0.0,0.0),(self.length, 0.0)],fill=GRID)
		self.screen.draw_line([(0.0,1.0),(self.length, 1.0)],fill=GRID)
	
	def _render_wave(self,):
		last_signal = None
		pointer = 0.0
		for timestamp, signal in self.raw_signal.items():
			self._render_wave_segment(last_signal, signal, pointer, timestamp)
			pointer = timestamp
			last_signal = signal
		self._render_wave_segment(last_signal, last_signal, pointer, self.length)
	
	def _render_wave_segment(self, last_signal, signal, start, stop):
		self.screen.draw_line([(start,self.line_y_values[last_signal]),(stop,self.line_y_values[last_signal])])
		self.screen.draw_line([(stop,self.line_y_values[last_signal]),(stop,self.line_y_values[signal])])
	
from re import compile, search
from logic_analyzer.colors import GRID