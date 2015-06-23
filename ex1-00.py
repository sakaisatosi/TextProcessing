# coding:utf-8
# 文字列を得て、逆に並べる

import sys

word = sys.argv[1]

word_list = []
word_list = list(word)
word_list.reverse()
print ''.join(word_list)
