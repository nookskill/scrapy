f = open('App.json','r')
i = 1
for line in f:
	if 'pet' in line.lower():
		print str(i)+": "+line,
		i+=1
