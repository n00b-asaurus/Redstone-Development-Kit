from logic_analyzer.screen import Screen
from logic_analyzer.timing_collector import TimingCollector
from logic_analyzer.text_loader import TextLoader


class ScreenRenderer:
	def __init__(self):
		self.signals = []
		self.visible_signals = []
		
	def render_log(self, log, channels=""):
		self._construct_environment_and_build_channel_objects(log)
		self._sort_or_hide_channel_objects(channels)
		return Screen().render(self.visible_signals)
			
	def _construct_environment_and_build_channel_objects(self, log):
		log_address = log.replace('"','')
		text_loader = TextLoader(log_address)
		timing_collector = TimingCollector(text_loader)
		self.signals = timing_collector.get_raw_info()
	
	def _sort_or_hide_channel_objects(self, channels):
		self.visible_signals = [channel.strip() for channel in channels.split('|')]
		if self.visible_signals == ['']:
			self.visible_signals = self.signals
		else:
			self._reorder_channel_objects()
	
	def _reorder_channel_objects(self,*channels):
		for signal in self.signals:
			if signal.name in self.visible_signals:
				signal_index = self.visible_signals.index(signal.name)
				self.visible_signals[signal_index] = signal