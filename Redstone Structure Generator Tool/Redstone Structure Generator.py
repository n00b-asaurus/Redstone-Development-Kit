from structure_generator.generator import generate
from structure_generator.argument_handler import ArgumentHandler
from structure_generator.argument import Argument
from structures.basic_encoder.encoder import Encoder as BasicEncoder
from structures.properinglish19_decoder.decoder import Decoder as ProperinglishDecoder
from structures.stenodyon_decoder.decoder import Decoder as StenodyonDecoder
#from string_handlers.autotyper import AutoTyper
from string_handlers.mcfunction_generator import McFunctionGenerator
from argparse import ArgumentParser
import traceback

structures = {
	"basic_encoder": BasicEncoder,
	"stenodyon_decoder": StenodyonDecoder,
	"properinglish19_decoder": ProperinglishDecoder,
}

argument_handler = ArgumentHandler()

def main(structure=None):
	if structure in structures.keys():
		Structure = structures[structure]
	elif structure in structures.values():
		Structure = structure
	else:
		if structure:
			# If we got here and structure is set then the user gave bad input
			print(f"'{structure}' isn't a valid structure name.")
		Structure = structures[argument_handler.handle(Argument("STRUCTURE", "What kind of structure is being built?", ", ".join(structures.keys())))]

	try:
		commands = generate(Structure(), argument_handler)
		command_output = McFunctionGenerator()
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

	args = parser.parse_args()
	main(args.structure)