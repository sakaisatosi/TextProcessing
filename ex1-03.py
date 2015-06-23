# coding: utf-8
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

def main(word):
	word_list = word.split(" ")
	word_len = [0] * 15
	for i in range(15):
		if "," in word_list[i] or "." in word_list[i]:
			word_len[i] = len(word_list[i]) -1
		else:
			word_len[i] = len(word_list[i])
	print word_len

if __name__ == '__main__':
	main("Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.")
