import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('punkr_tab')
nltk.download('averaged_perceptron_tagger_eng')
from nltk import pos_tag
def pos_tagging(sentence):
    words=word_tokenize(sentence)
    pos_tags=pos_tag(words)
    return pos_tags
sentence="The cat sat on the mat"
tags=pos_tagging(sentence)
print(tags)
