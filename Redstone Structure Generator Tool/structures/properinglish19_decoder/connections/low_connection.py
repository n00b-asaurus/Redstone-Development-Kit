from structures.properinglish19_decoder.connection import Connection
from structures.properinglish19_decoder.build_handlers.single_nc import SingleNC
from structures.properinglish19_decoder.build_handlers.single_off import SingleOff
from structures.properinglish19_decoder.build_handlers.right_double_off import RightDoubleOff
from structures.properinglish19_decoder.build_handlers.left_double_off import LeftDoubleOff


class LowConnection(Connection):	
	def __init__(self, x, z):
		self.x = x
		self.z = z
		self.build_handler = SingleOff()
		
	def type(self):
		return "low connection with {}".format(self.build_handler.type())
		
	def solve(self, right, downline, right_line):
		if downline != None and type(self.build_handler) == SingleOff and type(downline) == LowConnection and type(downline.build_handler) == SingleOff:
			if right:
				self.build_handler = SingleNC()
				downline.build_handler = RightDoubleOff()
			else:
				if not(type(right_line) == LowConnection and type(right_line.build_handler) == SingleNC):
					self.build_handler = SingleNC()
					downline.build_handler = LeftDoubleOff()