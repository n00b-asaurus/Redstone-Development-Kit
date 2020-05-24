from structure_generator.command import Command
import logging

log = logging.getLogger()

class Fill(Command):
	def __init__(self, pos1, pos2, block):
		self.pos1 = pos1
		self.pos2 = pos2
		self.block = block
		self.__calculate_difference()
		
	def __calculate_difference(self):
		self.delta_x = abs(self.pos1.x - self.pos2.x)
		self.delta_z = abs(self.pos1.z - self.pos2.z)
		log.debug("Fill dx:{} dz{}".format(self.delta_x, self.delta_z))
	
	def get_string(self):
		return "fill {} {} {}".format(self.pos1, self.pos2, self.block)
		
	def translate(self, x, y, z):
		self.pos1.translate(x,y,z)
		self.pos2.translate(x,y,z)
		
	def rotate(self, amount):
		log.debug("Fill rotating positions {} quarter turns clockwise".format(amount))
		log.debug("Fill initial positions: {} {}".format(self.pos1, self.pos2))
		self.pos1.rotate(amount)
		self.pos2.rotate(amount)
		self.block.rotate(amount)
		self.__calculate_difference()
		log.debug("Fill positions after rotations: {} {}".format(self.pos1, self.pos2))
		if self.pos1.x > self.pos2.x and self.pos1.z > self.pos2.z:
			log.debug("Fill pos1 and pos2 point left-down - adjusting")
			log.debug("Fill dx:{} dz{}".format(self.delta_x, self.delta_z))
			self.pos1.translate(-self.delta_x, 0, -self.delta_z)
			self.pos2.translate( self.delta_x, 0,  self.delta_z)
			log.debug("Fill positions after adjustments: {} {}".format(self.pos1, self.pos2))
		elif self.pos1.x > self.pos2.x and self.pos1.z <= self.pos2.z:
			log.debug("Fill pos1 and pos2 point right-down - adjusting")
			log.debug("Fill dx:{} dz{}".format(self.delta_x, self.delta_z))
			self.pos1.translate(-self.delta_x, 0, 0)
			self.pos2.translate( self.delta_x, 0, 0)
			log.debug("Fill positions after adjustments: {} {}".format(self.pos1, self.pos2))
		elif self.pos1.x <= self.pos2.x and self.pos1.z > self.pos2.z:
			log.debug("Fill pos1 and pos2 point left-up - adjusting")
			log.debug("Fill dx:{} dz{}".format(self.delta_x, self.delta_z))
			self.pos1.translate(0, 0, -self.delta_z)
			self.pos2.translate(0, 0,  self.delta_z)
			log.debug("Fill positions after adjustments: {} {}".format(self.pos1, self.pos2))