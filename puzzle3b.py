
data = open("data3.txt","r").read()
import string
data = string.strip(data)

world = {}
x = 0
y = 0
world[(x,y)] = 1
for c in data:
	if c == "^":
		world[(x,y)] = 1
		y = y - 1
	elif c =="v":
		world[(x,y)] = 1
		y = y + 1
	elif c == "<":
		world[(x,y)] = 1
		x = x - 1
	elif c == ">":
		world[(x,y)] = 1
		x = x + 1
	else:
		print "ERR",c

print len(world)
