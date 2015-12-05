

def check_pair(s):
	print "check_pair passed string",s
	res = True
	pairs = []
	for i in range(0, len(s)-1):
		part = s[i:i+2]
		pairs.append((part,i))

	for p in pairs:
		print "\tme",p
		for q in pairs:
			print "\tlooking at",q
			if p==q:
				print "\tskipping myself"
				continue

			print "\tcheck",p,q
			if p[0]==q[0]:
				print "\tpossible match"
				if p[1]+1 == q[1] or p[1]-1 == q[1]:
					print "\telim for overlap"
					res = False
				else:
					return True

	return res

# print check_pair("xyxy")
# print check_pair("aabcdefgaa")
# print check_pair("aaa")