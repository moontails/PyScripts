from urllib import urlopen
from bs4 import BeautifulSoup
import itertools
import re
import HTMLParser
import unicodedata
import time
import datetime

try:
	#get the page here
	ld2=[]
	ld3=[]
	
	start_time=time.time()
	
	#The seed url. This will act as the starting point to start the focussed crawling.
	seedlink="http://ibnlive.in.com/sports/"
	seedpage_html=urlopen(seedlink).read()
	
	#Need to Collect a few seed pages
	soupify=BeautifulSoup(seedpage_html)

	#empty list to hold candidate pages
	candidate_links=[]
	candidate_links_dict={}
	
	#a double dict to hold data of the form { {link1:{word1:TF word2:TF}} {link2:{word1:TF}} }
	dd={}
	print "Opening SeedURL and extracting links from it"
	
	#extracting all the links from a page
	for link in soupify.find_all('a'):
		try:
			if(link.get('href').startswith("http")):
				candidate_links.append(link.get('href'))
		except:
			pass

	candidate_links=list(set(candidate_links))
	print "\nNumber of links crawled in Depth1: " + repr(len(candidate_links))
	
	#also storing in a dict to keep track of inlink count which is calculated next
	#candidate_links_dict.update({seedlink:1})
	for link in candidate_links:
		candidate_links_dict.update({link:1})
		dd[link]={}

	#get the words from textfile and build our own corpus
	#SportsWords.txt contains the domain relevant words and SportsSeedURL.txt contains few links which can serve as seed url
	
	wordslist=open('SportsWords.txt','r').read()
	words=wordslist.split()
	SeedURLS=open('SportsSeedURL.txt','r').read()
	seeds=SeedURLS.split()
	outlinkcount={}
	
	for link in candidate_links:
		outlinkcount.update({link:1})
	print "Corpus list built successfully\nStarting Depth1 Crawling"

	#Depth 1 Crawling
	for crawl_candidate in candidate_links:
		try:	
			print "\nStarting Crawling of " + crawl_candidate
			crawled_html=urlopen(crawl_candidate).read()
			print "Reading the contents of the page of " + crawl_candidate
			souped=BeautifulSoup(crawled_html)
			print "Normalising data - Converting Unicode data to ASCII"
			page_text=""
			for string in souped.stripped_strings:
				page_text=page_text+string
			page_text=page_text=unicodedata.normalize('NFKD',page_text).encode('ascii','ignore')
			page_words=[]
			page_words=page_text.split()
			wdict={}
			for word in words:
				wdict[word]=0	
			frequency=0
			print "Computing Frequency Count"
			for word in page_words:
				if word in words:
					frequency+=1
				if word in wdict:
					temp=wdict[word]
					temp+=1
					wdict[word]=temp
			print "Finished computing frequency count"
			for i in wdict:
				if wdict[i]>0:
					dd[crawl_candidate][i]=wdict[i]
			crawl_temp=[]
			#read the links in each individual link now.
			print "Frequency Count is " + repr(frequency)
			if(frequency>0):
				for link in souped.find_all('a'):
					try:
						if(link.get('href').startswith("http")):
							crawl_temp.append(link.get('href'))
					except:
						pass
				print "Finished crawling at depth 1, now getting depth 2 links"
				crawl_temp=list(set(crawl_temp))
				for more in crawl_temp:
					ld2.append(more)				
				  #Now update the links in the dict be checking
				print "Calculating inlink and outlink count"
				for link in crawl_temp:
					if link in candidate_links_dict.keys():
						#get the inlink count first and then increment it
						count=candidate_links_dict[link]
						count+=1
						candidate_links_dict[link]=count
					else:
						#Else update that is add the link to the dict
						candidate_links_dict.update({link:1})
					#if link in seeds:
					#	count=outlinkcount[crawl_candidate]
					#	count+=1
					#	outlinkcount[crawl_candidate]=count
			else:
				print crawl_candidate+" Does not belong to domain"
			
			del crawl_temp
			del page_words
			del page_text
			del wdict
		except:	
			print "Could not open " + crawl_candidate

	print "\nNumber of links crawled in Depth1: " + repr(len(candidate_links))
	end_time=time.time()
	print "\nTime taken to crawl Depth 1 is: " + str(datetime.timedelta(seconds=(end_time-start_time)))
#	print "Calculating Outlink Count\n"
	ld2=list(set(ld2))
	print "Starting Depth2 Crawling\n"
	start_time=time.time()
	
	#Depth 2 Crawling
	for crawl_candidate in ld2:
		try:	
			print "\nStarting Crawling of " + crawl_candidate
			crawled_html=urlopen(crawl_candidate).read()
			print "Reading the contents of the page of " + crawl_candidate
			souped=BeautifulSoup(crawled_html)
			print "Normalising data - Converting Unicode data to ASCII"
			page_text=""
			for string in souped.stripped_strings:
				page_text=page_text+string
			page_text=page_text=unicodedata.normalize('NFKD',page_text).encode('ascii','ignore')
			page_words=[]
			page_words=page_text.split()
			wdict={}
			for word in words:
				wdict[word]=0	
			frequency=0
			print "Computing frequency count"
			for word in page_words:
				if word in words:
					frequency+=1
				if word in wdict:
					temp=wdict[word]
					temp+=1
					wdict[word]=temp
			print "Finished computing frequency count"
			for i in wdict:
				if wdict[i]>0:
					dd[crawl_candidate][i]=wdict[i]
			crawl_temp=[]
			#read the links in each individual link now.
			#pdb.set_trace()
			print "Frequency count is " + repr(frequency)
			if(frequency>0):
				for link in souped.find_all('a'):
					try:
						if(link.get('href').startswith("http")):
							crawl_temp.append(link.get('href'))
					except:
						pass
				print "Finished crawling at depth 2, now getting depth 3 links"
				crawl_temp=list(set(crawl_temp))
				for more in crawl_temp: 
					ld3.append(more)				
				  #Now update the links in the dict be checking
				print "Calculating inlink and outlink count"
				for link in crawl_temp:
					if link in candidate_links_dict.keys():
						#get the inlink count first and then increment it
						count=candidate_links_dict[link]
						count+=1
						candidate_links_dict[link]=count
					else:
						#Else update that is add the link to the dict
						candidate_links_dict.update({link:1})
					#if link in seeds:
					#	count=outlinkcount[crawl_candidate]
					#	count+=1
					#	outlinkcount[crawl_candidate]=count
			else:
				print crawl_candidate+" Does not belong to domain"
			
			del crawl_temp
			del page_words
			del page_text
			del wdict
		except:	
			pass
			#print "Could not open " + crawl_candidate
	
	print "\nNumber of links crawled in Depth 2: " + repr(len(ld2))
	end_time=time.time()
	print "\nTime taken to crawl Depth 2 is: " + str(datetime.timedelta(seconds=(end_time-start_time)))
	#print "Calculating Outlink Count\n"
	ld3=list(set(ld3))
	
	print "\nWriting to Flat file"
	for key in dd.keys():
		tempd=dd[key]
		for i in tempd.keys():
			with open("Word/"+i+".txt","a") as outfile:
				#Printing to file: <link> <TF> <inlink_count>
				outfile.write(key+" " + repr(tempd[i])+ " " + repr(candidate_links_dict[key]) + "\n")

except:
	print "\nCannot Open SeedURL\n"
