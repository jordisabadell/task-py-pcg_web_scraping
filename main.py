from list import scrapingList
from index import scrapingIndex
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


#scraping index
urls = scrapingIndex(url)

#scraping list
sb = ""
for prefix in urls:
    sb = sb + scrapingList(urls[prefix], prefix)

#add header row
sb = "Prefix-1\tPrefix-2\tId\tDescription\tLink\tDate update\n" + sb

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