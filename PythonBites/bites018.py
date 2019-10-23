import os
import urllib.request
import re
from collections import Counter

# data provided
stopwords_file = os.path.join('.', 'stopwords')
harry_text = os.path.join('.', 'harry')
urllib.request.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)
urllib.request.urlretrieve('http://bit.ly/2C6RzuR', harry_text)


def get_harry_most_common_word():
    pass

with open(stopwords_file) as f:
    stopwords=f.read().lower()

with open(harry_text, encoding="utf8") as texte:
    regex = re.compile('[^a-zA-Z ]')
    word=[]
    harry_potter=regex.sub('', texte.read().lower().replace('\n', ' '))
    harry_potter=harry_potter.split(' ')
    #print(harry_potter)
    for words in harry_potter:
        if words not in stopwords:
            word.append(words)    
    most_used_word = Counter(word).most_common(1)
    print(type(most_used_word[0]))