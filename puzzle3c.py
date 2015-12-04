
# part 2 of puzzle3

data = open("data3.txt","r").read()
import string
data = string.strip(data)

class Santa:
	def __init__(self,world):
		self.x = 0
		self.y = 0
		self.world = world
		self.inc(0,0)
	def inc(self,x,y):
		self.world[(self.x,self.y)] = 1
	def feed(self,c):
		self.inc(self.x,self.y)
		if c == "^":
			self.y = self.y - 1
		elif c =="v":
			self.y = self.y + 1
		elif c == "<":
			self.x = self.x - 1
		elif c == ">":
			self.x = self.x + 1
		else:
			print "ERR",c

world = {}
santa = Santa(world)
santa2 = Santa(world)		
who = 0
for c in data:
	if who%2 == 0:
		santa.feed(c)
	else:
		santa2.feed(c)
	who = who + 1

print len(world)
