from unittest import TestCase
from structure_generator.generator import generate
from structure_generator.structure import Structure
from structure_generator.argument import Argument
from minecraft_environment.position import Position
from minecraft_environment.minecraft import fill, clone, setblock, base_block, redstone_dust, redstone_torch, repeater

class TestStructureA(Structure):
	def generate_build(self, length, width, height):
		self._add_command(clone(Position(0,0,0),Position(length,height,width),Position(length+1,0,width+1)))
	
	def register_arguments(self):
		arguments = [
			Argument("Length", "The length of the structure"),
			Argument("Width", "The width of the structure"),
			Argument("Height", "The height of the structure"),
		]
		return arguments
		
class TestStructureB(Structure):
	def generate_build(self, length, width, height):
		self._add_command(clone(Position(0,0,0),Position(width,height,length),Position(width+1,0,length+1)))
	
	def register_arguments(self):
		arguments = [
			Argument("Length", "The length of the structure"),
			Argument("Width", "The width of the structure"),
			Argument("Height", "The height of the structure"),
		]
		return arguments
		
class TestStructureC(Structure):
	def generate_build(self, length, width, height, rotation):
		self._add_command(clone(Position(0,0,0),Position(width,height,length),Position(width+1,0,length+1)))
		self._rotate(rotation)
	
	def register_arguments(self):
		arguments = [
			Argument("Length", "The length of the structure"),
			Argument("Width", "The width of the structure"),
			Argument("Height", "The height of the structure"),
			Argument("Rotation", "The rotation of the structure"),
		]
		return arguments

class TestArgumentHandlerA:
	def __init__(self):
		pass
		
	def handle (self, arguments):
		argument_values = []
		for argument in arguments:
			if argument.name == "Length": argument_values.append(20)
			if argument.name == "Width": argument_values.append(35)
			if argument.name == "Height": argument_values.append(10)
		return argument_values
		
class TestArgumentHandlerB:
	def __init__(self):
		pass
		
	def handle (self, arguments):
		argument_values = []
		for argument in arguments:
			if argument.name == "Length": argument_values.append(18)
			if argument.name == "Width": argument_values.append(99)
			if argument.name == "Height": argument_values.append(50)
		return argument_values
		
class TestArgumentHandlerC:
	def __init__(self):
		pass
		
	def handle (self, arguments):
		argument_values = []
		for argument in arguments:
			if argument.name == "Length": argument_values.append(1)
			if argument.name == "Width": argument_values.append(0)
			if argument.name == "Height": argument_values.append(0)
			if argument.name == "Rotation": argument_values.append(3)
		return argument_values

class TestGenerator(TestCase):
	def test_generate_clone(self):
		commands = generate(TestStructureA(),TestArgumentHandlerA())
		self.assertEqual(commands, ["clone ~0 ~0 ~0 ~20 ~10 ~35 ~21 ~0 ~36"])	
		
	def test_generate_clone_with_different_structure(self):
		commands = generate(TestStructureB(),TestArgumentHandlerA())
		self.assertEqual(commands, ["clone ~0 ~0 ~0 ~35 ~10 ~20 ~36 ~0 ~21"])	
		
	def test_generate_clone_with_different_argument_handler(self):
		commands = generate(TestStructureA(),TestArgumentHandlerB())
		self.assertEqual(commands, ["clone ~0 ~0 ~0 ~18 ~50 ~99 ~19 ~0 ~100"])
		
	#def test_generate_clone_with_rotate(self):
	#	commands = generate(TestStructureC(),TestArgumentHandlerC())
	#	self.assertEqual(commands, ["clone ~0 ~0 ~0 ~0 ~0 ~-1 ~1 ~0 ~-2"])