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
		c = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
		print("correctness")
		print(self.container)
		print("correctness END")
		point = 0
		for i in range(4):
			for j in range(4):
				if (self.container[i][j] == c[i][j]):
					point = point + 1
		if point == 16:
			correct = True
		# print("YOLO")
	# control movement consider the lastMovement
	def canMove(self, movement):
		blank = self.findBlank()
		blankX, blankY = blank[0], blank[1]
		result = False
		if (movement == UP and self.lastMovement != DOWN and blankX != 0):
			result = True
		elif (movement == DOWN and self.lastMovement != UP and blankX != 3):
			result = True
		elif (movement == RIGHT and self.lastMovement != LEFT and blankY != 3):
			result = True
		elif (movement == LEFT and self.lastMovement != RIGHT and blankY != 0):
			result = True
		return result
	def move(self,movement): 
		blank = self.findBlank()
		blankX, blankY = blank[0], blank[1]
		if self.canMove(movement):
			if movement == UP:
				self.container[blankX][blankY], self.container[blankX - 1][blankY] = self.container[blankX - 1][blankY], self.container[blankX][blankY]
				self.lastMovement = UP

			elif movement == DOWN:
				self.container[blankX][blankY], self.container[blankX + 1][blankY] = self.container[blankX + 1][blankY], self.container[blankX][blankY]
				self.lastMovement = DOWN

			elif movement == LEFT:
				self.container[blankX][blankY], self.container[blankX][blankY - 1] = self.container[blankX][blankY - 1], self.container[blankX][blankY]
				self.lastMovement = LEFT

			elif movement == RIGHT:
				self.container[blankX][blankY], self.container[blankX][blankY + 1] = self.container[blankX][blankY + 1], self.container[blankX][blankY]
				self.lastMovement = RIGHT
		#self cost to movement
		self.cost = self.cost + 1 + self.less()
		self.correctness()
		# print("CHECK")

	
	# Count cost function less
	def less(self):
		result = 0
		for i in range(4):
			for j in range(4):
				if self.container != 16:
					for k in range(i,4):
						if k == i:
							for l in range(j,4):
								if self.container[i][j] > self.container[k][l]:
									result = result + 1
						else:
							for l in range(4):
								if self.container[i][j] > self.container[k][l]:
									result = result + 1

		return result

	# Inherit all possible movement
	def inherit(self):
		resultNodeQueue = []
		resultNodeQueue.clear()
		
		movementList = [UP,LEFT,DOWN,RIGHT]
		for i in range(4):
			if self.canMove(movementList[i]):

				# print(movementList[i])

				resultNodeQueue.append(Matrix(self.container,self.cost,self.lastMovement))
				resultNodeQueue[len(resultNodeQueue) - 1].move(movementList[i])

				
				# print("start1")
				# for x in resultNodeQueue:
				# 	print(x.container)
				# print("end1")

				# time.sleep(1)
			# else:
			# 	print()
			# 	print("WRONG")
			# 	print(movementList[i])
			# 	print("WRONG END")
			# 	print()
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
			print("produce")
			for i in self.element:
				print(i.container)
			print("produce end")

			# time.sleep(1)


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
		
matrixQueue = MatrixQueue(baseNode)
while(len(matrixQueue.element) != 0 and not correct):
	matrixQueue.produce()

for i in matrixQueue.element:
	print(getCost(i))
print(correct)
 
