import requests
from bs4 import BeautifulSoup
import operator

def Req(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    for content in soup.findAll('a', {'class' : 'h5 text-black d-block py-2'}):
        sentences = content.string
        words = sentences.lower().split()
        for each_word in words:
            # print(each_word)
            word_list.append(each_word)
    clean_up_list(word_list)

def clean_up_list(word_list):
    cleaned_word_list = []
    for word in word_list:
        clean_these = "!@#$%^&*()_-+=;:[]{}/\"?"
        for x in range(0, len(clean_these)):
            word = word.replace(clean_these[x], "")
        if len(word) > 0:
            # print(word)
            cleaned_word_list.append(word)
    create_dict(cleaned_word_list)

def create_dict(cleaned_word_list):
    word_count = {}
    for word in cleaned_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for x, y in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(x, y)




Req('https://storygrid.com/love-genre/')