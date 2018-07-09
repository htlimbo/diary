from random import randint

class Die():
	def __init__(self,times,sides=6):
		self.times = times
		self.sides = sides
			
	def roll_die(self):
		for time in range(1,self.times+1):
			x = randint(1,self.sides)
			print("The " + str(time) +" random number is: " + str(x) + ".")
		
		

t1 = Die(10,6)
t1.roll_die()
print('\n')
t2 = Die(10,20)
t2.roll_die()
