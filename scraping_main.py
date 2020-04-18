from scraping_list import scrapingList
import sys
import os
import codecs

#validate nº args
if len(sys.argv)<2:
    print("Insufficient number of arguments.")
    exit()

#get arg1
url = sys.argv[1]
if not url or 'http' not in url:
    print("Invald URL:", url)
    exit()

#get arg2 (optional)
if len(sys.argv)>=3:
    fileName = sys.argv[2]
else:
    fileName = ""

#scraping list
sb = scrapingList(url, 0, 100) #url, currentIteration, maxIterations

#print output result
if fileName:
    #remove file
    if os.path.exists(fileName):
        os.remove(fileName)
    #wirte
    f = codecs.open(fileName, "a", "utf-8")
    f.write(sb)
    f.close()
else: #output screen
    print(sb)