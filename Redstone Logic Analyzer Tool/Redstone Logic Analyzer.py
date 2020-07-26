from logic_analyzer.screen import Screen
from logic_analyzer.timing_collector import TimingCollector
from logic_analyzer.text_loader import TextLoader

try:
	log_address = input("Where's latest.log? > ").replace('"','')
	text_loader = TextLoader(log_address)
	timing_collector = TimingCollector(text_loader)
	signals = timing_collector.get_raw_info()
	visible_signals = [channel.strip() for channel in input("What channels are being rendered? > ").split('|')]
	if visible_signals == ['']:
		visible_signals = signals
	else:
		for signal in signals:
			if signal.name in visible_signals:
				visible_signals[visible_signals.index(signal.name)] = signal
	screen = Screen()
	render = screen.render(visible_signals)
	render.save('.\image.png')
	print("Generation Complete!")
	
except Exception as e:
	print("Encountered Exception: {}".format(e))
	
input("Press Enter to Continue...")