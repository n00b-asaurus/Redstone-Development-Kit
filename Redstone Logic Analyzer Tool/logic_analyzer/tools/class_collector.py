from os.path import dirname, basename, isfile, join
import glob
import importlib

def collect_child_classes(base_class, file_path, instantiate = False, register_method = None, *register_arguments, **register_keyword_arguments):
	discovered_files = glob.glob(join(dirname('.\\'+file_path.replace('.','\\')+'\\'), "*.py"), recursive=True)
	modules = []
	for file in discovered_files:
		if isfile(file) and not file.endswith('__init__.py'):
			module = importlib.import_module(file_path+"."+basename(file)[:-3])
			modules.append(module)
	
	if not instantiate:
		if not register_method:
			return base_class.__subclasses__()
		else:
			class_dict = {}
			for module_class in base_class.__subclasses__():
				key = eval("module_class.{}(*register_arguments, *register_keyword_arguments)".format(register_method))
				class_dict[key] = module_class
			return class_dict
	
	else:
		objects_list = []
		for module_class in base_class.__subclasses__():
			class_object = module_class()
			objects_list.append(class_object)
		if not register_method:
			return objects_list
		else:
			object_dict = {}
			for object in objects_list:
				key = eval("object.{}(*register_arguments, *register_keyword_arguments)".format(register_method))
				object_dict[key] = object
			return object_dict
	