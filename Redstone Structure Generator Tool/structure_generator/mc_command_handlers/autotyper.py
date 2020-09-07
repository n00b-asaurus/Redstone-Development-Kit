from structure_generator.mc_command_handler import MCCommandHandler
from pydirectinput import press, keyDown, keyUp
from pyperclip import copy
from time import sleep

class AutoTyper(MCCommandHandler):
	def __init__(self,):
		input('Structure ready, press Enter to begin building...')
		print('Building in 5')
		sleep(1)
		print('4')
		sleep(1)
		print('3')
		sleep(1)
		print('2')
		sleep(1)
		print('1')
		sleep(1)
		print('Building...')
		
	def handle(self, string):
		copy(string)
		press('/')
		keyDown('ctrl')
		keyDown('v')
		keyUp('v')
		keyUp('ctrl')
		press('enter')
		
	def close(self,):
		print("Build Complete")