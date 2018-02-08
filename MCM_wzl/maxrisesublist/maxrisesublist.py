st = open ("maxrisesublist.txt").read().split(' ')
l = len(st)
maxlen = range(l)
for i in range(l):
	maxlen[i] = 0
maxlen[0]=1;

for j in range(1,l+1):
	for i in range(i):
		if st[j]>st[i] :
			maxlen[j] = max(maxlen[0:j])+1
		else:
			maxlen[j] = max(maxlen[0:j])

print maxlen[l-1];
