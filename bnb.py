f = open("test.txt", "r")
inputMatrix = [[],[],[],[]]
for i in range(4):
	temp = f.readline().strip().split()
	for j in range(4):
		if temp[j] != 'x':
			inputMatrix[i].append(int(temp[j]))
		else:
			inputMatrix[i].append(0)
print(inputMatrix)