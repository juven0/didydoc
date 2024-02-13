import nltk 
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from os import walk
from os import path

class Parser:
    def __init__(self, vocabulaire) -> None:
        self.vocabulaire = vocabulaire

    def tokenizer(self, data):
        key_words = []
        vocabulaireTags = ['VB', 'VBG','NN', 'NNS','VBP', 'VBZ']
        stop_words = set(stopwords.words("french"))
        text  = nltk.word_tokenize(data)
        filtered_list = []
        for word in text:
            if word.lower() not in stop_words and word.isalpha() and len(word) > 1:
                filtered_list.append(word.lower())
        text_with_tag = nltk.pos_tag(filtered_list)
        for word_tag in text_with_tag:
            if (word_tag[1] in vocabulaireTags):
                key_words.append(word_tag[0])
        return key_words
    
    def parser(self, key_words):
        vocabulaireLen = len(self.vocabulaire)
        tmpArray = [0]*(vocabulaireLen-1)
        for w in key_words:
            try:
                wIndex =self.vocabulaire.index(w.lower())
                tmpArray[wIndex] = 1
            except:
                pass
        return tmpArray
