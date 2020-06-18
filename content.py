from bs4 import BeautifulSoup #https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from utils import getUrlBase, getUrlParams, removeNumberOfItems, getUrlDomain, trim, getUrlDomain
import requests

#
#
# @param url:string
# @return string
def scrapingContent(url):
    if not url:
        print("Error: URL is empty.")
        return ""
    
    #get URL content
    req = requests.get(url)

    statusCode = req.status_code
    if statusCode == 200:
        print("Get URL", url, statusCode, "OK")
        html = BeautifulSoup(req.text, "html.parser")
    
        #<span class="pressupost">4.050,00 € sense IVA</span>
        contents = html.find_all('span', 'pressupost')
        if len(contents)>0:
            pressupost = trim(contents[0].text.replace('€ sense IVA', ''))
        else:
            pressupost = "¿¿??"

    return pressupost