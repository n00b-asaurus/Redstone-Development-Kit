from structure_generator.datatypes.structure import Structure
from structure_generator.mc_command_handlers.autotyper import AutoTyper
from structure_generator.versions.version_je1152 import VersionJE1152
from structure_generator.constructor import Constructor
from structure_generator.io_channel import IOChannel
from structure_generator import minecraft
from bulk_import import import_subclasses

constructor_classes = import_subclasses(base_class = Constructor, directory = "structure_generator.constructors", deepest_level = 1)
constructors = {}
for constructor in constructor_classes:
	constructors[constructor.register()] = constructor
	
console = IOChannel()

def get_input_and_check_against_valid_options(header, valid_inputs, error_message_format):
	while True:
		_input = console.input(header)
		if _input in valid_inputs:
			return _input
		console.print(error_message_format.format(_input))


try:

	minecraft.set_version(VersionJE1152())
	structure_name = get_input_and_check_against_valid_options(
		header = "STRUCTURE - What kind of structure is being built? > ", 
		valid_inputs = ['basic_encoder','stenodyon_decoder','properinglish19_decoder'], 
		error_message_format = "{} is not a valid structure, try 'basic_encoder', 'stenodyon_decoder', or 'properinglish19_decoder'"
	)
	
	file = console.input("FILE - Where's the source file? > ")
	io_side = get_input_and_check_against_valid_options(
		header = "IO_SIDE - What side does the IO build towards? > ",
		valid_inputs = ['left', 'right'],
		error_message_format = "{} is not a valid input, try 'left' or 'right'"
	)
	
	structure = Structure(constructor = constructors[structure_name](file, io_side))
	
	build_to = get_input_and_check_against_valid_options(
		header = "BUILD_TO - What direction is the structure being built towards? > ",
		valid_inputs = ['left', 'right'],
		error_message_format = "{} is not a valid input, try 'left' or 'right'"
	)
	
	if build_to == 'left':
		structure.translate(0,0,-structure.size[2])
		
	facing = get_input_and_check_against_valid_options(
		header = "FACING = What direction are you facing? > ",
		valid_inputs = ['north','south','east','west'],
		error_message_format = "{} is not a valid direction, try 'north', 'south', 'east', or 'west'"
	)
	facing_translator = {'east':0,'west':2,'south':1,'north':3}
	structure.rotate(facing_translator[facing])

	offset = console.input("OFFSET - where is the structure being moved to? > ")
	if offset != "": offset = "0,0,0"
	structure.translate(int(offset.split(',')[0]),int(offset.split(',')[1]),int(offset.split(',')[2]))
	structure.build(command_handler = AutoTyper())


except Exception as e:
	console.print("Encountered Exception: {}".format(e))
	
console.input("Press Enter to Continue...")