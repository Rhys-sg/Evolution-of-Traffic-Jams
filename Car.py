
import numpy as np

class Car:
	def __init__(self, pos=0):
		self.length = 2					#length of each car
		self.minDistance = 1		#desired minimum distance between cars
		self.reactionTime = 0.9		#all drivers have constant reaction time
		self.maxVelocity = 17		
		self.maxAcceleration = 2		#all cars have max acceleration of 2
		self.maxBrakeAcceleration = 5		#speed at which cars brake
		self.position = pos		#curent position of this car
		self.velocity = 0.1		#current speed of this car
		self.acceleration = 0


	def update(self, lead, dt):
		"""Updates the position, velocity, and acceleration of this car, given the car in front of it"""

		#if position of lead car is less than current car, add 100 to lead position
		leadPosition = lead.position
		if leadPosition < self.position:
				leadPosition += 100

		#update pos and vel
		if self.velocity + self.acceleration * dt < 0:
			#do not let velocity become negative, just set it to 0, move position back
			self.position -= 1 / 2 * self.velocity * self.velocity / self.acceleration
			self.velocity = 0
		else:
			#update velocity and position based on acceleration
			self.velocity += self.acceleration * dt
			self.position += self.velocity * dt + self.acceleration * dt * dt / 2

		#update acceleration
		alpha = 0
		if lead:
			d_position = leadPosition - self.position - lead.length #distance between 2 cars
			d_velocity = self.velocity - lead.velocity #difference in speed of 2 cars
			alpha = (self.minDistance + max(0, self.reactionTime * self.velocity + d_velocity * self.velocity / (2 * np.sqrt(self.maxAcceleration * self.maxBrakeAcceleration)))) / d_position
		
		self.acceleration = self.maxAcceleration * (1 - (self.velocity / self.maxVelocity)**4 - alpha**2)

		if self.position > 100:
			self.position -= 100
