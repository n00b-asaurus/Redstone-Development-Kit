from logic_analyzer.screen_renderer import ScreenRenderer
	
class RedstoneLogicAnalyzer:
	def __init__(self):
		self.log_address 		= ""
		self.channels_to_render = None
		self.renderer			= ScreenRenderer()
	
	def main(self):
		self._collect_arguments()
		self._render_and_save_image()
		self._report_failed_channels()
	
	def _collect_arguments(self):
		self.log_address 		= input("Where's latest.log? > ")
		self.channels_to_render = input("What channels are being rendered? > ")
		
	def _render_and_save_image(self):
		render = self.renderer.render_log(self.log_address , self.channels_to_render)
		render.save('.\image.png')
		print("Generation Complete!")
		
	def _report_failed_channels(self):
		failures = self.renderer.report_failed_signals()
		print("{} Channels Failed to Render".format(len(failures)))
		if len(failures) > 0:
			self._list_failed_channel_names()
		
	def _list_failed_channel_names(self):
		print("Failed Channels:")
		for failure in self.renderer.report_failed_signals():
			print(failure)
	
try:		
	RedstoneLogicAnalyzer().main()
except Exception as e:
	print("Encountered Exception: {}".format(e))
input("Press Enter to Continue...")