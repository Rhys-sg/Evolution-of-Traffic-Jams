from Car import Car
import math

class Simulation:
	def __init__(self, numCars=0):
		self.dt = 1 / 60
		self.cars = self.createCars(numCars)

	def createCars(self, n):
		"""Creates n cars equidistant apart"""
		if n > 0: space = round(100 // n)
		return [Car(pos) for pos in range(0, 101 - space, space)] if n > 0 else []

	def createCar(self, pos):
		"""Creates a single car at given position on road"""
		c = Car(pos)
		self.cars.append(c)
		#cars array must stay sorted by position of each car
		self.sortCars()
		return c


	def sortCars(self):
		"""Sort cars in the array by their position in ascending order"""
		self.cars.sort(key=lambda c: c.position)

	def update(self):
		#update position, velocity, and acceleration of each car based on car in front of it.
		#for each car i, the lead car is car i + 1, the one directly in front

		self.sortCars()

		#update all but last car
		for i in range(len(self.cars) - 1):
			lead = self.cars[i + 1]
			self.cars[i].update(lead, self.dt)
		
		#update last car using first car in list as lead
		lead = self.cars[0]
		self.cars[-1].update(lead, self.dt)





	def getCarPositions(self):
		return [c.position for c in self.cars]

	def getCarSpeeds(self):
		return [c.velocity for c in self.cars]

	def getCars(self):
		return self.cars