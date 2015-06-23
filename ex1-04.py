# coding: utf-8
# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ． 

def main(word):
	word_list = word.split(" ")
	ans_dict = {}
	for i in range(20):
		if i in [1,5,6,7,8,9,15,16,19]:
			ans_dict.update({word_list[i][0]:i+1})
		else:
			ans_dict.update({word_list[i][:2]:i+1})
	print ans_dict

if __name__ == '__main__': # javaのmain関数のようなもの
	main("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.")
