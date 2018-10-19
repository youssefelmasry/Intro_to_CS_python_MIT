s = 'ytvopabo'
l = ''
tmp = s[0]
length = len(s)
for i in range(1,length):
	if s[i] >= tmp[-1]:
		tmp += s[i]
	else:
		if len(tmp) > len(l):
			l = tmp
		tmp = s[i]
if len(tmp) > len(l):
	l = tmp
print(l)