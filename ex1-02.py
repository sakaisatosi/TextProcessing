# coding: utf-8
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

def main(word1, word2):
	ans = ""
	for i in range(4):
		ans += list(word1)[i]
		ans += list(word2)[i]
	print ans

if __name__ == '__main__': # javaのmain関数のようなもの
	main(u"パトカー", u"タクシー")
