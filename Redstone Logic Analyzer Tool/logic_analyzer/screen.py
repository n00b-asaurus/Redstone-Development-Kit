from logic_analyzer.colors import BACKGROUND, GRID, SIGNAL

class Screen:
	def __init__(self, size=None):
		self.size = size
		self.vertical_scale = 20.0
		self.vertical_offset = 0.0
		self.horizontal_scale = 5.0
		self.horizontal_offset = 0.0
		self.channel_offset = 0.0
		if self.size != None:
			self.screen = Image.new(mode = "RGBA", size = self.size, color = BACKGROUND)
			self.draw = ImageDraw.Draw(self.screen)
	
	def render(self, signals):
		if self.size == None:
			self._infer_screen_size_from_channels(signals)
		self._draw_tick_lines(signals[0].length)
		self._draw_channels(signals)
		return self.screen
	
	def _draw_channels(self,signals):
		self.channel_offset = 0.3 * self.vertical_scale
		for signal in signals:
			signal.render_channel(self)
			self._draw_channel_name_every_100_pixels(signal)
			self.channel_offset += 1.3 * self.vertical_scale
			
	def _draw_channel_name_every_100_pixels(self,signal):
		for x in range(0, signal.length,100):
			self.draw_text(signal.name, (x + 5.0, 0.0))
		
	def _draw_tick_lines(self, number_of_ticks):
		for x in range(number_of_ticks):
			self.draw_line([(x,0.0),(x,100.0)],fill = GRID)
		
	def _infer_screen_size_from_channels(self, signals):
		size = (int(signals[0].length * self.horizontal_scale), int((len(signals) * self.vertical_scale * 1.3) + (self.vertical_scale * 0.3))) 
		self.screen = Image.new(mode = "RGBA", size = size, color = BACKGROUND)
		self.draw = ImageDraw.Draw(self.screen)
		
	def draw_line(self, coords, fill = SIGNAL):
		x1 = coords[0][0] * self.horizontal_scale + self.horizontal_offset
		y1 = coords[0][1] * self.vertical_scale + self.vertical_offset + self.channel_offset
		x2 = coords[1][0] * self.horizontal_scale + self.horizontal_offset
		y2 = coords[1][1] * self.vertical_scale + self.vertical_offset + self.channel_offset
		self.draw.line([(x1,y1),(x2,y2)], fill = fill, width = 1)
		
	def draw_text(self, text, coords):
		x, y = coords[0] * self.horizontal_scale + self.horizontal_offset, coords[1] * self.vertical_scale + self.vertical_offset + self.channel_offset
		self.draw.text((x,y), text = text, fill = SIGNAL, align = "center")
		
from PIL import Image, ImageDraw
