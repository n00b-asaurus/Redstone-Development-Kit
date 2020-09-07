from minecraft_environment import minecraft
from minecraft_environment.versions.version_je1152 import VersionJE1152

def generate(structure, argument_handler, minecraft_version = VersionJE1152()):
	minecraft.set_version(minecraft_version)
	arguments = structure.register_arguments()
	argument_values = argument_handler.handle(arguments)
	structure.generate_build(*argument_values)
	return structure.get_build_commands()