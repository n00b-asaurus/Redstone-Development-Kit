from unittest import TestCase
from unittest.mock import Mock, patch
from structure_generator.generator import generate
from structure_generator.structure import Structure
from structure_generator.argument import Argument
from structure_generator.argument_handler import ArgumentHandler
from minecraft_environment.position import Position
from minecraft_environment.minecraft import fill, clone, setblock, base_block, redstone_dust, redstone_torch, repeater

class TestGenerator(TestCase):
	def test_generate_clone(self):
		argument_handler = ArgumentHandler()
		argument_handler.handle = Mock()
		argument_handler.handle.return_value = [20,35,10]
		
		class MockStructure(Structure):
			def generate_build(self, length, width, height):
				self._add_command(clone(Position(0,0,0),Position(length,height,width),Position(length+1,0,width+1)))
			
			def register_arguments(self):
				return [
					Argument("Length", "The length of the structure"),
					Argument("Width", "The width of the structure"),
					Argument("Height", "The height of the structure"),
				]
		
		commands = generate(MockStructure(),argument_handler)
		self.assertEqual(commands, ["clone ~0 ~0 ~0 ~20 ~10 ~35 ~21 ~0 ~36"])	
	
	
	def test_generate_clone_with_different_structure(self):
		argument_handler = ArgumentHandler()
		argument_handler.handle = Mock()
		argument_handler.handle.return_value = [20,35,10]
		
		class MockStructure(Structure):
			def generate_build(self, length, width, height):
				self._add_command(clone(Position(0,0,0),Position(width,height,length),Position(width+1,0,length+1)))
			
			def register_arguments(self):
				return [
					Argument("Length", "The length of the structure"),
					Argument("Width", "The width of the structure"),
					Argument("Height", "The height of the structure"),
				]
		
		commands = generate(MockStructure(),argument_handler)
		self.assertEqual(commands, ["clone ~0 ~0 ~0 ~35 ~10 ~20 ~36 ~0 ~21"])	
		
		
	def test_generate_clone_with_different_argument_handler(self):
		argument_handler = ArgumentHandler()
		argument_handler.handle = Mock()
		argument_handler.handle.return_value = [18,99,50]
		
		class MockStructure(Structure):
			def generate_build(self, length, width, height):
				self._add_command(clone(Position(0,0,0),Position(length,height,width),Position(length+1,0,width+1)))
			
			def register_arguments(self):
				return [
					Argument("Length", "The length of the structure"),
					Argument("Width", "The width of the structure"),
					Argument("Height", "The height of the structure"),
				]
				
		commands = generate(MockStructure(),argument_handler)
		self.assertEqual(commands, ["clone ~0 ~0 ~0 ~18 ~50 ~99 ~19 ~0 ~100"])
		
		
	def test_generate_clone_with_rotate_90(self):
		'''This clone selects a quad from 0,0,0 to 1,1,1 and clones it to 2,0,2
		This whole selection is then rotated 90* clockwise.
		The positions in the clone command is going to change when rotating 
		to ensure the first position is always lower on the x-z coords than the second position.
		This test ensures this rule is respected.'''
		
		argument_handler = ArgumentHandler()
		argument_handler.handle = Mock()
		argument_handler.handle.return_value = [1,1,1,1]
		
		class MockStructure(Structure):
			def generate_build(self, length, width, height, rotation):
				self._add_command(clone(Position(0,0,0),Position(width,height,length),Position(width+1,0,length+1)))
				self._rotate(rotation)
			
			def register_arguments(self):
				return [
					Argument("Length", "The length of the structure"),
					Argument("Width", "The width of the structure"),
					Argument("Height", "The height of the structure"),
					Argument("Rotation", "The rotation of the structure"),
				]
		commands = generate(MockStructure(),argument_handler)
		self.assertEqual(commands, ["clone ~-1 ~0 ~0 ~0 ~1 ~1 ~-3 ~0 ~2"])
		
	def test_generate_clone_with_rotate_180(self):
		'''This clone selects a quad from 0,0,0 to 1,1,1 and clones it to 2,0,2
		This whole selection is then rotated 180* clockwise.
		The positions in the clone command is going to change when rotating 
		to ensure the first position is always lower on the x-z coords than the second position.
		This test ensures this rule is respected.'''
		
		argument_handler = ArgumentHandler()
		argument_handler.handle = Mock()
		argument_handler.handle.return_value = [1,1,1,2]
		
		class MockStructure(Structure):
			def generate_build(self, length, width, height, rotation):
				self._add_command(clone(Position(0,0,0),Position(width,height,length),Position(width+1,0,length+1)))
				self._rotate(rotation)
			
			def register_arguments(self):
				return [
					Argument("Length", "The length of the structure"),
					Argument("Width", "The width of the structure"),
					Argument("Height", "The height of the structure"),
					Argument("Rotation", "The rotation of the structure"),
				]
		commands = generate(MockStructure(),argument_handler)
		self.assertEqual(commands, ["clone ~-1 ~0 ~-1 ~0 ~1 ~0 ~-3 ~0 ~-3"])
		
	def test_generate_clone_with_rotate_270(self):
		'''This clone selects a quad from 0,0,0 to 1,1,1 and clones it to 2,0,2
		This whole selection is then rotated 270* clockwise.
		The positions in the clone command is going to change when rotating 
		to ensure the first position is always lower on the x-z coords than the second position.
		This test ensures this rule is respected.'''
		
		argument_handler = ArgumentHandler()
		argument_handler.handle = Mock()
		argument_handler.handle.return_value = [1,1,1,3]
		
		class MockStructure(Structure):
			def generate_build(self, length, width, height, rotation):
				self._add_command(clone(Position(0,0,0),Position(width,height,length),Position(width+1,0,length+1)))
				self._rotate(rotation)
			
			def register_arguments(self):
				return [
					Argument("Length", "The length of the structure"),
					Argument("Width", "The width of the structure"),
					Argument("Height", "The height of the structure"),
					Argument("Rotation", "The rotation of the structure"),
				]
		commands = generate(MockStructure(),argument_handler)
		self.assertEqual(commands, ["clone ~0 ~0 ~-1 ~1 ~1 ~0 ~2 ~0 ~-3"])
		
	def test_generate_fill(self):
		argument_handler = ArgumentHandler()
		argument_handler.handle = Mock()
		argument_handler.handle.return_value = [23,17,99]
		
		class MockStructure(Structure):
			def generate_build(self, length, width, height):
				self._add_command(fill(Position(0,0,0),Position(width,height,length),base_block()))
			
			def register_arguments(self):
				return [
					Argument("Length", "The length of the structure"),
					Argument("Width", "The width of the structure"),
					Argument("Height", "The height of the structure"),
				]
		commands = generate(MockStructure(),argument_handler)
		self.assertEqual(commands, ["fill ~0 ~0 ~0 ~17 ~99 ~23 minecraft:iron_block"])
		
		
	def test_generate_fill_with_rotate_90(self):
		'''This fill selects a quad from 0,0,0 to 1,1,1
		This whole selection is then rotated 90* clockwise.
		The positions in the fill command are going to change when rotating 
		to ensure the first position is always lower on the x-z coords than the second position.
		This test ensures this rule is respected.'''
		argument_handler = ArgumentHandler()
		argument_handler.handle = Mock()
		argument_handler.handle.return_value = [1,1,1,1]
		
		class MockStructure(Structure):
			def generate_build(self, length, width, height, rotation):
				self._add_command(fill(Position(0,0,0),Position(width,height,length),base_block()))
				self._rotate(rotation)
			
			def register_arguments(self):
				return [
					Argument("Length", "The length of the structure"),
					Argument("Width", "The width of the structure"),
					Argument("Height", "The height of the structure"),
					Argument("Rotation", "The rotation of the structure"),
				]
		commands = generate(MockStructure(),argument_handler)
		self.assertEqual(commands, ["fill ~-1 ~0 ~0 ~0 ~1 ~1 minecraft:iron_block"])
		
	def test_generate_fill_with_rotate_180(self):
		'''This fill selects a quad from 0,0,0 to 1,1,1
		This whole selection is then rotated 180* clockwise.
		The positions in the fill command are going to change when rotating 
		to ensure the first position is always lower on the x-z coords than the second position.
		This test ensures this rule is respected.'''
		argument_handler = ArgumentHandler()
		argument_handler.handle = Mock()
		argument_handler.handle.return_value = [1,1,1,2]
		
		class MockStructure(Structure):
			def generate_build(self, length, width, height, rotation):
				self._add_command(fill(Position(0,0,0),Position(width,height,length),base_block()))
				self._rotate(rotation)
			
			def register_arguments(self):
				return [
					Argument("Length", "The length of the structure"),
					Argument("Width", "The width of the structure"),
					Argument("Height", "The height of the structure"),
					Argument("Rotation", "The rotation of the structure"),
				]
		commands = generate(MockStructure(),argument_handler)
		self.assertEqual(commands, ["fill ~-1 ~0 ~-1 ~0 ~1 ~0 minecraft:iron_block"])
		
	def test_generate_fill_with_rotate_270(self):
		'''This fill selects a quad from 0,0,0 to 1,1,1
		This whole selection is then rotated 270* clockwise.
		The positions in the fill command are going to change when rotating 
		to ensure the first position is always lower on the x-z coords than the second position.
		This test ensures this rule is respected.'''
		argument_handler = ArgumentHandler()
		argument_handler.handle = Mock()
		argument_handler.handle.return_value = [1,1,1,3]
		
		class MockStructure(Structure):
			def generate_build(self, length, width, height, rotation):
				self._add_command(fill(Position(0,0,0),Position(width,height,length),base_block()))
				self._rotate(rotation)
			
			def register_arguments(self):
				return [
					Argument("Length", "The length of the structure"),
					Argument("Width", "The width of the structure"),
					Argument("Height", "The height of the structure"),
					Argument("Rotation", "The rotation of the structure"),
				]
		commands = generate(MockStructure(),argument_handler)
		self.assertEqual(commands, ["fill ~0 ~0 ~-1 ~1 ~1 ~0 minecraft:iron_block"])
		
	def test_setblock_with_base_block(self):
		argument_handler = ArgumentHandler()
		argument_handler.handle = Mock()
		argument_handler.handle.return_value = [23,17,77]
		
		class MockStructure(Structure):
			def generate_build(self, pos_x, pos_y, pos_z):
				self._add_command(setblock(Position(pos_x,pos_y,pos_z),base_block()))
			
			def register_arguments(self):
				return [
					Argument("PosX", "The X position of the block"),
					Argument("PosY", "The Y position of the block"),
					Argument("PosZ", "The Z position of the block"),
				]
		commands = generate(MockStructure(),argument_handler)
		self.assertEqual(commands, ["setblock ~23 ~17 ~77 minecraft:iron_block"])
		
	def test_setblock_with_base_block_and_rotate_90(self):
		argument_handler = ArgumentHandler()
		argument_handler.handle = Mock()
		argument_handler.handle.return_value = [23,17,77,1]
		
		class MockStructure(Structure):
			def generate_build(self, pos_x, pos_y, pos_z, rotation):
				self._add_command(setblock(Position(pos_x,pos_y,pos_z),base_block()))
				self._rotate(rotation)
			
			def register_arguments(self):
				return [
					Argument("PosX", "The X position of the block"),
					Argument("PosY", "The Y position of the block"),
					Argument("PosZ", "The Z position of the block"),
					Argument("Rotation", ""),
				]
		commands = generate(MockStructure(),argument_handler)
		self.assertEqual(commands, ["setblock ~-77 ~17 ~23 minecraft:iron_block"])
		
	def test_setblock_with_base_block_and_rotate_180(self):
		argument_handler = ArgumentHandler()
		argument_handler.handle = Mock()
		argument_handler.handle.return_value = [23,17,77,2]
		
		class MockStructure(Structure):
			def generate_build(self, pos_x, pos_y, pos_z, rotation):
				self._add_command(setblock(Position(pos_x,pos_y,pos_z),base_block()))
				self._rotate(rotation)
			
			def register_arguments(self):
				return [
					Argument("PosX", "The X position of the block"),
					Argument("PosY", "The Y position of the block"),
					Argument("PosZ", "The Z position of the block"),
					Argument("Rotation", ""),
				]
		commands = generate(MockStructure(),argument_handler)
		self.assertEqual(commands, ["setblock ~-23 ~17 ~-77 minecraft:iron_block"])
		
	def test_setblock_with_base_block_and_rotate_270(self):
		argument_handler = ArgumentHandler()
		argument_handler.handle = Mock()
		argument_handler.handle.return_value = [23,17,77,3]
		
		class MockStructure(Structure):
			def generate_build(self, pos_x, pos_y, pos_z, rotation):
				self._add_command(setblock(Position(pos_x,pos_y,pos_z),base_block()))
				self._rotate(rotation)
			
			def register_arguments(self):
				return [
					Argument("PosX", "The X position of the block"),
					Argument("PosY", "The Y position of the block"),
					Argument("PosZ", "The Z position of the block"),
					Argument("Rotation", ""),
				]
		commands = generate(MockStructure(),argument_handler)
		self.assertEqual(commands, ["setblock ~77 ~17 ~-23 minecraft:iron_block"])
		
	def test_setblock_with_redstone_dust(self):
		argument_handler = ArgumentHandler()
		argument_handler.handle = Mock()
		argument_handler.handle.return_value = [23,17,77]
		
		class MockStructure(Structure):
			def generate_build(self, pos_x, pos_y, pos_z):
				self._add_command(setblock(Position(pos_x,pos_y,pos_z),redstone_dust()))
			
			def register_arguments(self):
				return [
					Argument("PosX", "The X position of the block"),
					Argument("PosY", "The Y position of the block"),
					Argument("PosZ", "The Z position of the block"),
				]
		commands = generate(MockStructure(),argument_handler)
		self.assertEqual(commands, ["setblock ~23 ~17 ~77 minecraft:redstone_wire"])
		
	def test_setblock_with_redstone_torch(self):
		'''assuming the player is facing east (+x), placing a torch on the wall in front of them will cause it to point west (-x)'''
		argument_handler = ArgumentHandler()
		argument_handler.handle = Mock()
		argument_handler.handle.return_value = [23,17,77]
		
		class MockStructure(Structure):
			def generate_build(self, pos_x, pos_y, pos_z):
				self._add_command(setblock(Position(pos_x,pos_y,pos_z),redstone_torch('-x')))
			
			def register_arguments(self):
				return [
					Argument("PosX", "The X position of the block"),
					Argument("PosY", "The Y position of the block"),
					Argument("PosZ", "The Z position of the block"),
				]
		commands = generate(MockStructure(),argument_handler)
		self.assertEqual(commands, ["setblock ~23 ~17 ~77 minecraft:redstone_wall_torch[facing=west]"])
		
	def test_setblock_with_redstone_torch_and_rotate_90(self):
		'''assuming the player is facing east (+x), placing a torch on the wall in front of them will cause it to point west (-x)'''
		argument_handler = ArgumentHandler()
		argument_handler.handle = Mock()
		argument_handler.handle.return_value = [0,0,0,1]
		
		class MockStructure(Structure):
			def generate_build(self, pos_x, pos_y, pos_z, rotation):
				self._add_command(setblock(Position(pos_x,pos_y,pos_z),redstone_torch('-x')))
				self._rotate(rotation)
			
			def register_arguments(self):
				return [
					Argument("PosX", "The X position of the block"),
					Argument("PosY", "The Y position of the block"),
					Argument("PosZ", "The Z position of the block"),
					Argument("Rotation", ""),
				]
		commands = generate(MockStructure(),argument_handler)
		self.assertEqual(commands, ["setblock ~0 ~0 ~0 minecraft:redstone_wall_torch[facing=north]"])
		
	def test_setblock_with_redstone_torch_and_rotate_180(self):
		'''assuming the player is facing east (+x), placing a torch on the wall in front of them will cause it to point west (-x)'''
		argument_handler = ArgumentHandler()
		argument_handler.handle = Mock()
		argument_handler.handle.return_value = [0,0,0,2]
		
		class MockStructure(Structure):
			def generate_build(self, pos_x, pos_y, pos_z, rotation):
				self._add_command(setblock(Position(pos_x,pos_y,pos_z),redstone_torch('-x')))
				self._rotate(rotation)
			
			def register_arguments(self):
				return [
					Argument("PosX", "The X position of the block"),
					Argument("PosY", "The Y position of the block"),
					Argument("PosZ", "The Z position of the block"),
					Argument("Rotation", ""),
				]
		commands = generate(MockStructure(),argument_handler)
		self.assertEqual(commands, ["setblock ~0 ~0 ~0 minecraft:redstone_wall_torch[facing=east]"])
		
	def test_setblock_with_redstone_torch_and_rotate_270(self):
		'''assuming the player is facing east (+x), placing a torch on the wall in front of them will cause it to point west (-x)'''
		argument_handler = ArgumentHandler()
		argument_handler.handle = Mock()
		argument_handler.handle.return_value = [0,0,0,3]
		
		class MockStructure(Structure):
			def generate_build(self, pos_x, pos_y, pos_z, rotation):
				self._add_command(setblock(Position(pos_x,pos_y,pos_z),redstone_torch('-x')))
				self._rotate(rotation)
			
			def register_arguments(self):
				return [
					Argument("PosX", "The X position of the block"),
					Argument("PosY", "The Y position of the block"),
					Argument("PosZ", "The Z position of the block"),
					Argument("Rotation", ""),
				]
		commands = generate(MockStructure(),argument_handler)
		self.assertEqual(commands, ["setblock ~0 ~0 ~0 minecraft:redstone_wall_torch[facing=south]"])
		
	def test_setblock_with_repeater(self):
		'''assuming the player is facing east (+x), placing a repeater on the ground in front of them will cause its output to point east (+x) and its input to point west (-x)'''
		argument_handler = ArgumentHandler()
		argument_handler.handle = Mock()
		argument_handler.handle.return_value = [23,17,77]
		
		class MockStructure(Structure):
			def generate_build(self, pos_x, pos_y, pos_z):
				self._add_command(setblock(Position(pos_x,pos_y,pos_z),repeater('+x')))
			
			def register_arguments(self):
				return [
					Argument("PosX", "The X position of the block"),
					Argument("PosY", "The Y position of the block"),
					Argument("PosZ", "The Z position of the block"),
				]
		commands = generate(MockStructure(),argument_handler)
		self.assertEqual(commands, ["setblock ~23 ~17 ~77 minecraft:repeater[facing=west]"])
		
	def test_setblock_with_repeater_and_rotate_90(self):
		'''assuming the player is facing east (+x), placing a repeater on the ground in front of them will cause its output to point east (+x) and its input to point west (-x)'''
		argument_handler = ArgumentHandler()
		argument_handler.handle = Mock()
		argument_handler.handle.return_value = [0,0,0,1]
		
		class MockStructure(Structure):
			def generate_build(self, pos_x, pos_y, pos_z, rotation):
				self._add_command(setblock(Position(pos_x,pos_y,pos_z),repeater('+x')))
				self._rotate(rotation)
			
			def register_arguments(self):
				return [
					Argument("PosX", "The X position of the block"),
					Argument("PosY", "The Y position of the block"),
					Argument("PosZ", "The Z position of the block"),
					Argument("Rotation", ""),
				]
		commands = generate(MockStructure(),argument_handler)
		self.assertEqual(commands, ["setblock ~0 ~0 ~0 minecraft:repeater[facing=north]"])
		
	def test_setblock_with_repeater_and_rotate_180(self):
		'''assuming the player is facing east (+x), placing a repeater on the ground in front of them will cause its output to point east (+x) and its input to point west (-x)'''
		argument_handler = ArgumentHandler()
		argument_handler.handle = Mock()
		argument_handler.handle.return_value = [0,0,0,2]
		
		class MockStructure(Structure):
			def generate_build(self, pos_x, pos_y, pos_z, rotation):
				self._add_command(setblock(Position(pos_x,pos_y,pos_z),repeater('+x')))
				self._rotate(rotation)
			
			def register_arguments(self):
				return [
					Argument("PosX", "The X position of the block"),
					Argument("PosY", "The Y position of the block"),
					Argument("PosZ", "The Z position of the block"),
					Argument("Rotation", ""),
				]
		commands = generate(MockStructure(),argument_handler)
		self.assertEqual(commands, ["setblock ~0 ~0 ~0 minecraft:repeater[facing=east]"])
		
	def test_setblock_with_repeater_and_rotate_270(self):
		'''assuming the player is facing east (+x), placing a repeater on the ground in front of them will cause its output to point east (+x) and its input to point west (-x)'''
		argument_handler = ArgumentHandler()
		argument_handler.handle = Mock()
		argument_handler.handle.return_value = [0,0,0,3]
		
		class MockStructure(Structure):
			def generate_build(self, pos_x, pos_y, pos_z, rotation):
				self._add_command(setblock(Position(pos_x,pos_y,pos_z),repeater('+x')))
				self._rotate(rotation)
			
			def register_arguments(self):
				return [
					Argument("PosX", "The X position of the block"),
					Argument("PosY", "The Y position of the block"),
					Argument("PosZ", "The Z position of the block"),
					Argument("Rotation", ""),
				]
		commands = generate(MockStructure(),argument_handler)
		self.assertEqual(commands, ["setblock ~0 ~0 ~0 minecraft:repeater[facing=south]"])
		
	def test_clone_and_translate(self):
		argument_handler = ArgumentHandler()
		argument_handler.handle = Mock()
		argument_handler.handle.return_value = [10,18,15]
		
		class MockStructure(Structure):
			def generate_build(self, pos_x, pos_y, pos_z):
				self._add_command(clone(Position(0,0,0),Position(1,1,1),Position(2,0,2)))
				self._translate(pos_x,pos_y,pos_z)
			
			def register_arguments(self):
				return [
					Argument("PosX", "The X position of the block"),
					Argument("PosY", "The Y position of the block"),
					Argument("PosZ", "The Z position of the block"),
					Argument("Rotation", ""),
				]
		commands = generate(MockStructure(),argument_handler)
		self.assertEqual(commands, ["clone ~10 ~18 ~15 ~11 ~19 ~16 ~12 ~18 ~17"])
	
	def test_fill_withbase_block_and_translate(self):
		argument_handler = ArgumentHandler()
		argument_handler.handle = Mock()
		argument_handler.handle.return_value = [10,18,15]
		
		class MockStructure(Structure):
			def generate_build(self, pos_x, pos_y, pos_z):
				self._add_command(fill(Position(0,0,0),Position(1,1,1),base_block()))
				self._translate(pos_x,pos_y,pos_z)
			
			def register_arguments(self):
				return [
					Argument("PosX", "The X position of the block"),
					Argument("PosY", "The Y position of the block"),
					Argument("PosZ", "The Z position of the block"),
					Argument("Rotation", ""),
				]
		commands = generate(MockStructure(),argument_handler)
		self.assertEqual(commands, ["fill ~10 ~18 ~15 ~11 ~19 ~16 minecraft:iron_block"])
		
	def test_setblock_with_base_block_and_translate(self):
		argument_handler = ArgumentHandler()
		argument_handler.handle = Mock()
		argument_handler.handle.return_value = [10,18,15]
		
		class MockStructure(Structure):
			def generate_build(self, pos_x, pos_y, pos_z):
				self._add_command(setblock(Position(0,0,0),base_block()))
				self._translate(pos_x,pos_y,pos_z)
			
			def register_arguments(self):
				return [
					Argument("PosX", "The X position of the block"),
					Argument("PosY", "The Y position of the block"),
					Argument("PosZ", "The Z position of the block"),
					Argument("Rotation", ""),
				]
		commands = generate(MockStructure(),argument_handler)
		self.assertEqual(commands, ["setblock ~10 ~18 ~15 minecraft:iron_block"])
		
	def test_multi_command_structure(self):
		argument_handler = ArgumentHandler()
		argument_handler.handle = Mock()
		argument_handler.handle.return_value = []
		
		class MockStructure(Structure):
			def generate_build(self,):
				self._add_command(clone(Position(0,0,0),Position(1,1,1),Position(2,0,2)))
				self._add_command(clone(Position(0,0,0),Position(1,1,1),Position(2,0,2)))
				self._add_command(clone(Position(0,0,0),Position(1,1,1),Position(2,0,2)))
				self._add_command(clone(Position(0,0,0),Position(1,1,1),Position(2,0,2)))
				self._add_command(clone(Position(0,0,0),Position(1,1,1),Position(2,0,2)))
				self._add_command(clone(Position(0,0,0),Position(1,1,1),Position(2,0,2)))
			
			def register_arguments(self):
				return []
			
		commands = generate(MockStructure(),argument_handler)
		self.assertEqual(len(commands), 6)
		
	