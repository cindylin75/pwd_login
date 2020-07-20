password = 'a123456'
i = 3
while True:
	pwd = input('Please insert the password:')
	if pwd == password:
		print('Log in success!')
		break
	else:
		i = i - 1
		print('The password is worong. You have', i ,'chance')
		if i == 0:
			break