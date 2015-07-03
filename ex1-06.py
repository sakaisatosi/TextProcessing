# coding: utf-8
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ． 

def n_gram(n, text):
	n_gram_list = []
	for i in range(0, len(list(text))+1-n):
		word = ""
		for j in range(0, n):
			word += list(text)[i+j]
		n_gram_list.append(word)
	return n_gram_list

def union(X, Y):
	

if __name__ == '__main__': 
	print n_gram(2, "paraparaparadise")
	print n_gram(2, "paragraph")
	
