UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"
def  swap(a,b):
	a,b = b,a
class matrix:
	def __init__(self):
		self.container = [[],[],[],[]]
		self.cost = 0
		self.lastMovement = ""
	def __init__(self,other, inherit = True):
		self.container = other.container
		self.cost = other.cost
		if (inherit):
			self.lastMovement = other.lastMovement + 1
		else:
			self.lastMovement = other.lastMovement
	def findBlank(self):
		for i in range(4):
			for j in range(4):
				if (self.container[i][j]):
					return i,j
	def move(self,movement): # control movement consider the lastMovement
		blankX,blankY = self.findBlank()
		if movement == UP and blankX != 0 and self.lastMovement != DOWN:
			swap(self.container[blankX][blankY],self.container[blankX + 1][blankY])
			self.lastMovement = UP
		elif movement == DOWN and blankX != 3 and self.lastMovement != UP:
			swap(self.container[blankX][blankY],self.container[blankX - 1][blankY])
			self.lastMovement = DOWN
		elif movement == LEFT and blankY != 0 and self.lastMovement != RIGHT:
			swap(self.container[blankX][blankY],self.container[blankX][blankY - 1])
			self.lastMovement = LEFT
		elif movement == RIGHT and blankY != 3 and self.lastMovement != LEFT:
			swap(self.container[blankX][blankY],self.container[blankX][blankY + 1])
			self.lastMovement = RIGHT

class matrixQueue:
	# As static atribbute
	nodeExpand = 0
	def __init__(self):
		self.element = []
	def add(self, newElement):
		self.container.append(newElement)
		nodeExpand = nodeExpand+1
f = open("test.txt", "r")
inputMatrix = [[],[],[],[]]
for i in range(4):
	temp = f.readline().strip().split()
	for j in range(4):
		if temp[j] != 'x':
			inputMatrix[i].append(int(temp[j]))
		else:
			inputMatrix[i].append(0)
queue = []
queue.append(inputMatrix)
inputMatrix[1][0] = 4
queue.append(inputMatrix)
print(queue)
