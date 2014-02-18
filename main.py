import os
import json
from collections import Counter

import nltk
from nltk.stem import WordNetLemmatizer

from utils import get_high_frequency_words
from utils import cleanse

wnl = WordNetLemmatizer()
words = map(wnl.lemmatize, list(get_high_frequency_words()))
words_set = set(words)

def get_words_freq(corpus): # book
    record = {}
    corpus = map(wnl.lemmatize, corpus)
    counter = Counter(corpus)
    corpus_set = set(corpus)
    record['book'] = book
    record['count'] = len(corpus_set & words_set)
    record['terms'] = [{'term': word, 'frequency': counter[word]} for word in corpus_set & words_set]
    return record

def gen_word_freq_classics():
    # this function is responsible for getting GRE words frequency for the 
    # classic books stored inside ./classics directory
    #
    # corpus = get_cleaned(open('classics/'+book).read()).split()
    # result = [get_words_freq(book) for book in os.listdir('classics/')]
    result = []
    for book in os.listdir('classics/'):
        corpus = get_cleaned(open('classics/'+book).read()).split()
        result.append(get_words_freq(corpus))
    return result

result = gen_freq_classics()
result = sorted(result, key=lambda x: x['count'], reverse=True)
with open('output-wnl.json', 'w') as f:
    f.write(json.dumps(result, indent=4))

words_freq =[{'book': o['book'], 'count': o['count']} for o in result]
with open('wordsfrequency.json', 'w') as f:
    f.write(json.dumps(words_freq, indent=4))

# d = json.loads(open('output.json').read())
# sorted(d, key=lambda x: x['count'], reverse=True)