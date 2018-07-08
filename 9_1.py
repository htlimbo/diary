class Restaurant():
	"""one simple test"""
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		
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
