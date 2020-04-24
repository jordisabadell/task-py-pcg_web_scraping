from bs4 import BeautifulSoup #https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from utils import getUrlBase, getUrlParams, removeNumberOfItems, getUrlDomain, trim
import requests

# Scraping index page. Return list of URLs to scraping
#
# @params url:string
# @return dictionary
def scrapingIndex(url):

    urls = {}

    if not url:
        print("Error: URL is empty.")
        return ""

    #get URL content
    req = requests.get(url)

    statusCode = req.status_code
    if statusCode == 200:
        print("Get URL", url, statusCode, "OK")
        html = BeautifulSoup(req.text, "html.parser")

        #<div class="caixa-enllacos">
        #   <div class="FW_BoxSimple">
        #       <h3>Title of section (nº of iterms)</h3>
        #   </div>
        #   <ul>
        #       <li>
        #           <a href=""></a>
        #       </li>
        #   </ul>
        #</div>
        contents = html.find_all('div', 'caixa-enllacos')
        for content in contents:
            
            title = content.find('h3')
            if title:
                anchor = content.find('a')
                if anchor:
                    title = trim(removeNumberOfItems(anchor.getText()))
        
            if title:
                lis = content.find_all('li')
                for li in lis:
                    anchor = li.find('a')
                    if anchor:
                        href = getUrlDomain(url) + anchor.get('href')
                        subtitle = trim(removeNumberOfItems(anchor.getText()))

                        #add item to dictionary of urls
                        urls[title + "\t" + subtitle] = href 

    return urls