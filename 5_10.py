current_users=['admin','zhang','bao','xiao','guo']
new_users=['Zhang','li','wang','Xiao','wu']

for user_name in new_users:
	if user_name.lower() in current_users:
		print('The name ' + user_name +' has been used.')
	else:
		print('You can use the name.')
