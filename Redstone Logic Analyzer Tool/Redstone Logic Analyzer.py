from logic_analyzer.screen_renderer import ScreenRenderer
from argparse import ArgumentParser


class RedstoneLogicAnalyzer:
	def __init__(self, log_address=None, channels_to_render=None):
		self.log_address 		= log_address
		self.channels_to_render = channels_to_render
		self.renderer			= ScreenRenderer()
	
	def main(self):
		self._collect_arguments()
		self._render_and_save_image()
		self._report_failed_channels()
	
	def _collect_arguments(self):
		"""
		log_address: str
		channels_to_render: str

		If log_address or channels_to_render is None then the user will be prompted for it.
		"""
		if self.log_address is None:
			self.log_address 		= input("Where's latest.log? > ")

		if self.channels_to_render is None:
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


if __name__ == "__main__":
	# execute only if run as a script

	# Get arguments from the command line to make it easier to input the log path and repeat inputs
	parser = ArgumentParser()
	parser.add_argument("-l", "--log", type=str, help="Path to latest.log.")
	parser.add_argument("-c", "--channels", nargs="*", help="The probe names to render. Leave blank to use all channels in default order.")

	args = parser.parse_args()
	log_address = args.log
	channels_to_render = args.channels
	if channels_to_render is not None:
		channels_to_render = " ".join(channels_to_render)
	
	try:
		RedstoneLogicAnalyzer(log_address, channels_to_render).main()
	except Exception as e:
		print("Encountered Exception: {}".format(e))
	input("Press Enter to Continue...")