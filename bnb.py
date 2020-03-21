f = open("test.txt", "r")
inputString = []

i = 0
for x in f:
  inputString.insert(i,x.strip())
  i = i + 1
for x in inputString:
  print(x)