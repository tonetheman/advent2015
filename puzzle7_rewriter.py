
data = open("data7.txt","r").readlines()

import string
data = map(string.strip,data)

import re
PA = re.compile("([0-9a-z]+) -> ([a-z]+)")
NOTRULE = re.compile("NOT ([a-z]+) -> ([a-z]+)")
ANDOR = re.compile("([0-9a-z]+) (AND|OR) ([a-z]+) -> ([a-z]+)")
SHIFT = re.compile("([a-z]+) (LSHIFT|RSHIFT) (\d+) -> ([a-z]+)")

def log(*args):
	ts = ""
	for a in args:
		ts = ts + str(a) + " "
	print ts

def try_assign(line):
	if PA.match(line):
		m = PA.match(line)
		log(m.group(2), "=", m.group(1))
		return True
	return False
def try_andor(line):
	if ANDOR.match(line):
		m = ANDOR.match(line)
		if m.group(2) == "AND":
			log(m.group(3), "=", m.group(1), "&", m.group(3))
		elif m.group(2) == "OR":
			log(m.group(3), "=", m.group(1), "|", m.group(3))
		return True
	return False
def try_shift(line):
	if SHIFT.match(line):
		m = SHIFT.match(line)
		if m.group(2) == "LSHIFT":
			log(m.group(4),"=",m.group(1),"<<",m.group(3))
		elif m.group(2) == "RSHIFT":
			log(m.group(4),"=",m.group(1),">>",m.group(3))
		return True
	return False
def try_not(line):
	if NOTRULE.match(line):
		m = NOTRULE.match(line)
		log(m.group(2), "=", "~", m.group(1))
		return True
	return False


for line in data:
	if try_assign(line):
		pass
	elif try_andor(line):
		pass
	elif try_shift(line):
		pass
	elif try_not(line):
		pass
	else:
		print line