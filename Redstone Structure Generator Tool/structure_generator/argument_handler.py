class ArgumentHandler:
	def __init__(self):
		pass
		
	def handle(self, arguments):
		return_list = True
		if type(arguments) != list:
			return_list = False
			arguments = [arguments]
		argument_values = []
		for argument in arguments:
			header_format = "{} - {} > ".format(argument.name, argument.help)
			error_format = "{{}} is not a valid option. Try {}".format(argument.choices)
			value = self._get_input_and_check_against_valid_options(header_format, argument.choices, error_format)
			argument_values.append(value)
		if return_list:
			return argument_values
		else:
			return argument_values[0]
			
	def _get_input_and_check_against_valid_options(self, header, valid_inputs, error_message_format):
		while True:
			user_input = input(header)
			if valid_inputs == None or user_input in valid_inputs:
				return user_input
			print(error_message_format.format(user_input))