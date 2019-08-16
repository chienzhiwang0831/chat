
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:#sig:是去除txt開頭簽名檔
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	Allen_word_count = 0
	Allen_image_count = 0
	Allen_sticker_count = 0
	Viki_word_count = 0
	Viki_image_count = 0
	Viki_sticker_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if  name == 'Allen':
			if s[2] == '圖片':
				Allen_image_count += 1
			elif s[2] == '貼圖':
				Allen_sticker_count += 1
			else:
				for m in s[2:]:
					Allen_word_count += len(m)

		elif name == 'Viki':
			if s[2] == '圖片':
				Viki_image_count += 1
			elif s[2] == '貼圖':
				Viki_sticker_count += 1
			else:
				for m in s[2:]:
					Viki_word_count += len(m)


	print('allen說了', Allen_word_count, '個字')
	print('allen傳了', Allen_sticker_count, '個貼圖')
	print('allen傳了', Allen_image_count, '張圖片')

	print('viki說了', Viki_word_count, '個字')
	print('viki傳了', Viki_sticker_count, '個貼圖')
	print('viki傳了', Viki_image_count, '張圖片')






def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)
main()