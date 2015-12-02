
import string

data = open("data1.txt","r").read()
data = string.strip(data)

floor = 0
for c in data:
  if c == "(":
    floor = floor + 1
  elif c == ")":
    floor = floor -1
  else:
    print "ERRRRROR"
print floor
