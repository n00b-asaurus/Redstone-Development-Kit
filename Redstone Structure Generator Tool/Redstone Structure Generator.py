from structure_generator.generator import generate
from structure_generator.argument_handler import ArgumentHandler
from structure_generator.argument import Argument
from structures.basic_encoder.encoder import Encoder as BasicEncoder
from structures.properinglish19_decoder.decoder import Decoder as ProperinglishDecoder
from structures.stenodyon_decoder.decoder import Decoder as StenodyonDecoder
from string_handlers.autotyper import AutoTyper
from string_handlers.mcfunction_generator import McFunctionGenerator
from argparse import ArgumentParser
import traceback

structures = {
	"basic_encoder": BasicEncoder,
	"stenodyon_decoder": StenodyonDecoder,
	"properinglish19_decoder": ProperinglishDecoder,
}

outputs = {
	"autotyper": AutoTyper,
	"mcfunction": McFunctionGenerator,
}

argument_handler = ArgumentHandler()

def pick_class_from_dictionary(name, help, dictionary):
	valid_options = ", ".join(dictionary.keys())
	users_choice = Argument(name, help, valid_options)
	key = argument_handler.handle(users_choice)
	return dictionary[key]
	

def main(structure=None, output=None):
	if structure in structures.keys():
		Structure = structures[structure]
	elif structure in structures.values():
		Structure = structure
	else:
		if structure:
			# If we got here and structure is set then the user gave bad input
			print(f"'{structure}' isn't a valid structure name.")
		Structure = pick_class_from_dictionary("STRUCTURE", "what kind of structure is being built?", structures)

	try:
		commands = generate(Structure(), argument_handler)
		if output == None:
			command_output = pick_class_from_dictionary("OUTPUT", "how would you like to process this structure", outputs)()
		else:
			command_output = outputs[output]()
		command_output.handle(commands)
		command_output.close()
	except Exception as e:
		print("Encountered Exception: {}".format(e))
		
	input("Press Enter to Continue...")

if __name__ == "__main__":
	parser = ArgumentParser()
	structure_arg_group = parser.add_mutually_exclusive_group()
	structure_arg_group.add_argument("-s", "--structure", help="The name of the structure to build (must match exactly).")
	structure_arg_group.add_argument("-e", "--basic_encoder", action="store_const", const="basic_encoder", dest="structure", help="Build the basic_encoder.")
	structure_arg_group.add_argument("-d", "--stenodyon_decoder", action="store_const", const="stenodyon_decoder", dest="structure", help="Build the stenodyon_decoder.")
	structure_arg_group.add_argument("-p", "--properinglish19_decoder", action="store_const", const="properinglish19_decoder", dest="structure", help="Build the properinglish19_decoder.")
	output_group = parser.add_mutually_exclusive_group()
	output_group.add_argument("-a","--autotyper",action="store_const", const="autotyper", dest="output", help="Type the build commands directly into chat")
	output_group.add_argument("-m","--mcfunction",action="store_const", const="mcfunction", dest="output", help="Save the build commands to an mcfunction file")

	args = parser.parse_args()
	main(args.structure, args.output)