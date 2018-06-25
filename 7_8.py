sandwich_orders = ['berry','apple','pastrami','watermelon','pastrami']
finished_sandwiches = []
print('The pastrami has sold clean.\n')

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	current_process = sandwich_orders.pop()
	print('Verifying sandwich: ' + current_process.title())
	finished_sandwiches.append(current_process)
	
print("\nThe following : ")
for sandwich in finished_sandwiches:
	print(sandwich.title())
