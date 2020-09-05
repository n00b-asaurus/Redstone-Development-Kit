'''
		examples of log output
		player 				[CHAT] <n00b_asaurus> comment: hello world
		say executed 		[test_probe] hello world
							[CHAT] [test_probe] hello world
		say 				[@] comment: hello world
		tellraw 			[CHAT] hello world
		tellraw executed 	[CHAT] my name is test_probe and my value is 100

		formats:
			bit channel:	time:300,channel:probe 1,state:true
			word channel:	time:300,channel:probe 2,state:23
			comments: 		time:301,channel:comment,state:write something here!
'''

class LineDictFactory:
	def __init__(self):
		self.channel_dictionary = {}
		self.longest_tvalue 	= 0
		self.time_pattern 		= compile(r'time:(\d*),')
		self.channel_pattern 	= compile(r'channel:(.*),')
		self.state_pattern 		= compile(r'state:(.*)$')
		self.signal_classes		= [BitSignal, WordSignal]
		
	def parse_lines(self, lines):
		for line in lines:
			self._extract_data_and_add_to_channel_dictionary(line)
		self.longest_tvalue += 20
		return self.channel_dictionary, self.longest_tvalue
		
	def _extract_data_and_add_to_channel_dictionary(self, line):
		if "[CHAT]" not in line and "[@]" not in line:
			return
		time,channel,state = self._extract_data_from_line(line)
		self._add_data_to_channel_dictionary(time, channel, state)
		
	def _extract_data_from_line(self, line):
		try:
			time = int(search(self.time_pattern,line).group(1))
			channel = search(self.channel_pattern, line).group(1)
			state = search(self.state_pattern, line).group(1)
			self.longest_tvalue = max(time,self.longest_tvalue)
			return time, channel, state
		except Exception:
			return
	
	def _add_data_to_channel_dictionary(self, time, channel, state):
		if channel not in self.channel_dictionary:
			self._create_new_channel(channel, state)
		self.channel_dictionary[channel]["signal"][time] = self.channel_dictionary[channel]["type"].format_input(state)
		
	def _create_new_channel(self, channel, state):
		self.channel_dictionary[channel] = {"type":self._match_signal_class(state),"signal":{}}
		
	def _match_signal_class(self, value):
		for signal_class in self.signal_classes:
			if signal_class.match_input(value):
				return signal_class 


class TimingCollector:
	def __init__(self, text_source):
		self.text_source = text_source
		
	def get_raw_info(self):
		text = self.text_source.get_text() #return as a list, one line per index
		channel_dictionary,longest_tvalue = LineDictFactory().parse_lines(text)
		return self._contruct_objects_from_dictionary(channel_dictionary,longest_tvalue)
		
	def _contruct_objects_from_dictionary(self,channel_dictionary,longest_tvalue):
		channel_objects = []
		for name, data in channel_dictionary.items():
			channel_objects.append(data["type"](name,data["signal"],longest_tvalue))
		return channel_objects
	
				
				
from re import compile, match, search
# explicitly importing the modules because pyinstaller doesn't work with bulk import
from logic_analyzer.signals.bit_signal import BitSignal
from logic_analyzer.signals.word_signal import WordSignal