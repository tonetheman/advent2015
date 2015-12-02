
lines = open("data2.txt","r").readlines()

import string
import re
P=re.compile("(\d+)x(\d+)x(\d+)")

def f(l,w,h):
  side1 = l*w
  side2= w*h
  side3 = h*l

  part1 = 2*l*w + 2*w*h + 2*h*l
  part2 = 0
  
  # figure smallest side between 1 and 2
  if side1<side2:
    part2 = side1
  else:
    part2 = side2

  # figure smallest side between 3 and best so far
  if part2<side3:
    part2 = part2
  else:
    part2 = side3
  return part1 + part2

def ribbon(l,w,h):
	perim1 = l*2 + w*2
	perim2 = w*2 + h*2
	perim3 = h*2 + l*2
	f = 0
	if perim1<perim2:
		f = perim1
	else:
		f = perim2
	if f<perim3:
		f = f
	else:
		f = perim3
	bow = l * w * h
	return f + bow
  
grand = 0
rgrand = 0
for line in lines:
	line = string.strip(line)
	m = P.match(line)
	if m:
		a = float(m.group(1))
		b = float(m.group(2))
		c = float(m.group(3))
		total = f(a,b,c)
		rtotal = ribbon(a,b,c)
		# print total
		grand = grand + total
		rgrand = rgrand + rtotal

print grand
print rgrand
