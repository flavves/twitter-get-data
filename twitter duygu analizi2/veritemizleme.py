# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 01:00:08 2022

@author: okmen
"""


import pandas as pd


############################################################################################3


with open("onlinealisveris.txt", "r") as dosya:
    metinler = dosya.readlines()



vektor= pd.Series(metinler)

mdf= pd.DataFrame(vektor,columns=["twitler"])
yeni_mdf=mdf.copy()

#küçük harf yapma

yeni_mdf=yeni_mdf["twitler"].apply(lambda x: " ".join(x.lower() for x in x.split()))

#noktalama işaretleri siliniyor

type(yeni_mdf)

yeni_mdf=yeni_mdf.str.replace("[^\w\s]","")


#sayıların silinmesi

yeni_mdf=yeni_mdf.str.replace("\d","")

#stopwords mantığı

yeni_mdf=pd.DataFrame(yeni_mdf,columns=["twitler"])
yeni_mdf
!pip install nltk

import nltk
nltk.download("stopwords")

from nltk.corpus import stopwords

sw=stopwords.words("turkish")
sw.append("m")
sw.append("replying to")
sw.append("h")
sw.append("to")
sw.append("replying")
sw.append("and")

yeni_mdf=yeni_mdf["twitler"].apply(lambda x: " ".join(x for x in x.split() if x not in sw))


#az geçen kelimelerin silinmesi (opsiyonel) kullanmayacağım şuan

yeni_mdf= pd.DataFrame(yeni_mdf, columns=["twitler"])

az_gecenler=pd.Series(" ".join(yeni_mdf["twitler"]).split()).value_counts()




#son hali ile ilk hali karşılaştırma

#ilk hali

mdf["twitler"][0:5]
#son hali
yeni_mdf["twitler"][0:5]

yeni_mdf.to_csv('onlinealisveristemizlenmis.csv')


############################################################################################################



############################################################################################3


with open("onlinecalisma.txt", "r") as dosya:
    metinler = dosya.readlines()



vektor= pd.Series(metinler)

mdf= pd.DataFrame(vektor,columns=["twitler"])
yeni_mdf=mdf.copy()

#küçük harf yapma

yeni_mdf=yeni_mdf["twitler"].apply(lambda x: " ".join(x.lower() for x in x.split()))

#noktalama işaretleri siliniyor

type(yeni_mdf)

yeni_mdf=yeni_mdf.str.replace("[^\w\s]","")


#sayıların silinmesi

yeni_mdf=yeni_mdf.str.replace("\d","")

#stopwords mantığı

yeni_mdf=pd.DataFrame(yeni_mdf,columns=["twitler"])
yeni_mdf
!pip install nltk

import nltk
nltk.download("stopwords")

from nltk.corpus import stopwords

sw=stopwords.words("turkish")
sw.append("m")
sw.append("replying to")
sw.append("h")
sw.append("to")
sw.append("replying")
sw.append("and")

yeni_mdf=yeni_mdf["twitler"].apply(lambda x: " ".join(x for x in x.split() if x not in sw))


#az geçen kelimelerin silinmesi (opsiyonel) kullanmayacağım şuan

yeni_mdf= pd.DataFrame(yeni_mdf, columns=["twitler"])

az_gecenler=pd.Series(" ".join(yeni_mdf["twitler"]).split()).value_counts()




#son hali ile ilk hali karşılaştırma

#ilk hali

mdf["twitler"][0:5]
#son hali
yeni_mdf["twitler"][0:5]

yeni_mdf.to_csv('onlinecalismatemizlenmis.csv')


############################################################################################################





############################################################################################3


with open("onlineegitim.txt", "r") as dosya:
    metinler = dosya.readlines()



vektor= pd.Series(metinler)

mdf= pd.DataFrame(vektor,columns=["twitler"])
yeni_mdf=mdf.copy()

#küçük harf yapma

yeni_mdf=yeni_mdf["twitler"].apply(lambda x: " ".join(x.lower() for x in x.split()))

#noktalama işaretleri siliniyor

type(yeni_mdf)

yeni_mdf=yeni_mdf.str.replace("[^\w\s]","")


#sayıların silinmesi

yeni_mdf=yeni_mdf.str.replace("\d","")

#stopwords mantığı

yeni_mdf=pd.DataFrame(yeni_mdf,columns=["twitler"])
yeni_mdf
#!pip install nltk

import nltk
nltk.download("stopwords")

from nltk.corpus import stopwords

sw=stopwords.words("turkish")
sw.append("m")
sw.append("replying to")
sw.append("h")
sw.append("to")
sw.append("replying")
sw.append("and")

yeni_mdf=yeni_mdf["twitler"].apply(lambda x: " ".join(x for x in x.split() if x not in sw))


#az geçen kelimelerin silinmesi (opsiyonel) kullanmayacağım şuan

yeni_mdf= pd.DataFrame(yeni_mdf, columns=["twitler"])

az_gecenler=pd.Series(" ".join(yeni_mdf["twitler"]).split()).value_counts()




#son hali ile ilk hali karşılaştırma

#ilk hali

mdf["twitler"][0:5]
#son hali
yeni_mdf["twitler"][0:5]

yeni_mdf.to_csv('onlineegitimtemizlenmis.csv')


############################################################################################################














