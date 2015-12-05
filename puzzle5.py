
def is_bad(s):
	res = False
	BAD = [ "ab", "cd", "pq", "xy" ]
	for i in range(0, len(s)-1):
		part = s[i:i+2]
		if part in BAD:
			return True

	return res

def has_3_vowels(s):
	VOWELS = [ "a", "e", "i", "o", "u" ]
	vowel_count = 0
	for c in s:
		if c in VOWELS:
			vowel_count = vowel_count +1
	if vowel_count >= 3:
		return True
	return False

def has_twice_letter(s):
	res = False
	for i in range(0, len(s)-1):
		part = s[i:i+2]
		if part[0] == part[1]:
			return True
	return res

def check(word):
	if is_bad(word):
		# print "is bad"
		return False
	if not has_3_vowels(word):
		# print "not has 3 vowels"
		return False
	if not has_twice_letter(word):
		# print "not has twice letter"
		return False
	return True

def doit():
	data = open("data5.txt","r").readlines()

	import string
	data = map(string.strip,data)

	count = 0
	for word in data:
		if check(word):
			count = count + 1
	print count
	

def test():
	print check("ugknbfddgicrmopn")
	print check("aaa")
	print check("jchzalrnumimnmhp")
	print check("haegwjzuvuyypxyu")
	print check("dvszwmarrgswjxmb")


doit()