import logging
from argparse import ArgumentParser
from structure_generator.datatypes.structure import Structure
from structure_generator.mc_command_handlers.autotyper import AutoTyper
from structure_generator.versions.version_je1152 import VersionJE1152
from structure_generator.io_channel import IOChannel
from structure_generator.constructor import Constructor
from structure_generator import minecraft
from toolbox.class_collector import collect_child_classes
constructors = collect_child_classes(base_class = Constructor, file_path = "structure_generator.constructors", instantiate = False, register_method = "register")

logging.basicConfig(
	filename = '.\\log.txt',
	level = logging.DEBUG,
	filemode = 'w',
	format = '%(levelname)s - %(message)s'
)

log = logging.getLogger()
console = IOChannel()

parser = ArgumentParser(description="generates a redstone structure based on a table text file and some arguments", prefix_chars='/')
parser.add_argument('/structure', action='store', required=True, help='the type of structure you wish to generate')
parser.add_argument('/file', action='store', required=True, help='the table used to generate the structure, must be in a .txt file')
parser.add_argument('/facing', action='store', required=True, choices=['north','south','east','west'], help='the direction the structure will be built towards')
parser.add_argument('/build_to', action='store', required=True, choices=['left','right'], help='the direction the structure will build towards')
parser.add_argument('/io_side', action='store', required=True, choices=['left','right'], help='which side the inputs or outputs will go to')
parser.add_argument('/offset', action='store', required=True, help='offset argument')
args = parser.parse_args()

log.info("Building {}".format(constructors[args.structure]))
minecraft.set_version(VersionJE1152())
structure = Structure(constructor = constructors[args.structure](args.file, args.io_side))
if args.build_to == 'left':
	structure.translate(0,0,-structure.size[2])
facing_translator = {'east':0,'west':2,'south':1,'north':3}
structure.rotate(facing_translator[args.facing])
structure.translate(int(args.offset.split(',')[0]),int(args.offset.split(',')[1]),int(args.offset.split(',')[2]))
structure.build(command_handler = AutoTyper())