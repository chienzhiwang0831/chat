def read(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:#sig-刪除開頭\utff簽名檔
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	preson = None
	for line in lines:
		if 'Allen' == line:
			preson = 'Allen'
			continue
		elif 'Tom' in line:
			preson = 'Tom'
			continue
		if preson:
			new.append(preson + ':' + line)#不懂這段????
	return new


def write(filename, lines):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in lines:
			f.write(line + '\n')


lines = read('input.txt')
lines = convert(lines)
write('output.txt', lines)
print(lines)