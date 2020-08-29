from logic_analyzer.screen_renderer import ScreenRenderer
	
try:		
	log = input("Where's latest.log? > ")
	channels_to_render = input("What channels are being rendered? > ")
	render = ScreenRenderer().render_log(log, channels_to_render)
	render.save('.\image.png')
	print("Generation Complete!")
except Exception as e:
	print("Encountered Exception: {}".format(e))
input("Press Enter to Continue...")