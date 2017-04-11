# encoding: utf-8
import os
import io
import os.path
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize,sent_tokenize
ps=PorterStemmer()
os.chdir("/home/shivendra/Desktop/bbc/politics")
for filename in os.listdir(os.getcwd()):
	finallist=[]
	print filename
	with io.open(filename,"r" ,encoding="utf-8")as fp:
		s=fp.read()
		stop_words=set(stopwords.words("english"))
		word_tokens=word_tokenize(s)
		filtered_sentence=[w for w in word_tokens if  w  not in stop_words]
		stemmed_sentence=[ ps.stem(w) for w in filtered_sentence ]
		for w in stemmed_sentence:
			finallist.append(w)
		print finallist



