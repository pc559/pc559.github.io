#!/usr/bin/env python

import sys
from collections import Counter

filename = ''

if len(sys.argv)<2:
	print 'No filename given'
	sys.exit()

try:	text = open(sys.argv[1]).readlines()
except IOError:
	print 'Unable to open file'
	sys.exit()

def extract(text,start,end,include_start=True):
	ind_1 = text.find(start)
	ind_2 = text.find(end,ind_1+len(start))
	extr = text[ind_1+len(start)*(not include_start):ind_2]
	return extr

def common_words(links):
	if type(links)==list:
		words = []
		for link in links:
			word = extract(link,'.','.',False)
			if '/' in word: word = extract(link,'//','.',False)
			words.append(word)
		return Counter(words)
	elif type(links)==str:
		word = extract(links,'.','.',False)
		if '/' in word: word = extract(links,'//','.',False)
		return word


links = [extract(t,'http',' ') for t in text if 'http' in t]

words_count = common_words(links)

top_freq = [link for link in links if words_count[common_words(link)]>=10]
med_freq = [link for link in links if words_count[common_words(link)]<10 and words_count[common_words(link)]>1]
bot_freq = [link for link in links if words_count[common_words(link)]==1]


for link in top_freq:
	results = open('extractor_'+common_words(link)+'_links.txt','a')
	results.write(link+'\n')
	results.close()
for link in med_freq:
	results = open('extractor_fairly_common_links.txt','a')
	results.write(link+'\n')
	results.close()
for link in bot_freq:
	results = open('extractor_other_links.txt','a')
	results.write(link+'\n')
	results.close()








