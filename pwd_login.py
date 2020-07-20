password = 'a123456'
i = 3 
while True:
    pwd = input('please insert your password:')
    if pwd == password:
	    print('log in success!')
        break # leave the loop
else:
	i = i - 1
	print('the password is worng, you have', i ,' chance')
