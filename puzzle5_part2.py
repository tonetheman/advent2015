
def log(*args):
	ts = ""
	for a in args:
		ts = ts + str(a) + " "
	print ts

def check_pair(s):
	log("check_pair passed string",s)
	res = False
	pairs = []
	for i in range(0, len(s)-1):
		part = s[i:i+2]
		pairs.append((part,i))

	for p in pairs:
		log("\tme",p)
		for q in pairs:
			log("\tlooking at",q)
			if p==q:
				log("\tskipping myself")
				continue

			log("\tcheck",p,q)
			if p[0]==q[0]:
				log("\tpossible match")
				if p[1]+1 == q[1] or p[1]-1 == q[1]:
					log( "\telim for overlap")
					res = False
				else:
					return True

	return res

def check_repeated_letter(s):
	log("check_repeated_letter passed string",s)
	for index in range(len(s)-2):
		current_letter = s[index]
		must_match = s[index+2]
		if current_letter == must_match:
			log("current_letter matches must_match",current_letter,
				must_match)
			return True
	log("check_repeated_letter is returing false")
	return False

def check(s):
	if check_repeated_letter(s):
		if check_pair(s):
			return True
	return False

def test():
	#res = check("qjhvhtzxzqqjkmpb")
	# res = check("xxyxx")
	# res = check("uurcxstgmygtbstg")
	res = check("ieodomkazucvgmuy")
	print "nice",res
	# print check("uurcxstgmygtbstg")
	# print check("ieodomkazucvgmuy")


def doit():
	data = open("data5.txt","r").readlines()

	import string
	data = map(string.strip,data)

	count = 0
	for word in data:
		if check(word):
			count = count + 1
	print count

doit()





