# /bin/python

import re
import json
from string import Template

import requests
from bs4 import BeautifulSoup

def dowload_top_100():
    '''This script will download Top 100 books of last 30 days from Project 
    Gutenberg and saves them with appropriate file name'''
    base_url = Template('http://www.gutenberg.org/files/$book_id/$book_id.txt')
    r = requests.get('http://www.gutenberg.org/browse/scores/top')
    soup = BeautifulSoup(r.text)
    h2 = soup.find(id='books-last30')
    ol = h2.next_sibling.next_sibling
    for a_tag in ol.find_all('a'):
        m = re.match(r'(.*)(\(\d+\))', a_tag.text)
        file_name = m.group(1).strip()
        m = re.match(r'/ebooks/(\d+)', a_tag.get('href'))
        book_id = m.group(1)
        url = base_url.substitute(book_id=book_id)
        r = requests.get(url)
        if r.status_code == requests.codes.ok:
            #print 'Downloaded... ', file_name
            f = open(file_name, 'w')
            f.write(r.text.encode('UTF-8'))
            f.close()

def get_cleaned(text_corpus):
    '''Removes all the punctuation and special characters from corpus'''
    return re.sub(r'[^\w-]', ' ', text_corpus)

def get_high_frequency_words():
    hf_words = json.loads(open('hf_words.json').read())
    for record in hf_words:
        yield record['term']

if __name__ == '__main__':
    dowload_top_100()