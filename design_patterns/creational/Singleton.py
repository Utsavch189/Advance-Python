"""
What is Singleton Method in Python
Singleton Method is a type of Creational Design pattern and is one of the simplest design patterns00 available to us. It is a way to provide one and only one object of a particular type. It involves only one class to create methods and specify the objects. 
Singleton Design Pattern can be understood by a very simple example of Database connectivity. When each object creates a unique Database Connection to the Database, it will highly affect the cost and expenses of the project. So, it is always better to make a single connection rather than making extra irrelevant connections which can be easily done by Singleton Design Pattern.

"""

"""
Monostate/Borg Singleton Design pattern
Singleton behavior can be implemented by Borg’s pattern but instead of having only one instance of the class, there are multiple instances that share the same state. Here we don’t focus on the sharing of the instance identity instead we focus on the sharing state. 
"""


# Singleton Borg pattern
class Borg:

	# state shared by each instance
	__shared_state = dict()

	# constructor method
	def __init__(self):

		self.__dict__ = self.__shared_state
		self.state = 'Utsav'

	def __str__(self):

		return self.state


# main method
if __name__ == "__main__":

	person1 = Borg() # object of class Borg
	person2 = Borg() # object of class Borg
	person3 = Borg() # object of class Borg
	
	print(person3)

	person1.state = 'A' # person1 changed the state
	person2.state = 'B'	 # person2 changed the state

	print(person1) # output --> Algorithms
	print(person2) # output --> Algorithms

	person3.state = 'Supu' # person3 changed the
	# the shared state

	print(person1) # output --> Geeks
	print(person2) # output --> Geeks
	print(person3) # output --> Geeks



"""
Creating a singleton in Python
In the classic implementation of the Singleton Design pattern, we simply use the static method for creating the getInstance method which has the ability to return the shared resource. We also make use of the so-called Virtual private Constructor to raise the exception against it although it is not much required.
"""

# classic implementation of Singleton Design pattern
class Singleton:

	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(Singleton, cls).__new__(cls)
		return cls.instance


# main method
if __name__ == "__main__":

	# create object of Singleton Class
	obj = Singleton()
	print(obj)

	obj2=Singleton()
	print(obj2)




