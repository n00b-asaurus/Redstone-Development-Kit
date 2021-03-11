from logic_analyzer.screen_renderer import ScreenRenderer
from argparse import ArgumentParser
import os
from pathlib import Path


class RedstoneLogicAnalyzer:
	input_tries_before_exit_prompt = 2

	def __init__(self, image_save_path, log_address=None, channels_to_render=None):
		self.image_save_path    = image_save_path
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
		if self.log_address:
			# If log_address is None then we are still waiting for user input, no need to check validity.
			log_address_valid = os.path.isfile(self.log_address)
		else:
			log_address_valid = False
		
		multiple_try_message = ""
		try_count = 0

		while not log_address_valid:
			try_count += 1
			if try_count == self.input_tries_before_exit_prompt:
				multiple_try_message = " (type 'exit' to exit script)"

			if self.log_address:
				# Don't bug the user about None not being a valid file, they haven't even given any input yet.
				print(f"{self.log_address} is not a valid file path.")
			self.log_address = input(f"Where's latest.log?{multiple_try_message} > ")
			if self.log_address == "exit":
				exit("Script aborted at log address input.")
			log_address_valid = os.path.isfile(self.log_address)

		if self.channels_to_render is None:
			self.channels_to_render = input("What channels are being rendered? > ")
		
	def _render_and_save_image(self):
		render = self.renderer.render_log(self.log_address , self.channels_to_render)
		render.save(self.image_save_path)
		print("Generation Complete!")
		print(f"Image saved as: {image_save_path}")
		
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
	parser.add_argument("-i", "--image_name", type=str, default="image.png", help="Path to location to save image. If name doesn't end in .png then .png will be appended or replace the given extension.")

	args = parser.parse_args()
	log_address = args.log
	channels_to_render = args.channels
	if channels_to_render is not None:
		channels_to_render = " ".join(channels_to_render)
	
	# Strip extra . off the right end if there are extras and then make sure the suffix is .png
	image_save_path = Path(args.image_name.rstrip(".")).with_suffix(".png")

	try:
		RedstoneLogicAnalyzer(image_save_path, log_address, channels_to_render).main()
	except Exception as e:
		print("Encountered Exception: {}".format(e))
	input("Press Enter to Continue...")