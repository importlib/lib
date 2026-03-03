from nltk.corpus import wordnet as wn
from nltk.wsd import lesk
import nltk


nltk.download('wordnet')
nltk.download('omw-1.4')

def word_disambiguation(sentence, target_word):
    words = sentence.split()  
    sense = lesk(words, target_word)
    return sense.definition() if sense else "No definition found"


sentence = "I give bat to my friend after the play"
target_word = "bat"
definition = word_disambiguation(sentence, target_word)
print(f"Word Sense Definition: {definition}")