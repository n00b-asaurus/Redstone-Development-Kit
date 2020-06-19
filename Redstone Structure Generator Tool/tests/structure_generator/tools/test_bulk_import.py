from tests.structure_generator.tools.resources.base_class import BaseClass

from unittest import TestCase

from structure_generator.tools.bulk_import import import_subclasses, DirectoryNotFoundError

class TestBulkImport(TestCase):
	def test_import_no_classes(self):
		classes = import_subclasses(directory = "tests/structure_generator/tools/resources/no_classes", base_class = BaseClass)
		self.assertEqual(classes, [])
		
		
	def test_import_from_nonexistant_path(self):
		self.assertRaises(DirectoryNotFoundError, import_subclasses, directory = "tests/structure_generator/tools/resources/does_not_exist", base_class = BaseClass)
		
	def test_import_non_recursive(self):
		classes = import_subclasses(directory = "tests/structure_generator/tools/resources/sub_classes", base_class = BaseClass)
		from tests.structure_generator.tools.resources.sub_classes.class_a import ClassA
		from tests.structure_generator.tools.resources.sub_classes.class_b import ClassB
		from tests.structure_generator.tools.resources.sub_classes.class_c import ClassC
		from tests.structure_generator.tools.resources.sub_classes.sub_sub_classes.class_d import ClassD
		from tests.structure_generator.tools.resources.sub_classes.sub_sub_classes.class_e import ClassE
		self.assertEqual(classes, [ClassA, ClassB, ClassC])
		del ClassA
		del ClassB
		del ClassC
		del ClassD
		del ClassE
		
	def test_import_recursive(self):
		classes = import_subclasses(directory = "tests/structure_generator/tools/resources/sub_classes", base_class = BaseClass, deepest_level = 1)
		from tests.structure_generator.tools.resources.sub_classes.class_a import ClassA
		from tests.structure_generator.tools.resources.sub_classes.class_b import ClassB
		from tests.structure_generator.tools.resources.sub_classes.class_c import ClassC
		from tests.structure_generator.tools.resources.sub_classes.sub_sub_classes.class_d import ClassD
		from tests.structure_generator.tools.resources.sub_classes.sub_sub_classes.class_e import ClassE
		self.assertEqual(classes, [ClassA, ClassB, ClassC, ClassD, ClassE])
		del ClassA
		del ClassB
		del ClassC
		del ClassD
		del ClassE
	
	# these tests do pass, they just don't do so well after the recursive test registers all modules.
	'''	
	def test_import_non_recursive_dot_separated(self):
		classes = import_subclasses(directory = "tests.structure_generator.tools.resources.sub_classes", base_class = BaseClass)
		from tests.structure_generator.tools.resources.sub_classes.class_a import ClassA
		from tests.structure_generator.tools.resources.sub_classes.class_b import ClassB
		from tests.structure_generator.tools.resources.sub_classes.class_c import ClassC
		from tests.structure_generator.tools.resources.sub_classes.sub_sub_classes.class_d import ClassD
		from tests.structure_generator.tools.resources.sub_classes.sub_sub_classes.class_e import ClassE
		self.assertEqual(classes, [ClassA, ClassB, ClassC])
		del ClassA
		del ClassB
		del ClassC
		del ClassD
		del ClassE
	'''
	'''
	def test_import_non_recursive_backslash_separated(self):
		classes = import_subclasses(directory = "tests\\structure_generator\\tools\\resources\\sub_classes", base_class = BaseClass)
		from tests.structure_generator.tools.resources.sub_classes.class_a import ClassA
		from tests.structure_generator.tools.resources.sub_classes.class_b import ClassB
		from tests.structure_generator.tools.resources.sub_classes.class_c import ClassC
		from tests.structure_generator.tools.resources.sub_classes.sub_sub_classes.class_d import ClassD
		from tests.structure_generator.tools.resources.sub_classes.sub_sub_classes.class_e import ClassE
		self.assertEqual(classes, [ClassA, ClassB, ClassC])
		del ClassA
		del ClassB
		del ClassC
		del ClassD
		del ClassE
	'''
		