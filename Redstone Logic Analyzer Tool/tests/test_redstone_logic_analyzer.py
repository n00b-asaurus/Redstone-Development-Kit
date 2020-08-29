from logic_analyzer.screen_renderer import ScreenRenderer
from PIL import Image
from unittest import TestCase

class TestScreenRenderer(TestCase):
	def test_render(self):
		render = ScreenRenderer().render_log("tests\\latestlogtest.txt")
		self.assertEqual(type(render),Image.Image)
		
	def test_render_size_for_all_channels(self):
		render = ScreenRenderer().render_log("tests\\latestlogtest.txt")
		self.assertEqual(render.size,(7600, 84))