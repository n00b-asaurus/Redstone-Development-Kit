class ArgumentHandler:
	def __init__(self):
		self.return_list=True
		
	def handle(self, arguments):
		arguments = self._scrub_arguments(arguments)
		argument_values = self._get_values_from_arguments(arguments)
		if self.return_list: return argument_values
		else: return argument_values[0]
	
	def _get_values_from_arguments(self, arguments):
		argument_values = []
		for argument in arguments:
			value = self._get_value_from_argument(argument)
			argument_values.append(value)
		return argument_values
		
	def _get_value_from_argument(self, argument):
		header_format = "{} - {} > ".format(argument.name, argument.help)
		error_format = "{{}} is not a valid option. Try {}".format(argument.choices)
		value = self._get_input_and_check_against_valid_options(header_format, argument.choices, error_format)
		return value
		
	def _scrub_arguments(self, arguments):
		self.return_list = True
		if type(arguments) != list:
			self.return_list = False
			arguments = [arguments]
		return arguments
			
	def _get_input_and_check_against_valid_options(self, header, valid_inputs, error_message_format):
		while True:
			user_input = input(header)
			if valid_inputs == None or user_input in valid_inputs:
				return user_input
			print(error_message_format.format(user_input))