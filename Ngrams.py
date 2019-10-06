# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 09:05:26 2019
 
@author: MWorthington
"""
from collections import Counter
from nltk import ngrams
from nltk.corpus import stopwords
import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
import numpy as np
import pandas as pd
import re
 
def Unigrams(data,outputFile):
    words = open(data,encoding="latin").read().lower()
    words = re.sub(r'[^\w\s]','', words)
    words = re.sub(r'\d+','', words).split(" ")
    stop_words = stopwords.words('english')
    words = [word for word in words if word not in stop_words]
    ngram_counts = Counter(ngrams(words, 1))
    print(ngram_counts.most_common(200))
    with open(outputFile, 'w') as f:
        for key in ngram_counts.keys():
            f.write("%s,%s\n"%(key,ngram_counts[key]))
 
def Bigrams(data,outputFile):
    words = open(data,encoding="latin").read().lower()
    words = re.sub(r'[^\w\s]','', words)
    words = re.sub(r'\d+','', words).split(" ")
    stop_words = stopwords.words('english')
    words = [word for word in words if word not in stop_words]
    ngram_counts = Counter(ngrams(words, 2))
    print(ngram_counts.most_common(200))
    with open(outputFile, 'w') as f:
        for key in ngram_counts.keys():
            f.write("%s,%s\n"%(key,ngram_counts[key]))
    
def Trigrams(data,outputFile):
    words = open(data,encoding="latin").read().lower()
    words = re.sub(r'[^\w\s]','', words)
    words = re.sub(r'\d+','', words).split(" ")
    stop_words = stopwords.words('english')
    words = [word for word in words if word not in stop_words]
    ngram_counts = Counter(ngrams(words, 3))
    print(ngram_counts.most_common(200))
    with open(outputFile, 'w') as f:
        for key in ngram_counts.keys():
            f.write("%s,%s\n"%(key,ngram_counts[key]))
 
def Ngrams(partition,data,outputFile):
    words = open(data,encoding="utf8").read().lower()
    words = re.sub(r'[^\w\s]','', words)
    words = re.sub(r'\d+','', words).split(" ")
    stop_words = stopwords.words('english')
    words = [word for word in words if word not in stop_words]
    ngram_counts = Counter(ngrams(words, partition))
    print(ngram_counts.most_common(200))
    with open(outputFile, 'w') as f:
        for key in ngram_counts.keys():
            f.write("%s,%s\n"%(key,ngram_counts[key]))
    
if __name__ == "__main__":
   
    #enter your input & output file path in csv format preferably.
    data = r''
    outputFile = ''
    
    userinput = input("How would you like to partition the data?\n (Unigrams, Bigrams, Trigrams, Ngrams)")
   
    if userinput == 'Unigrams':
        Unigrams(data,outputFile)  
            
    if userinput == 'Bigrams':
        Bigrams(data,outputFile)
                             
    if userinput == 'Trigrams':
        Trigrams(data,outputFile)
               
    if userinput == 'Ngrams':
        partition = int(input("Ngram value?"))
        Ngrams(partition,data,outputFile)
