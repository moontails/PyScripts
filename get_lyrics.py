#!/usr/bin/python

#####################
# argument 1 - Song Name, arguement 2 - Band Name
# example uasge - 
#         python get_lyrics.py "worth fighting for" "judas priest"
#####################

import sys
import re
from urllib2 import urlopen
from bs4 import BeautifulSoup

song_name = ""
band_name = ""

def get_lyrics(song,band):

    # Constructing the url to fetch lyrics from
    
    lyrics_url = "http://www.azlyrics.com/lyrics/" + band.replace(" ","") + "/" + song.replace(" ", "") + ".html"
    
    #print lyrics_url + "\n"

    try:
        
        # Open and read the page
        
        page = urlopen(lyrics_url)
        html = page.read()
        
        #Find the starting and ending indices for the lyrics
        
        startindex = html.find("<!-- start of lyrics -->") + len("<!-- start of lyrics -->")
        endindex = html.find("<!-- end of lyrics -->") - len("<!-- end of lyrics -->")
        
        # Slicing to get the lyrics
        
        lyrics = html[startindex:endindex]
        
        # Soupifying the page for better display
        
        soup = BeautifulSoup(lyrics)
        print "\nHere is the lyrics for " + song.upper() + " by " + band.upper() + "\n"
        print soup.get_text()
        
    except:
        
        # Printing error message
        print "\nSorry " + song.upper() + " by " + band.upper() + " NOT FOUND\n"

def main():
    song_name = sys.argv[1]
    band_name = sys.argv[2]
    get_lyrics( song_name, band_name)

main()
