dict_one={}
prompt = 'If you could visit one place in the world,where would you go?'
place_active = True

while place_active:
	name = input('Please input your name: ')
	location = input(prompt)
	
	dict_one[name] = location
	
	repeat = input('Would you like to another location?(yes/no)')
	if repeat == 'no':
		place_active = False
		
print('\n---Results:---\n')
for name,location in dict_one.items():
	print(name.title() + ' wants to go to ' + location.title() + '.')
	
