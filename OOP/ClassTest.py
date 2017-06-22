from Animal import Animal
from Dog import Dog
if __name__=="__main__":
	#polly=Animal("polly","sheep")
	#print("My name is ",polly.getName())
	#print("I am a ",polly.getSpecies())
	#print(polly.message)
	#hello=Animal("hello","String")
	#print(hello)
	#print(hello.message)
	
	jolly=Animal("jolly",Animal)
	sparky=Dog("sparky",Dog,"running")
	
	print(jolly)
	sparky.Move()
	print(sparky)
	
	print(sparky.name +" is instance of Animal "+str(isinstance(sparky,Animal)))
	
	print(sparky.name +" is instance of Dog "+str(isinstance(sparky,Dog)))

	print(sparky.eat())
	#print(sparky.sleep())
	#print(jolly.hobby)