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
		
		
restaurant = Restaurant('lambama','mexico')

print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type.title())
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served(10)
restaurant.print_number_served()

restaurant.increment_number_served(6)
restaurant.print_number_served()
