#Parses an Urban Dictionary Page and returns the Word and the main definition
import urllib3, re
from bs4 import BeautifulSoup
from lib import game_word

def get_words_from_ud_page(page_data):
    soup = BeautifulSoup(page_data, 'html.parser')

    ud_words = []

    for container in soup.find_all("div", attrs={"class": "def-panel"}):
        word_container = container.find('a', attrs={"class": "word"})
        word = word_container.text
        print(word)

        meaning_container = container.find('div', attrs={"class": "meaning"})
        meaning = meaning_container.text
        example_container = container.find('div', attrs={"class": "example"})
        example = example_container.text
        ud_word = game_word.GameWord()
        ud_word.word = word
        ud_word.meaning = meaning
        ud_word.example = example
        ud_words.append(ud_word)
    #return ud_word
    return ud_words

def get_max_pages(page_data):
    soup = BeautifulSoup(page_data, 'html.parser')
    last_page_container = soup.find('a', text="Last »")

    href = last_page_container['href']
    max_pages = _get_number_from_url(href)
    return max_pages

def _get_number_from_url(url_str):
    strang = re.search(r'\d+$', url_str)
    print(strang.group(0))
    return int(strang.group(0))
    #return int(strang.group(1)) if strang else None
