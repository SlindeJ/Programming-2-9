
class pizza23:
	def __init__(self, inches):
		self.labor = 0.75
		self.rent = 1
		self.inc = inches
		self.mats = 0
		
	def calcmaterials(self):
		self.mats = 0.05 * (self.inc**2)
		
	def getcost(self):
		return self.labor + self.rent + self.mats
		pass
