sumofsquare = 0
squareofsum = 0
for i in range(1,101):
	sumofsquare += i*i
	squareofsum += i
squareofsum = squareofsum*squareofsum
print squareofsum - sumofsquare