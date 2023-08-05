"""
Facade Method is a Structural Design pattern that provides a simpler unified interface to a more complex system. 
The word Facade means the face of a building or particularly an outer lying interface of a complex system, consists of several sub-systems. 
It is an essential part Gang of Four design patterns. 
It provides an easier way to access methods of the underlying systems by providing a single entry point
"""

"""
Imagine we have a washing machine which can wash the clothes, rinse the clothes and spin the clothes but all the tasks separately. 
As the whole system is quite complex, we need to abstract the complexities of the subsystems. 
We need a system that can automate the whole task without the disturbance or interference of us. 
"""

"""Facade pattern with an example of WashingMachine"""

class Washing:
	'''Subsystem # 1'''

	def wash(self):
		print("Washing...")


class Rinsing:
	'''Subsystem # 2'''

	def rinse(self):
		print("Rinsing...")


class Spinning:
	'''Subsystem # 3'''

	def spin(self):
		print("Spinning...")


class WashingMachine:
	'''Facade'''

	def __init__(self):
		self.washing = Washing()
		self.rinsing = Rinsing()
		self.spinning = Spinning()

	def startWashing(self):
		self.washing.wash()
		self.rinsing.rinse()
		self.spinning.spin()

""" main method """
if __name__ == "__main__":

	washingMachine = WashingMachine()
	washingMachine.startWashing()
