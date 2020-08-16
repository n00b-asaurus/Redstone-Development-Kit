from structure_generator.mc_command_handler import MCCommandHandler
import py4j
import os
import logging
log = logging.getLogger()
from structure_generator.io_channel import IOChannel
from time import sleep
console = IOChannel()

class AutoTyper(MCCommandHandler):
	def __init__(self,):
		log.debug('Launching AutoTyper.jar')
		os.system('start /min cmd.exe @cmd /k "launch_auto_typer.bat"')
		gateway = py4j.java_gateway.JavaGateway()
		self.autotyper = gateway.entry_point.getAutoTyper()
		console.input('Structure ready, press Enter to begin building...')
		console.print('Building in 5')
		sleep(1)
		console.print('4')
		sleep(1)
		console.print('3')
		sleep(1)
		console.print('2')
		sleep(1)
		console.print('1')
		sleep(1)
		console.print('Building...')
		
	def handle(self, string):
		log.debug('Sending command: {}'.format(string))
		self.autotyper.typeString(string)
		
	def close(self,):
		log.debug('Closing AutoTyper.jar')
		log.debug('This may result in errors')
		log.debug('These can be ignored...\n\n\n')
		try:
			self.autotyper.exit()
		except Exception:
			pass
		log.debug('\n\n\nAutoTyper.jar successfully closed\n')