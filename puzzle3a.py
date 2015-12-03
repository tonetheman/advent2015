
data = open("data3.txt","r").read()
import string
data = string.strip(data)

def add_inc(gd,x,y):
	key = x * 2 + y
	if gd.has_key(key):
		tmp = gd[key]
		tmp = tmp + 1
		gd[key] = tmp
	else:
		gd[key] = 1

gd = {} 
x = 0
y = 0
add_inc(gd,x,y)

for c in data:
	if c == "^":
		y = y + 1
	elif c == "v":
		y = y - 1
	elif c == ">":
		x = x + 1	
	elif c == "<":
		x = x - 1
	else:
		print "ERROR on input",c
	add_inc(gd,x,y)

count = 0
for k,v in gd.iteritems():
	print k,v
	count = count + 1
print "total houses", count

