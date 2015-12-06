
GRID_SIZE=1000
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
	# print "turn_range",x1,y1,x2,y2,value
	for i in range(x1,x2):
		for j in range(y1,y2):
			grid[i][j]=value
def toggle_range(grid,p1,p2):
	x1 = p1[0]
	y1 = p1[1]
	x2 = p2[0]+1
	y2 = p2[1]+1
	for i in range(x1,x2):
		for j in range(y1,y2):
			value = grid[i][j]
			if value==1:
				grid[i][j]=0
			else:
				grid[i][j]=1

def count_lights(grid):
	count = 0
	for i in range(GRID_SIZE):
		for j in range(GRID_SIZE):
			if grid[i][j]==1:
				count = count + 1
	return count

def turn_on(start_pos,end_pos):
	s = start_pos.split(",")
	s =map(int,s)
	e = end_pos.split(",")
	e =map(int,e)
	turn_range(grid,(s[0],s[1]),(e[0],e[1]),1)

def turn_off(start_pos,end_pos):
	s = start_pos.split(",")
	s =map(int,s)
	e = end_pos.split(",")
	e =map(int,e)
	turn_range(grid,(s[0],s[1]),(e[0],e[1]),0)

def toggle(start_pos,end_pos):
	s = start_pos.split(",")
	s =map(int,s)
	e = end_pos.split(",")
	e =map(int,e)
	toggle_range(grid,(s[0],s[1]),(e[0],e[1]))

def make_p6(grid):
	outf = open("p6.ppm","w")
	outf.write("P6\n")
	outf.write("1000 1000\n")
	outf.write("1\n")

	for i in range(GRID_SIZE):
		for j in range(GRID_SIZE):
			outf.write(str(grid[i][j]) + " ")
		outf.write("\n")

	outf.close()

def doit():
	data = open("data6.txt","r").readlines()
	import string
	data = map(string.strip,data)

	for line in data:
		if line.startswith("turn on"):
			ldata = line.split(" ")
			start_pos = ldata[2]
			end_pos = ldata[4]
			turn_on(start_pos,end_pos)
		elif line.startswith("turn off"):
			ldata = line.split(" ")
			start_pos = ldata[2]
			end_pos = ldata[4]
			turn_off(start_pos,end_pos)
		elif line.startswith("toggle"):
			ldata = line.split(" ")
			start_pos = ldata[1]
			end_pos = ldata[3]
		else:
			print "ERR IN INPUT",line

	make_p6(grid)

	print count_lights(grid)

doit()

