class TextLoader:
	def __init__(self, log_address):
		with open(log_address) as f:
			log = f.readlines()
			self.text = []
			i = -1
			while "Executed 2 commands from function 'logic_analyzer:commands/start'" not in log[i]: 
				i -= 1
			i += 1
			while "Executed 1 commands from function 'logic_analyzer:commands/stop'" not in log[i]: 
				self.text.append(log[i])
				i += 1
		
		
	def get_text(self,):
		return self.text