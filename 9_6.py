class Restaurant():
	"""one simple test"""
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
		
	def set_number_served(self,numbers):
		if numbers >= self.number_served:
			self.number_served = numbers
		else:
			print("You can not roll back numbers.")
					
	def increment_number_served(self,upnumber):
		self.number_served += upnumber
		
	def print_number_served(self):
		print("The number of served people are : " \
		+ str(self.number_served) +'.')
		
	def describe_restaurant(self):
		print("The restaurant name is: " + self.restaurant_name.title() +'.')
		print("The cuisine type is: " + self.cuisine_type.title() + '.')
		
	def open_restaurant(self):
		print("The restaurant is opening.")
		

class IceCreamStand(Restaurant):
	"""one simple test"""
	def __init__(self,restaurant_name,cuisine_type):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors = []
		
	def taste_list(self):
		prompt = "\nPlease input your taste: "
		prompt += "\nEnter 'q' to end.\n"
		
		active = True
		while active:
			message = input(prompt)
			
			if message == 'q' :
				active = False
			else:
				self.flavors.append(message.title())

				
	def print_taste_list(self):
		print(self.flavors)
		
my_icecream = IceCreamStand('luck','newland')

print(my_icecream.restaurant_name.title())
print(my_icecream.cuisine_type.title())
my_icecream.describe_restaurant()
my_icecream.open_restaurant()

my_icecream.set_number_served(10)
my_icecream.print_number_served()
my_icecream.increment_number_served(6)
my_icecream.print_number_served()


my_icecream.taste_list()
my_icecream.print_taste_list()

