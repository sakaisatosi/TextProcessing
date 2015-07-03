# coding: utf-8
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

def ngram(n, style, text):
	if style == "char":
		for i in range(0, len(list(text))+1-n):
			result = ""
			for j in range(0, n):
				result += list(text)[i+j]
			print result
	elif style == "word":
		word_list = text.split(" ")
		for i in range(0, len(word_list)+1-n):
			result = ""
			for j in range(0, n):
				result += word_list[i+j] + " "
			print result

if __name__ == '__main__': 
	ngram(3, "word", "I am an NLPer")
