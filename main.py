import os
import json
from collections import Counter

from utils import get_high_frequency_words
from utils import get_cleaned

words = list(get_high_frequency_words())
words_set = set(words)

def get_freq_record(book):
    record = {}
    corpus = get_cleaned(open('classics/'+book).read()).split()
    counter = Counter(corpus)
    corpus_set = set(corpus)
    record['book'] = book
    record['count'] = len(corpus_set & words_set)
    record['terms'] = [{'term': word, 'frequency': counter[word]} for word in corpus_set & words_set]
    return record

result = [get_freq_record(book) for book in os.listdir('classics/')]
f = open('output.json', 'w')
f.write(json.dumps(result, indent=4, sort_keys=True))
f.close()