class TimingCollector:
	def __init__(self, text_source):
		self.text_source 		= text_source
		self.channels 			= {} #channel template name:{type:comment,signal:{}}
		self.last_time 			= 0
		self.time_pattern 		= compile(r'time:(\d*),')
		self.channel_pattern 	= compile(r'channel:(.*),')
		self.state_pattern 		= compile(r'state:(.*)$')
		self.longest_tvalue 	= 0
		self.signal_classes		= collect_child_classes(base_class = Signal, file_path = 'logic_analyzer.signals')
		'''
		examples of log output
		player 				[CHAT] <n00b_asaurus> comment: your mom
		say executed 		[test_probe] hello world
							[CHAT] [test_probe] hello world
		say 				[@] comment: blah blah blah
		tellraw 			[CHAT] Welcome to Minecraft Tools
		tellraw executed 	[CHAT] my name is test_probe and my value is 69

		formats:
			bit channel:	time:300,channel:probe 1,state:true
			word channel:	time:300,channel:probe 2,state:23
			comments: 		time:301,channel:comment,state:write something here!
		'''

	
	def get_raw_info(self):
		text = self.text_source.get_text() #return as a list, one line per index
		for line in text:
			self._parse_line(line)
		self.longest_tvalue += 20
		
		channel_objects = []
		for name, data in self.channels.items():
			channel_objects.append(data["type"](name,data["signal"],self.longest_tvalue))
		return channel_objects
	
	def _parse_line(self, line):
		if "[CHAT]" not in line and "[@]" not in line:
			return
		try:
			time = int(search(self.time_pattern,line).group(1))
			channel = search(self.channel_pattern, line).group(1)
			state = search(self.state_pattern, line).group(1)
			self.longest_tvalue = max(time,self.longest_tvalue)
		except Exception:
			return
		
		if channel not in self.channels:
			self.channels[channel] = {"type":self._match_signal_class(state),"signal":{}}
		self.channels[channel]["signal"][time] = self.channels[channel]["type"].format_input(state)
			
	def _match_signal_class(self, value):
		for signal_class in self.signal_classes:
				if signal_class.match_input(value):
					return signal_class
				
				
from re import compile, match, search
from toolbox.class_collector.class_collector import collect_child_classes
from logic_analyzer.signal import Signal