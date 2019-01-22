x = [1, 4, 8, 12]
counter = 0
while counter < len(x):  #0,1,2
		z = (x[counter]) * 3   #[1,4,8,1,4,8,1,4,8]
		print(z)
		for y in x:
			print(y * '*')
		counter += 1
