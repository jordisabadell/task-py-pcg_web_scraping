from bs4 import BeautifulSoup #https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from content import scrapingContent
from utils import getUrlBase, getUrlParams, removeNumberOfItems, getUrlDomain, trim, getUrlDomain
import requests

# Scraping list page. Return content.
#
# @param url:string
# @param prefix:string
# @return string
def scrapingList(url, prefix):

    sb = "" # return result

    if not url:
        print("Error: URL is empty.")
        return ""

    #get URL content
    req = requests.get(url)

    statusCode = req.status_code
    if statusCode == 200:
        print("Get URL", url, statusCode, "OK")
        html = BeautifulSoup(req.text, "html.parser")

        #<dt>
        #   <a href="Link">Title</a>
        #</dt>
        #<dd>
        #   String
        #</dd>
        contents = html.find_all(['dt', 'dd'])
        for content in contents:
            if content.name=="dt":
                anchor = content.find('a')
                href = getUrlBase(url) + anchor.get('href')
                title = trim(anchor.getText())
                id_ = getUrlParams(href)

                sb = sb + prefix + "\t" + id_["idDoc"] + "\t" + title + "\t" + href

                sb = sb + "\t" + scrapingContent(href)
            else: #dd
                date = trim(content.getText())
                if ":" in date: #Some text: 01/01/2020 00:00h
                    date = trim(date[date.find(":")+1:len(date)])
                if "h" in date: #01/01/2020 00:00h
                    date = trim(date.replace("h", ""))

                sb = sb + "\t" + date + "\n"

        #<tr>
        #   <td><a href="...">1</a></td>
        #   <td><a href="...">2</a></td>
        #   <td><a href="...">Següent</a></td> <-- Link to iterate.
        #   <td><a href="...">Anterior</a></td>
        #</tr>
        navLinks = html.find_all('td')            
        for navLink in navLinks:
            link = navLink.find('a')
            text = link.getText().strip()
            href = link.get('href')

            href = getUrlBase(url) + trim(href)

            if 'Següent' in text:
                sb = sb + scrapingList(href, prefix)
    else:
        print("Error: Can't get URL ", statusCode)
    
    return sb