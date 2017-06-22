from abc import abstractmethod,ABCMeta
class Animal:
	__metaclass__ = ABCMeta

	message="I am an ANimal class"
	def __init__(self,name,species):
		self.name=name
		self.species=species

	def getName(self):
		return self.name

	def getSpecies(self):
		return self.species
	
	@abstractmethod
	def Move(self):
		pass

	@abstractmethod
	def eat(self):
		pass
	
	#more pythonic way og abstract method
	def sleep(self):
		raise NotImplementedError()
			
	def __str__(self):
		return ("%s is %s" % (self.name,self.species))
