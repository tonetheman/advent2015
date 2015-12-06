
GRID_SIZE=10
grid = []
for i in range(GRID_SIZE):
	grid.append(GRID_SIZE*[0])

def turn_off(grid):
	for i in range(GRID_SIZE):
		for j in range(GRID_SIZE):
			grid[i][j] = 0

def turn_range(grid,p1,p2,value):
	x1 = p1[0]
	y1 = p1[1]
	x2 = p2[0]+1
	y2 = p2[1]+1
	print "xrange",x1,x2
	print "yrange",y1,y2
	for i in range(x1,x2):
		for j in range(y1,y2):
			grid[i][j]=value

def count_lights(grid):
	count = 0
	for i in range(GRID_SIZE):
		for j in range(GRID_SIZE):
			if grid[i][j]==1:
				count = count + 1
	return count

def doit():
	data = open("data6.txt","r").readlines()
	import string
	data = map(string.strip,data)

	for line in data:
		if line.startswith("turn on"):
			pass
		elif line.startswith("turn off"):
			pass
		else:
			print "ERR IN INPUT",line



