from os.path import dirname, basename, isfile, join, exists, abspath
import glob
import importlib

def import_subclasses(directory, base_class, deepest_level = 0):
	formated_directory = directory.replace("/","\\").replace(".","\\")
	if exists(formated_directory):
		discovered_files = glob.glob(formated_directory + "\\**", recursive = True)
		
		#import all python files upto the deepest level
		modules = []
		base_depth = len(formated_directory.split("\\"))
		for file in discovered_files:
			if isfile(file) and file.endswith(".py") and not file.endswith('__init__.py') and len(file.split("\\")) <= base_depth + deepest_level + 1:
				modules.append(importlib.import_module(file.replace("\\",".").replace(".py","")))
				
		#collect the ones of type base_class
		return base_class.__subclasses__()
		
	else:
		raise DirectoryNotFoundError("Could not find directory {}".format(formated_directory))
	
class DirectoryNotFoundError(ImportError):
	pass