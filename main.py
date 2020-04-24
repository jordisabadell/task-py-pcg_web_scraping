from list import scrapingList
from index import scrapingIndex
import sys
import os
import codecs
import json

#configuration params
#-----------

INPUT_FILE = "urls_to_scrape_TEST.json"
OUTPUT_DIRECTORY = "c:/tmp/"
CSV_HEADER = "Prefix-1\tPrefix-2\tId\tDescription\tLink\tDate update\n"

#!~end of configuration params


#open configuration file and iterate urls
items = json.load(open(INPUT_FILE, "r", encoding="utf8"))
for item in items:
    sb = ""
    
    #scraping index page from main url
    urls = scrapingIndex(item["url"])

    #scraping list of urls    
    for prefix in urls:
        sb = sb + scrapingList(urls[prefix], prefix)

    #add header row
    sb = CSV_HEADER + sb

    #remove file if exists
    if os.path.exists(item["file"]):
        os.remove(item["file"])
    
    #wirte output file
    if not OUTPUT_DIRECTORY.endswith("/"):
        outputFile = OUTPUT_DIRECTORY + "/" + item["file"]
    else:  
        outputFile = OUTPUT_DIRECTORY + item["file"]
    f = codecs.open(outputFile, "a", "utf-8")
    f.write(sb)
    f.close()