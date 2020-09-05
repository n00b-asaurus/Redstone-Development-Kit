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
		if type(signals) != list:
			signals = [signals]
		if self.size == None:
			size = (int(signals[0].length * self.horizontal_scale), int((len(signals) * self.vertical_scale * 1.3) + (self.vertical_scale * 0.3))) 
			self.screen = Image.new(mode = "RGBA", size = size, color = BACKGROUND)
			self.draw = ImageDraw.Draw(self.screen)
		for x in range(signals[0].length):
			self.draw_line([(x,0.0),(x,100.0)],fill = GRID)
		self.channel_offset = 0.3 * self.vertical_scale
		for signal in signals:
			signal.render_channel(self)
			for x in range(0, signal.length,100):
				self.draw_text(signal.name, (x + 5.0, 0.0))
			self.channel_offset += 1.3 * self.vertical_scale
		#still need to draw the timestamps, grids, and the channel headers
		return self.screen
		
	def draw_line(self, coords, fill = SIGNAL):
		x1, y1 = coords[0][0] * self.horizontal_scale + self.horizontal_offset, coords[0][1] * self.vertical_scale + self.vertical_offset + self.channel_offset
		x2, y2 = coords[1][0] * self.horizontal_scale + self.horizontal_offset, coords[1][1] * self.vertical_scale + self.vertical_offset + self.channel_offset
		self.draw.line([(x1,y1),(x2,y2)], fill = fill, width = 1)
		
	def draw_text(self, text, coords):
		x, y = coords[0] * self.horizontal_scale + self.horizontal_offset, coords[1] * self.vertical_scale + self.vertical_offset + self.channel_offset
		self.draw.text((x,y), text = text, fill = SIGNAL, align = "center")
		
from PIL import Image, ImageDraw
