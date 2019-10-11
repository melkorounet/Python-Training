import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('.', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


# start coding

def load_words():
    """Load the words dictionary (DICTIONARY constant) into a list and return it"""
    dico = open(DICTIONARY)
    words=list(dico)
    return words


def calc_word_value(word):
    """Given a word calculate its value using the LETTER_SCORES dict"""
    word = word.upper()
    word_value = 0
    for letter in word :
        if letter not in LETTER_SCORES.keys():
            word_value += 0
        else:
            word_value += LETTER_SCORES[letter]
    print(word_value)
    pass


def max_word_value(words):
    """Given a list of words calculate the word with the maximum value and return it"""
    pass

#print(LETTER_SCORES)
#load_words()

calc_word_value("benzalphenylhydrazone")