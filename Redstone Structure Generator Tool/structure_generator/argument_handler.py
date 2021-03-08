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
		if argument.choices:
			value = self._get_input_and_check_against_valid_options(header_format, argument.choices)
		else:
			value = input(header_format)
		return value
		
	def _scrub_arguments(self, arguments):
		self.return_list = True
		if type(arguments) != list:
			self.return_list = False
			arguments = [arguments]
		return arguments
			
	def _get_input_and_check_against_valid_options(self, header, options):
		num_options = len(options)
		selected = None
		print(header)
		for i, option in enumerate(options):
			print(f"\t{i+1}: {option}")

		while not selected:
			user_input = input(f"Type out an option or give its index (1-{num_options}): ")
			
			try:
				option_index = int(user_input)
				if option_index > 0 and option_index <= num_options:
					selected = options[option_index-1]
				else:
					print(f"{option_index} is not a valid option.")
			except ValueError:
				# Check if any of the options starts with the user input. (Also works if the whole option is typed out.)
				# To match any option that contains the input instead change 'o.startswith(user_input)' to 'user_input in o'
				matching_options = [o for o in options if user_input in o] # List comprehension gives us a nice one liner.
				
				if len(matching_options) == 0:
					print("No options matched.")
				elif len(matching_options) == 1:
					selected = matching_options[0]
				else:
					print("Multiple options matched. Type out enough to match just one.")

		print(f"Selected: {selected}")
		return selected