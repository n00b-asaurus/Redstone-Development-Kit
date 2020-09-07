from minecraft_environment.command import Command
import logging

log = logging.getLogger()

class Clone(Command):
	def __init__(self, pos1, pos2, pos3):
		self.pos1 = pos1
		self.pos2 = pos2
		self.pos3 = pos3
		self.__calculate_difference()
		
	def __calculate_difference(self):
		self.delta_x = abs(self.pos1.x - self.pos2.x)
		self.delta_z = abs(self.pos1.z - self.pos2.z)
		log.debug("Clone dx:{} dz{}".format(self.delta_x, self.delta_z))
		
	def get_string(self):
		return "clone {} {} {}".format(self.pos1, self.pos2, self.pos3)
		
	def translate(self, x, y, z):
		log.debug("Clone translating positions x{} y{} z{}".format( x, y, z))
		log.debug("Clone initial positions: {} {} {}".format(self.pos1, self.pos2, self.pos3))
		self.pos1.translate(x,y,z)
		self.pos2.translate(x,y,z)
		self.pos3.translate(x,y,z)
		log.debug("Clone positions after translation: {} {} {}".format(self.pos1, self.pos2, self.pos3))
			
		
	def rotate(self, amount):
		log.debug("Clone rotating positions {} quarter turns clockwise".format(amount))
		log.debug("Clone initial positions: {} {} {}".format(self.pos1, self.pos2, self.pos3))
		self.pos1.rotate(amount)
		self.pos2.rotate(amount)
		self.pos3.rotate(amount)
		self.__calculate_difference()
		log.debug("Clone positions after rotations: {} {} {}".format(self.pos1, self.pos2, self.pos3))
		if self.pos1.x > self.pos2.x and self.pos1.z > self.pos2.z:
			log.debug("Clone pos1 and pos2 point left-down - adjusting")
			log.debug("Clone dx:{} dz{}".format(self.delta_x, self.delta_z))
			self.pos1.translate(-self.delta_x, 0, -self.delta_z)
			self.pos2.translate( self.delta_x, 0,  self.delta_z)
			self.pos3.translate(-self.delta_x, 0, -self.delta_z)
			log.debug("Clone positions after adjustments: {} {} {}".format(self.pos1, self.pos2, self.pos3))
		elif self.pos1.x > self.pos2.x and self.pos1.z <= self.pos2.z:
			log.debug("Clone pos1 and pos2 point right-down - adjusting")
			log.debug("Clone dx:{} dz{}".format(self.delta_x, self.delta_z))
			self.pos1.translate(-self.delta_x, 0, 0)
			self.pos2.translate( self.delta_x, 0, 0)
			self.pos3.translate(-self.delta_x, 0, 0)
			log.debug("Clone positions after adjustments: {} {} {}".format(self.pos1, self.pos2, self.pos3))
		elif self.pos1.x <= self.pos2.x and self.pos1.z > self.pos2.z:
			log.debug("Clone pos1 and pos2 point left-up - adjusting")
			log.debug("Clone dx:{} dz{}".format(self.delta_x, self.delta_z))
			self.pos1.translate(0, 0, -self.delta_z)
			self.pos2.translate(0, 0,  self.delta_z)
			self.pos3.translate(0, 0, -self.delta_z)
			log.debug("Clone positions after adjustments: {} {} {}".format(self.pos1, self.pos2, self.pos3))