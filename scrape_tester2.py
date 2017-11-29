import urllib3, random
from bs4 import BeautifulSoup
from lib import game_word
from parsers import urban_dictionary

#quote_page = "https://www.urbandictionary.com/define.php?term=turkey%20hole"
quote_page = "https://www.urbandictionary.com/"
page_num_str = "?page="

http = urllib3.PoolManager()
req = http.request("GET", quote_page)
page_data = req.data

#Hey, we need the maximum number of pages of UDic Entries
max_pages = urban_dictionary.get_max_pages(page_data)
print("The max Number of Pages: {}".format(str(max_pages)))

#Ok great, lets pick a few random ones...
#Lets get X random Questions
pages_to_grab=random.sample(range(max_pages), 2)
print("Grabbing Pages..." + str(pages_to_grab))

#great now lets
for i in range(len(pages_to_grab)):
    new_page_url = quote_page + page_num_str + str(pages_to_grab[i])
    print("Grabbing from this url: " + new_page_url)
    new_req = http.request("GET", new_page_url)
    new_page_data = new_req.data
    urban_dictionary_words = urban_dictionary.get_words_from_ud_page(new_page_data)

    for urban_dictionary_word in urban_dictionary_words:
        print("*****************************************************************")
        print("Word: {}\r".format(urban_dictionary_word.word))
        print("Meaning: {}\r".format(urban_dictionary_word.meaning))
        print("Example: {}\r".format(urban_dictionary_word.example))
    #print("Word: {}\rMeaning: {}\rExample: {}\r".format(urban_dictionary_word.word, urban_dictionary_word.meaning, urban_dictionary_word.example))
