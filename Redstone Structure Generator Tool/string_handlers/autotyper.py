from pydirectinput import press, keyDown, keyUp
from pyperclip import copy
from time import sleep

class AutoTyper:
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
		
	def handle(self, commands):
		for count, command in enumerate(commands):
			print("Entering command {} of {}:{}".format(count+1, len(commands), command))
			self._type_command(command)
		
	def _type_command(self, string):
		copy(string)
		press('/')
		keyDown('ctrl')
		keyDown('v')
		keyUp('v')
		keyUp('ctrl')
		press('enter')
		
	def close(self,):
		print("Build Complete")