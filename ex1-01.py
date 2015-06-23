# coding: utf-8
# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ.

def main(word):
	# [n:m:s]はs個飛ばしでn番目からm-1番目の要素を参照
	print "".join(list(word)[::2]).encode("utf-8")

if __name__ == '__main__': # javaのmain関数のようなもの
	main(u"パタトクカシーー")
