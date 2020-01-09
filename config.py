import json#for manipulating json files
from sys import platform
class config():
	
	def create_config():#create the config file
		cfg='{"configType": "Portal 2 Modding Tools Config File","toolsVersion": "0","lastVersion": "false", "modGithubRepoUrl" = ""}'
		with open('config.cfg', 'w', encoding="utf-8") as file:
			json.dump(json.loads(cfg), file, indent=3)
	
	def load(section):#load a config
		r"""
		loads a section of the config (json-formatted) and return the data.
		raise an exception if the config or the requested section doesn't exist
		example::
			>>> import config
			>>> print(config.load("version"))
			'2.6'
		"""
		try:
			with open('config.cfg', 'r', encoding="utf-8") as file:
				cfg = json.load(file)#iload the config
				readedata = cfg[section]# take the requested field
			return readedata #return the readed data
		except:
			raise configLoadError
	
	def save(data, section):#save a config
		r"""
		save the data on the config (json-formatted), re-create the config if no one is found.
		example::
			>>> import config
			>>> print(config.load("version"))
			'2.6'
			>>> config.save("2.5","version")
			>>> print(config.load("version"))
			'2.5'
		"""
		try:
			with open('config.cfg', 'r', encoding="utf-8") as file:
				cfg = json.load(file)# load the config file
				cfg[section]=data
			with open('config.cfg', 'w', encoding="utf-8") as file:
				json.dump(cfg, file, indent=3)
		except:
			raise configError
	
	def check(arg = None):
		r"""
		if no aurgment is present check if the config file exist and if is a good config file, else will
		check if the given section exists.
		"""
		try:
			with open('config.cfg', 'r') as file:
				pass
		except:
			raise configDoesntExist
		if arg == None:# check the aurgment is present
			try:
				with open('config.cfg', 'r') as file:# try to open the config file
					cfg = json.load(file)  # load the config file
					if cfg['config_type'] == "Portal 2 Modding Tools Config File":
						return True # the check is made successfully
					else:
						raise configError # the config file is not a BM config file
			except:
				raise configDoesntExist # the config file doesn't exist
		else:
			try:
				with open("config.cfg", 'r') as file:  # try to open the config file
					cfg = json.load(file) # load the config file
					if cfg[arg]:
						return True
					else:
						return False
			except:
				raise configDoesntExist # the config file doesn't exist

class static:
    @property
    def name():
        return "Portal 2 Modding Tools"
    @property
    def version():
        return config.load("toolsVersion")


class configError(BaseException):
	r"""
	base error for config operations
	"""
	pass
class configLoadError(BaseException):
	r"""
	There's no config with that ID!
	"""
	pass
class configDoesntExist(BaseException):
	r"""
	The config file doesn't exist!
	"""
	pass