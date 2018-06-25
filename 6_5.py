famouse_rivers={
	'nile':'egypt',
	'yangzi':'china',
	'amazon':'brazile',
	}
for key,value in famouse_rivers.items():
	print("The "+ key.title() +" runs throuth " + value.title() 
	+ ". ")

print('\n')
for river in famouse_rivers.keys():
	print(river.title())
	
print('\n')
for country in famouse_rivers.values():
	print(country.title())
