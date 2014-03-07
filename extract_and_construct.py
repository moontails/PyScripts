#!/usr/bin/python

#####################
# The "org.html" contains the org hierarchy.
# Also you need to have Beautiful Soup installed to make life easier for yourself
#####################

from bs4 import BeautifulSoup

def getimageurl():

    #Open the html file
    fd =open("org.html")

    #Soupify it
    soup = BeautifulSoup(fd)

    print "\nBeginning construction of the link\n"

    #extract all the hrefs, split to get username and construct the img link

    fd1=open('imglink', 'w+')
    for link in soup.find_all('a'):
        a,uname=link.get('href').split("=")
        fd1.write("start_of_link"+uname.rstrip()+".jpg"+"\n")

    #closing the fd's
    fd.close()
    fd1.close()

    print "\nDone\n"

def main():
    getimageurl()

main()
