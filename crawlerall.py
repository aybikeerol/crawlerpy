import requests
from bs4 import BeautifulSoup
import re
import operator
from collections import Counter


def start(url):
	wordlist = []
	source_code = requests.get(url).text

	soup = BeautifulSoup(source_code, 'html.parser')

	for each_text in soup.findAll('div', {'class':'g'}):


		content = each_text.text
		words = content.lower().split()

		for each_word in words:
			wordlist.append(each_word)
		clean_wordlist(wordlist)


# Function removes any unwanted symbols
def clean_wordlist(wordlist):

	clean_list =[]
	for word in wordlist:
		symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '

		for i in range (0, len(symbols)):
			word = word.replace(symbols[i], '')

		if len(word) > 0:
			clean_list.append(word)
	create_dictionary(clean_list)

def create_dictionary(clean_list):
	word_count = {}

	for word in clean_list:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1

	c = Counter(word_count)
	top = c.most_common(2)
	print(top)

if __name__ == '__main__':
	start("http://www.google.com/search?q=cyberpropaganda")

def getAllLinks(soup):
    urls = []
    for item in soup.findAll('div',{'class':'g'}):
        link = item.find("a")
#div g dediğim her bir arama sonucu
        # arama sonuçlarının linki
        try:
            href = link['href']
            href = href.split("/url?q=")[1]
            urls.append(href)
            new_url = requests.get(href)
            newSoup = BeautifulSoup(new_url.text, "lxml")
            for link in newSoup.findAll("a"):
                print(link)
            # data of all the website

        except:

            pass

    return urls

def crawlGooglePages():
    search_word= "cyberpropaganda"
    base = "http://www.google.com"
    url = "http://www.google.com/search?q="+ search_word

    #requests.get ile istekte bulunduk,istekte bulunduğumuz bağlantıya ait bütün bilgilere new_url nesnesi üzerinden erişebiliriz.
           # newSoup = BeautifulSoup(new_url.text, "lxml")
            # data of all the website
    getting_url = requests.get(url)
    soup = BeautifulSoup(getting_url.text, "lxml")
    footerPageUrls = soup.find('table',{'id':'nav'})
    #arama sayfaları gezmeyi sağlıyor  1>2>3 ...
    Counter()
    pageUrls = []

    for link in footerPageUrls.findAll("a"):
        pageUrls.append(link['href'])

    return pageUrls

pageUrls = crawlGooglePages()
base = "http://www.google.com"
allUrls = {}
page = 1
for pageLink in pageUrls:

    getting_url = requests.get(base+pageLink)
    soup = BeautifulSoup(getting_url.text, "lxml")
    pageUrls = getAllLinks(soup)
    allUrls["page-"+str(page)] = pageUrls
    page+=1



