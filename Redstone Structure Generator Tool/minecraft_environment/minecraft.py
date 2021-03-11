mc_version = None

def set_version(version):
	global mc_version
	mc_version = version

def mcfunctions_require_forwardslash():
	return mc_version.mcfunctions_require_forwardslash

def clone(pos1, pos2, pos3):
	return mc_version.clone(pos1, pos2, pos3)
	
def fill(pos1, pos2, block):
	return mc_version.fill(pos1, pos2, block)
	
def setblock(pos, block):
	return mc_version.setblock(pos, block)
	
def base_block():
	return mc_version.base_block()
	
def redstone_dust():
	return mc_version.redstone_dust()
	
def redstone_torch(facing):
	return mc_version.redstone_torch(facing)
	
def repeater(facing):
	return mc_version.repeater(facing)
	
def air():
	return mc_version.air()