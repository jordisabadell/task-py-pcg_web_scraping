import sys
import os
import codecs
import json
import argparse
from list import scrapingList
from index import scrapingIndex

#CONSTANTS
CSV_HEADER = "Prefix-1\tPrefix-2\tId\tDescription\tLink\tDate update\n"

#ARGUMENTS
parser = argparse.ArgumentParser(description='Given a list of URLs of P.C.G web, it scrapes the content and save it to CSV file/s. It needs a configuration JSON file with URLs and output file/s name.')
parser.add_argument('--inputfile', dest='input_file', 
    help='Input file name with configuration (i.e: \'urls_to_scrape.json\').', type=str, required=True)
parser.add_argument('--outputfolder', dest='output_folder', 
    help='Output folder name (i.e: \'c:/tmp/\').', type=str, required=True)

args = parser.parse_args()
inputFileName = args.input_file
outputFolderName = args.output_folder

#EXECUTE
#open configuration file and iterate urls
items = json.load(open(inputFileName, "r", encoding="utf8"))
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
    if not outputFolderName.endswith("/"):
        outputFile = outputFolderName + "/" + item["file"]
    else:  
        outputFile = outputFolderName + item["file"]
    f = codecs.open(outputFile, "a", "utf-8")
    f.write(sb)
    f.close()

print("Done.")
