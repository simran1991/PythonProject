from Animal import Animal
class Dog(Animal):
	
	def __init__(self,name,species,hobby):
		super().__init__(name,species)
		self.hobby=hobby

	
	def Move(self):
		print(self.name+" is moving")