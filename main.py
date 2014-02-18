import os
import json
from collections import Counter

import nltk
from nltk.stem import WordNetLemmatizer

from utils import get_high_frequency_words
from utils import get_cleaned

wnl = WordNetLemmatizer()
words = map(wnl.lemmatize, list(get_high_frequency_words()))
words_set = set(words)

def get_freq_record(book):
    record = {}
    corpus = get_cleaned(open('classics/'+book).read()).split()
    corpus = map(wnl.lemmatize, corpus)
    counter = Counter(corpus)
    corpus_set = set(corpus)
    record['book'] = book
    record['count'] = len(corpus_set & words_set)
    record['terms'] = [{'term': word, 'frequency': counter[word]} for word in corpus_set & words_set]
    return record

result = [get_freq_record(book) for book in os.listdir('classics/')]
result = sorted(result, key=lambda x: x['count'], reverse=True)
with open('output-wnl.json', 'w') as f:
    f.write(json.dumps(result, indent=4))

words_freq =[{'book': o['book'], 'count': o['count']} for o in result]
with open('wordsfrequency.json', 'w') as f:
    f.write(json.dumps(words_freq, indent=4))

# d = json.loads(open('output.json').read())
# sorted(d, key=lambda x: x['count'], reverse=True)