s = 'azcbobobegghakl'
count = 0
l = len(s)
for i in range(l-2):
	if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
		count +=1
print(count)