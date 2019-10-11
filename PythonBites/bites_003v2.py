import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('.', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}

test_words = ['bob', 'julian', 'pybites', 'quit', 'barbeque']

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
        word_value += 0 if letter not in LETTER_SCORES.keys() else LETTER_SCORES[letter]
    return word_value


def max_word_value(words):
    """Given a list of words calculate the word with the maximum value and return it"""
    liste = []
    for word in words :
        liste.append((calc_word_value(word), word))
        liste.sort()
    return (liste[-1][1]).strip('\n')
    pass