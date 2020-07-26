import logging

logger = logging.getLogger()

class TextLoader:
	def __init__(self, log_address):
		logger.debug("Constructing TextLoader with log address {}".format(log_address))
		with open(log_address) as f:
			logger.debug("Opened file - read lines")
			log = f.readlines()
			logger.debug("init text array")
			self.text = []
			i = -1
			logger.debug("Searching for latest start")
			while "Executed 2 commands from function 'logic_analyzer:commands/start'" not in log[i]: 
				logger.debug("skipping {}".format(log[i]))
				i -= 1
			i += 1
			while "Executed 1 commands from function 'logic_analyzer:commands/stop'" not in log[i]: 
				logger.debug("adding {}".format(log[i]))
				self.text.append(log[i])
				i += 1
		
		
	def get_text(self,):
		return self.text