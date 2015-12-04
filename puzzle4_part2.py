
import hashlib

secret_key = "iwrupvqb"

for i in range(10000000):
	ts = secret_key + str(i)

	m = hashlib.md5()
	m.update(ts)
	hd = m.hexdigest()
	if hd[0:6] == "000000":
		print i,ts, m.hexdigest()
		break
	
