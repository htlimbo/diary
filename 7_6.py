prompt = 'Please input what kinds of peiliao you want: '
prompt += "\n(Enter 'quit' when you are finished.)"
prompt += "\n"

activeCount = True
while activeCount:
	message = input(prompt)
	if message == 'quit':
		#activeCount = False
		break
	else:
		print('The peiliao include: ' + message)

