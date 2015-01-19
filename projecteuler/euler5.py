k = 0
x = 20
keepGoing = True
while (keepGoing):
	for j in range(1,20):
		if (x % j != 0):
			break
		elif (j == 19):
			print x
			keepGoing= False

	x += 20
	k = 0

