import json

def get_stored_number():
	filename = 'likenumber.json'
	try:
		with open(filename) as f_obj:
			likenumber = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return likenumber
		
def get_new_number():
	likenumber = input('Please input your favorite number: ')
	filename = 'likenumber.json'
	with open(filename,'w') as f_obj:
		json.dump(likenumber,f_obj)
	return likenumber
	
def print_number():
	likenumber = get_stored_number()
	if likenumber:
		print("I know your favorite number!It's " + str(likenumber) + '.')
	else:
		likenumber = get_new_number()
		print("We will remember your favorite number!It's " +\
		 str(likenumber) + '.')
		 
		 
print_number()
