UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"
import time

correct = False
def  swap(a,b):
	a,b = b,a
def getCost(elem):
	return elem.cost
class Matrix:
	correct = False
	def __init__(self, contain, score = 0, last = ""):
		self.container = [[0 for y in range(4)] for x in range (4)]
		for i in range (4):
			for j in range(4):
				self.container[i][j] = int(contain[i][j])
		self.cost = score
		self.lastMovement = last
	def findBlank(self):
		a = [0,0]
		for i in range(4):
			for j in range(4):
				if self.container[i][j] == 16:
					a[0] = i
					a[1] = j
		return a
	def correctness(self):
		global correct
		c = 1
		for i in range(4):
			for j in range(4):
				if (self.container[i][j] != c):
					return False
				c = c + 1
		correct = True
	# control movement consider the lastMovement
	def canMove(self, movement):
		blank = self.findBlank()
		blankX, blankY = blank[0], blank[1]
		result = False
		if (movement == UP and self.lastMovement != UP and blankX != 0):
			result = True
		elif (movement == DOWN and self.lastMovement != DOWN and blankX != 3):
			result = True
		elif (movement == RIGHT and self.lastMovement != RIGHT and blankY != 3):
			result = True
		elif (movement == LEFT and self.lastMovement != LEFT and blankX != 0):
			result = True
		return result
	def move(self,movement): 
		blank = self.findBlank()
		blankX, blankY = blank[0], blank[1]
		a = False
		if movement == UP and blankX != 0 and self.lastMovement != UP:
			self.container[blankX][blankY], self.container[blankX - 1][blankY] = self.container[blankX - 1][blankY], self.container[blankX][blankY]
			self.lastMovement = UP
			a = True
		elif movement == DOWN and blankX != 3 and self.lastMovement != DOWN:
			self.container[blankX][blankY], self.container[blankX + 1][blankY] = self.container[blankX + 1][blankY], self.container[blankX][blankY]
			self.lastMovement = DOWN
			a = True
		elif movement == LEFT and blankY != 0 and self.lastMovement != LEFT:
			self.container[blankX][blankY], self.container[blankX][blankY - 1] = self.container[blankX][blankY - 1], self.container[blankX][blankY]
			self.lastMovement = LEFT
			a = True
		elif movement == RIGHT and blankY != 3 and self.lastMovement != RIGHT:
			self.container[blankX][blankY], self.container[blankX][blankY + 1] = self.container[blankX][blankY + 1], self.container[blankX][blankY]
			self.lastMovement = RIGHT
			a = True

		# count cost LESS(X)
		#self cost to movement
		self.cost = self.cost + 1 + self.less()
		self.correctness()
		# print("test")
		return a
	
	# Count cost function less
	def less(self):
		result = 0
		for i in range(4):
			for j in range(4):
				if self.container[i][j] != 16:
					for k in range(i,4):
						for l in range(j,4):
							if self.container[i][j] > self.container[k][l] and self.container[k][l] != 16:
								result = result + 1
		# print(result)
		return result

	# Inherit all possible movement
	def inherit(self):
		resultNodeQueue = []
		
		
		movementList = [UP,LEFT,DOWN,RIGHT]
		for i in range(4):
			if self.move(movementList[i]):
				# print(tempNode.container)
				# tempNode = Matrix(self.container,self.cost,self.lastMovement)
				
				print(movementList[i])
				# print(movementList[(i + 2) % 4])
				resultNodeQueue.append(Matrix(self.container,self.cost,self.lastMovement))
				resultNodeQueue[len(resultNodeQueue) - 1].move(movementList[i])

				
				print("start1")
				for x in resultNodeQueue:
					print(x.container)
				print("end1")
				# print(tempNode.container)
				self.move(movementList[(i + 2) % 4])
				time.sleep(1)
				
			print((i+2) % 4)
			print("WRONG")
			print(self.container)
			
		# print(resultNodeQueue[0].container)
		# print("start2")
		# for x in resultNodeQueue:
		# 	print(x.container)
		# print("end2")
		return resultNodeQueue

class MatrixQueue:
	# As static atribbute
	nodeExpand = 0
	def __init__(self,base):
		self.element = [base]
	def add(self, newElement):
		self.element = self.element + newElement
		MatrixQueue.nodeExpand = MatrixQueue.nodeExpand + len(newElement)
	def produce(self):
		if len(self.element) != 0:
			self.add(self.element[0].inherit())	
			self.element.pop(0)
			self.element.sort(key = getCost)
			for i in self.element:
				print(i.container)
			# print(self.element[0].container)
			time.sleep(1)


f = open("test.txt", "r")
inputMatrix = [[0 for y in range(4)] for x in range (4)]


for i in range(4):
	temp = f.readline().strip().split()
	for j in range(4):
		if temp[j] != 'x':
			inputMatrix[i][j] = int(temp[j])
		else:
			inputMatrix[i][j] = 16
		# print(str(inputMatrix[i][j]))
baseNode = Matrix(inputMatrix)
for i in range(4):
	for j in range(4):
		baseNode.container[i][j] = inputMatrix[i][j]
		print(baseNode.container[i][j])
		
# for i in range(4):
# 	for j in range(4):
# 		# print(baseNode.container[i][j])
matrixQueue = MatrixQueue(baseNode)
# matrixQueue.element[0].move(RIGHT)
# print(matrixQueue.element[0].container)
while(len(matrixQueue.element) != 0 and not correct):
	matrixQueue.produce()

# baseNode.move(RIGHT)
# print(baseNode.container)
# baseNode.move(DOWN)
# print(baseNode.container)
 
