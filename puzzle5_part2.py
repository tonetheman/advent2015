
def log(*args):
	return
	ts = ""
	for a in args:
		ts = ts + str(a) + " "
	print ts

def check_pair(s):
	log("check_pair passed string",s)
	res = True
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

print check_pair("xyxy")
# print check_pair("aabcdefgaa")
# print check_pair("aaa")