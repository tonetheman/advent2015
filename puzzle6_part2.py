
GRID_SIZE=1000

class Grid:
	def __init__(self):
		self.grid = []
		for i in range(GRID_SIZE):
			self.grid.append(GRID_SIZE*[0])

	def clear(self):
		for i in range(GRID_SIZE):
			for j in range(GRID_SIZE):
				self.grid[i][j] = 0

	def add_range(self,p1,p2):
		x1 = p1[0]
		y1 = p1[1]
		x2 = p2[0]+1
		y2 = p2[1]+1
		# print "turn_range",x1,y1,x2,y2,value
		for i in range(x1,x2):
			for j in range(y1,y2):
				self.grid[i][j]=self.grid[i][j]+1

	def add_range2(self,p1,p2):
		x1 = p1[0]
		y1 = p1[1]
		x2 = p2[0]+1
		y2 = p2[1]+1
		# print "turn_range",x1,y1,x2,y2,value
		for i in range(x1,x2):
			for j in range(y1,y2):
				self.grid[i][j]=self.grid[i][j]+2

	def sub_range(self,p1,p2):
		x1 = p1[0]
		y1 = p1[1]
		x2 = p2[0]+1
		y2 = p2[1]+1
		# print "turn_range",x1,y1,x2,y2,value
		for i in range(x1,x2):
			for j in range(y1,y2):
				self.grid[i][j]=self.grid[i][j]-1

				if self.grid[i][j]<0:
					self.grid[i][j]=0

	def count_lights(self):
		count = 0
		for i in range(GRID_SIZE):
			for j in range(GRID_SIZE):
				if self.grid[i][j]==1:
					count = count + 1
		return count

	def sum_lights(self):
		_sum = 0
		for i in range(GRID_SIZE):
			for j in range(GRID_SIZE):
				_sum = _sum + self.grid[i][j]
		return _sum

	def turn_on(self,start_pos,end_pos):
		s = start_pos.split(",")
		s =map(int,s)
		e = end_pos.split(",")
		e =map(int,e)
		self.add_range((s[0],s[1]),(e[0],e[1]))

	def turn_off(self,start_pos,end_pos):
		s = start_pos.split(",")
		s =map(int,s)
		e = end_pos.split(",")
		e =map(int,e)
		self.sub_range((s[0],s[1]),(e[0],e[1]))

	def toggle(self,start_pos,end_pos):
		s = start_pos.split(",")
		s =map(int,s)
		e = end_pos.split(",")
		e =map(int,e)
		self.add_range2((s[0],s[1]),(e[0],e[1]))

	def make_p6(self):
		outf = open("p6.ppm","w")
		outf.write("P3\n")
		outf.write("1000 1000\n")
		outf.write("1\n")

		for i in range(GRID_SIZE):
			for j in range(GRID_SIZE):
				outf.write(str(self.grid[i][j]) + " 0 0 ")
			outf.write("\n")

		outf.close()

def doit():
	data = open("data6.txt","r").readlines()
	import string
	data = map(string.strip,data)

	grid = Grid()

	for line in data:
		if line.startswith("turn on"):
			ldata = line.split(" ")
			start_pos = ldata[2]
			end_pos = ldata[4]
			grid.turn_on(start_pos,end_pos)
		elif line.startswith("turn off"):
			ldata = line.split(" ")
			start_pos = ldata[2]
			end_pos = ldata[4]
			grid.turn_off(start_pos,end_pos)
		elif line.startswith("toggle"):
			ldata = line.split(" ")
			start_pos = ldata[1]
			end_pos = ldata[3]
			grid.toggle(start_pos,end_pos)
		else:
			print "ERR IN INPUT",line

	grid.make_p6()

	print grid.sum_lights()

doit()

