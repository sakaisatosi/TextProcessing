# coding: utf-8
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

def main(word):
	# [n:m:s]はs個飛ばしでn番目からm-1番目の要素を参照
	print "".join(list(word)[::2]).encode("utf-8")

if __name__ == '__main__': # javaのmain関数のようなもの
	main(u"パタトクカシーー")
