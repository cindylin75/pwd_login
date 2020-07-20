password = 'a123456'
i = 3
while True:
	i = i - 1
	pwd = input('Please insert the password:')
	if pwd == password:
		print('Log in success!')
		break
	else:
		print('The password is wrong.')
		if i > 0:
			print('You have', i ,'chance')
		else:
			print('You have no chance! Please email your protector')
			break
			