# -*- coding: utf-8 -*-
import unicodedata
import re
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Read the whole text.
text = open('tweets.txt').read()
text=text.split('\n')
tweets=[aux.split("|") for aux in text ]
tweets=[aux for aux in tweets if len(aux)==4 ]

print "Number of tweets: %s" % (len(tweets))
tweets=[unicodedata.normalize('NFKD', unicode(aux[2],'utf-8')).encode('ASCII', 'ignore') for aux in tweets]
#generate a text whith all the tweets about a certain candidate, taking out the @mentions.
wc={}
wc['Pinera']=' '.join([' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",aux).split()) for aux in tweets if '@sebastianpinera' in aux])
wc['Guillier']=' '.join([' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",aux).split()) for aux in tweets if '@SenadorGuillier' in aux])
wc['Goic']=' '.join([' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",aux).split()) for aux in tweets if '@carolinagoic' in aux])
wc['Sanchez']=' '.join([' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",aux).split()) for aux in tweets if '@labeasanchez' in aux])

#for each candidate, clean the text of common words and plot the wordcloud
for x in wc:
	wc[x]=wc[x].replace('RT','')
	wc[x]=wc[x].replace(' la ',' ')
	wc[x]=wc[x].replace(' el ',' ')
	wc[x]=wc[x].replace(' de ',' ')
	wc[x]=wc[x].replace(' es ',' ')
	print x
	print len(wc[x])
	wordcloud = WordCloud(background_color="white", max_font_size=40).generate(wc[x])
	plt.figure()
	plt.imshow(wordcloud, interpolation="bilinear")
	plt.axis("off")
	plt.show()





	

