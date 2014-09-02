#!/usr/bin/python

#####################
# Also you need to have Beautiful Soup installed to make life easier for yourself
#####################

from urllib.request import urlopen,urlretrieve
from bs4 import BeautifulSoup

def getnotes(url):

    #Open the html file
    page = urlopen(url)

    #Soupify it
    soup = BeautifulSoup(page)
    
    print "\nBeginning construction of the link\n"
	
	lect = []
    #extract all the hrefs for the presentations and pdfs
    for link in soup.find_all('a'):
        if ".pptx" in link.get('href'):
			lect.append(link.get('href'))

	#store the base of the url
	base_url="http://l2r.cs.uiuc.edu/~danr/Teaching/CS446-14/"
    for x in lect:
		urlretrieve(base_url+x)

    print "\nFinished processing - Links stores in file 'imglink'\n"

def main():
	#The main url for the class
	url="http://l2r.cs.uiuc.edu/~danr/Teaching/CS446-14/lectures.html"
    getnotes()

main()
