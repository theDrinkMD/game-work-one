#Parses an Urban Dictionary Page and returns the Word and the main definition
import urllib3
from bs4 import BeautifulSoup
from lib import game_word

def getUdPageInfo(page_data):
    soup = BeautifulSoup(page_data, 'html.parser')

    #Finds First
    #word_container = soup.find('a', attrs={"class": "word"})
    #word = word_container.text
    #meaning_container = soup.find('div', attrs={"class": "meaning"})
    #meaning = meaning_container.text
    #example_container = soup.find('div', attrs={"class": "example"})
    #example = example_container.text
    #ud_word = game_word.GameWord()
    #ud_word.word = word
    #ud_word.meaning = meaning
    #ud_word.example = example

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
