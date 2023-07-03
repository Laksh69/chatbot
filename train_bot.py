#Text Data Preprocessing Lib
import nltk
nltk.download("punkt")
from nltk.stem import PorterStemmer
stemer= PorterStemmer()
import json
import pickle
import numpy as np

words = []
classes = []
word_tags_list= []
ignore_words=["?","!",",",".","'s","m"]
train_data_file= open("intents.json").read()
intents=json.loads(train_data_file)


# function for appending stem words
def getStemWords(words,ignoreWords):
        stemwords=[]
        for word in words:
                if word not in ignoreWords:
                        w = stemer.stem(word.lower())
                        stemwords.append(w)
        return stemwords

for intent in intents ['intents']:
        for pattern in intent ["patterns"]:
                patternWord=nltk.word_tokenize(pattern)
                words.extend(patternWord)
                word_tags_list.append(patternWord,intent['tag'])
        if intent['tag'] not in classes:
                classes.append(intent["tag"])
                stemWords= getStemWords(words,ignore_words)

print(stemWords)
print(classes)
print(word_tags_list [0])




    
        # Add all words of patterns to list
        
        # Add all tags to the classes list
         

#Create word corpus for chatbot

