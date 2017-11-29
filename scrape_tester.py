import urllib3
from bs4 import BeautifulSoup
from lib import game_word
from parsers import urban_dictionary

#quote_page = "https://www.urbandictionary.com/define.php?term=turkey%20hole"
quote_page = "https://www.urbandictionary.com/"
http = urllib3.PoolManager()
req = http.request("GET", quote_page)
page_data = req.data
print("Got Page Data...")

#urban_dictionary_word = game_word.GameWord()
print("Got Game World...")
urban_dictionary_words = urban_dictionary.get_words_from_ud_page(page_data)

for urban_dictionary_word in urban_dictionary_words:
    print("*****************************************************************")
    print("Word: {}\r".format(urban_dictionary_word.word))
    print("Meaning: {}\r".format(urban_dictionary_word.meaning))
    print("Example: {}\r".format(urban_dictionary_word.example))

    #print("Word: {}\rMeaning: {}\rExample: {}\r".format(urban_dictionary_word.word, urban_dictionary_word.meaning, urban_dictionary_word.example))
