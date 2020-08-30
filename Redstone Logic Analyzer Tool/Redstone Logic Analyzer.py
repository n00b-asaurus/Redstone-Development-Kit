from logic_analyzer.screen_renderer import ScreenRenderer
	
try:		
	log = input("Where's latest.log? > ")
	channels_to_render = input("What channels are being rendered? > ")
	renderer = ScreenRenderer()
	render = renderer.render_log(log, channels_to_render)
	render.save('.\image.png')
	print("Generation Complete!")
	failures = renderer.report_failed_signals()
	print("{} Channels Failed to Render".format(len(failures)))
	if len(failures) > 0:
		print("Failed Channels:")
		for failure in failures:
			print(failure)
except Exception as e:
	print("Encountered Exception: {}".format(e))
input("Press Enter to Continue...")