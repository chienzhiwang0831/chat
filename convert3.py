
lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line)

for line in lines:
	s = line.split(' ')#s[0]__[13:34Allen]__[0123456789]
	time = s[0][:5]#01234重0~4開始，到5以後都不要
	name = s[0][5:]#01234重5開始算，到結尾無
	print(name)
	#print(name)

