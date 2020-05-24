class TextLoader:
	def __init__(self, log_address):
		with open(log_address) as f:
			log = f.readlines()
			self.text = []
			i = -1
			while "[CHAT] Executed 2 commands from function 'logic_analyzer:start'" not in log[i]: 
				#print("skipping {}".format(log[i]))
				i -= 1
			i += 1
			while "[n00b_asaurus: Executed 1 commands from function 'logic_analyzer:stop']" not in log[i]: 
				#print("adding {}".format(log[i]))
				self.text.append(log[i])
				i += 1
		# [CHAT] Executed 2 commands from function 'logic_analyzer:start'
		# target text
		# [n00b_asaurus: Executed 1 commands from function 'logic_analyzer:stop']
		
		
	def get_text(self,):
		return self.text