def main():

	o = 0
	link = 0
	a = 0	
	with open("./assets/Chat_backup.txt", 'r', encoding = 'utf-8') as f:
		for i in f.readlines():
			if 'omitted' in i:
				print(i)
				o += 1
			elif 'http://' in i:
				print(i)
				link += 1
			else:
				a += 1

	print(f'omitted {o}')
	print(f'links {link}')
	print(f'{a}')


if __name__ == '__main__':
	main()