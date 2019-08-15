

def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:#sig:是去除txt開頭簽名檔
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	preson = None#代表空值
	for line in lines:
		if line == 'Allen':
			preson = 'Allen'
			continue
		elif line == 'Tom':
			preson = 'Tom'
			continue
		if preson:
			new.append(preson + ':' + line)#不太懂意思
	return new		

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)
main()