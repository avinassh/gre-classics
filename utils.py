# /bin/python

import re
import requests
import json

def get_cleaned(text_corpus):
    '''Removes all the punctuation and special characters from corpus'''
    #pattern = re.compile(r'[.,:;'"!?]')
    pass

def get_high_frequency_words():
    hf_words = json.loads(open('hf_words.json').read())
    for record in hf_words:
        yield record['term']

if __name__ == '__main__':
    pass