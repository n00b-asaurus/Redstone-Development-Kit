from structure_generator.generator import generate
from structure_generator.argument_handler import ArgumentHandler
from structure_generator.argument import Argument
from structures.basic_encoder.encoder import Encoder as BasicEncoder
from structures.properinglish19_decoder.decoder import Decoder as ProperinglishDecoder
from structures.stenodyon_decoder.decoder import Decoder as StenodyonDecoder
from string_handlers.autotyper import AutoTyper

structures = {
	"basic_encoder": BasicEncoder,
	"stenodyon_decoder": ProperinglishDecoder,
	"properinglish19_decoder": StenodyonDecoder,
}

argument_handler = ArgumentHandler()
structure = structures[argument_handler.handle(Argument("STRUCTURE", "What kind of structure is being built?", ", ".join(structures.keys())))]

try:
	commands = generate(structure(), argument_handler)
	command_output = AutoTyper()
	for count, command in enumerate(commands):
		print("Entering command {} of {}:{}".format(count+1, len(commands), command))
		command_output.handle(command)
	command_output.close()
except Exception as e:
	print("Encountered Exception: {}".format(e))
	
input("Press Enter to Continue...")