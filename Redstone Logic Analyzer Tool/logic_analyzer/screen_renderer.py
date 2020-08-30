from logic_analyzer.screen import Screen
from logic_analyzer.timing_collector import TimingCollector
from logic_analyzer.text_loader import TextLoader


class ScreenRenderer:
	def __init__(self):
		self.signals = []
		self.visible_signals = []
		self.failed_signals = []
		self.requested_signals = []
		self.temp_visible_signals = []
		
	def render_log(self, log, channels=""):
		self._load_log_and_build_channel_objects(log)
		self._pick_channel_objects_to_render(channels)
		return Screen().render(self.visible_signals)
		
	def report_rendered_signals(self):
		return self.visible_signals
		
	def report_failed_signals(self):
		return self.failed_signals
			
	def _load_log_and_build_channel_objects(self, log):
		log_address = log.replace('"','')
		text_loader = TextLoader(log_address)
		timing_collector = TimingCollector(text_loader)
		self.signals = timing_collector.get_raw_info()
	
	def _pick_channel_objects_to_render(self, channels):
		self.requested_signals = [channel.strip() for channel in channels.split('|')]
		if self.requested_signals == ['']:
			self.visible_signals = self.signals
		else:
			self._sort_and_hide_channel_objects()
	
	def _sort_and_hide_channel_objects(self):
		self.temp_visible_signals = [None,] * len(self.requested_signals)
		self._move_selected_signals_to_temp_and_remove_request()
		self.visible_signals = [signal for signal in self.temp_visible_signals if signal != None]
		self.failed_signals = [signal for signal in self.requested_signals if signal != None]
		
	def _move_selected_signals_to_temp_and_remove_request(self):
		for signal in self.signals:
			if signal.name in self.requested_signals:
				signal_index = self.requested_signals.index(signal.name)
				self.requested_signals[signal_index] = None
				self.temp_visible_signals[signal_index] = signal