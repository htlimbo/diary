cities={
	'shanghai':{
		'country':'china',
		'population':'100w',
		'fact':'beside the sea',
		},
	'new york':{
		'country':'america',
		'population':'80w',
		'fact':'famouse',
		},
	}

for city,city_info in cities.items():
	print('\nCity: ' + city.title())
	print('Country: ' + city_info['country'].title())
	print('Population: ' + city_info['population'].title())
	print('Fact: ' + city_info['fact'].title())
