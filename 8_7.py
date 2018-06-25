def make_album(singer_name,album_name,songs=''):
	album_info={
		'Singer':singer_name.title(),
		'Album':album_name.title(),
		}
	if songs:
		album_info['Songs_num'] = songs
	return album_info

active = True
while active:
	print('Please tell some mesaages about your favorite album:')
	print("(Enter 'q' at any time to quit)")
	
	f_singer = input('Singer name: ')
	if f_singer == 'q':
		break
	f_album = input('Album name: ')
	if f_album == 'q':
		break
	prompt = "Song's numbers: "
	prompt += "(If you don't know,press the key 'enter')"
	f_songs = input(prompt)
	if f_songs == 'q':
		break
	
	
	album_messages = make_album(f_singer,f_album,f_songs)
	print(album_messages)
		
	
