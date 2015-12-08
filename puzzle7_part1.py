
data = open("data7.txt","r").readlines()

import string,re
data = map(string.strip,data)

syms = {}

total_instructions = 0
total_assigns = 0
total_and1 = 0
total_or1 = 0

P = re.compile("([a-z0-9]+) (AND|OR|LSHIFT|RSHIFT) ([a-z0-9]+) -> ([a-z0-9]+)")
PASSIGN = re.compile("(\d+) -> ([a-z]+)")
NOT = re.compile("NOT ([a-z]+) -> ([a-z]+)")
SIMPLE_ASSIGN = re.compile("([a-z]+) -> ([a-z]+)")
for line in data:
	total_instructions = total_instructions + 1

	m = P.match(line)
	if m is not None:
		pass
	else:
		m1 = NOT.match(line)
		if m1 is not None:
			pass
		else:
			m2 = PASSIGN.match(line)
			if m2 is not None:
				val = m2.group(1)
				sym = m2.group(2)
				print "PASSIGN",val,sym
				syms[sym] = int(val)
			else:
				m3 = SIMPLE_ASSIGN.match(line)
				if m3 is not None:
					pass
				else:
					print "not matched",line


print "syms", syms
print "total instructions",total_instructions



