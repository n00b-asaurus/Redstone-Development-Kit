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
		
	def test_render_size_for_some_channels(self):
		render = ScreenRenderer().render_log("tests\\latestlogtest.txt","probe 1 | probe 2")
		self.assertEqual(render.size,(7600, 58)) 
		'''
		Each channel is 20 pixels tall with a 6 pixel space between channels. 
		The number of spacers will always be the number of channels +1.
		This means rendering 3 channels will result in 20 + 20 + 6 + 6 + 6, or 58.
		'''
		render = ScreenRenderer().render_log("tests\\latestlogtest.txt","probe 1 | probe 3")
		self.assertEqual(render.size,(7600, 58)) 
		render = ScreenRenderer().render_log("tests\\latestlogtest.txt","probe 3 | probe 2")
		self.assertEqual(render.size,(7600, 58)) 
		
	def test_render_size_for_one_channel(self):
		render = ScreenRenderer().render_log("tests\\latestlogtest.txt","probe 1")
		self.assertEqual(render.size,(7600, 32)) 
		render = ScreenRenderer().render_log("tests\\latestlogtest.txt","probe 2")
		self.assertEqual(render.size,(7600, 32)) 
		render = ScreenRenderer().render_log("tests\\latestlogtest.txt","probe 3")
		self.assertEqual(render.size,(7600, 32)) 
		
	def test_render_all_channels_in_specified_order(self):
		renderer = ScreenRenderer()
		render = renderer.render_log("tests\\latestlogtest.txt","probe 3 | probe 1 | probe 2")
		signals = renderer.report_rendered_signals()
		self.assertEqual(len(signals), 3)
		self.assertEqual(signals[0].name, "probe 3")
		self.assertEqual(signals[1].name, "probe 1")
		self.assertEqual(signals[2].name, "probe 2")
		self.assertEqual(render.size,(7600, 84))
		
	def test_render_all_channels_in_specified_order_with_nonexistant_channel(self):
		renderer = ScreenRenderer()
		render = renderer.render_log("tests\\latestlogtest.txt","probe 2 | grated_cheese | probe 3 | probe 1")
		signals = renderer.report_rendered_signals()
		self.assertEqual(len(signals), 3)
		self.assertEqual(signals[0].name, "probe 2")
		self.assertEqual(signals[1].name, "probe 3")
		self.assertEqual(signals[2].name, "probe 1")
		self.assertEqual(render.size,(7600, 84))
		failed_signals = renderer.report_failed_signals()
		self.assertEqual(len(failed_signals), 1)
		self.assertEqual(failed_signals[0], "grated_cheese")
		
	def test_render_all_channels_in_specified_order_with_multiple_nonexistant_channels(self):
		renderer = ScreenRenderer()
		render = renderer.render_log("tests\\latestlogtest.txt","probe 3 | grated_cheese | probe 2 | diced_tomatos | probe 1 | taco shell")
		signals = renderer.report_rendered_signals()
		self.assertEqual(len(signals), 3)
		self.assertEqual(signals[0].name, "probe 3")
		self.assertEqual(signals[1].name, "probe 2")
		self.assertEqual(signals[2].name, "probe 1")
		self.assertEqual(render.size,(7600, 84))
		failed_signals = renderer.report_failed_signals()
		self.assertEqual(len(failed_signals), 3)
		self.assertEqual(failed_signals[0], "grated_cheese")
		self.assertEqual(failed_signals[1], "diced_tomatos")
		self.assertEqual(failed_signals[2], "taco shell")