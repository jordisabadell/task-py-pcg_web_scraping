from bs4 import BeautifulSoup #https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from scraping_utils import *
import requests

# Scraping list URL. Return content.
#
# @param url:string
# @param currentIteration: int
# @param maxIterations: int
# @return string
def scrapingList(url, currentIteration, maxIterations):

    sb = "" # return result

    if not url:
        print("Error: URL is empty.")
        return ""
    
    if currentIteration>=maxIterations:
        print("Stop process by reaching the maximum number of iterations.")
        return ""

    if currentIteration==0:
        sb = "Num\tId\tDescription\tLink\tDate update\n"

    #get URL content
    req = requests.get(url)

    statusCode = req.status_code
    if statusCode == 200:
        print("Iteration", currentIteration ,"Get URL", url, statusCode, "OK")
        html = BeautifulSoup(req.text, "html.parser")

        #<dt>
        #   <a href="Link">Title</a>
        #</dt>
        #<dd>
        #   String
        #</dd>
        contents = html.find_all(['dt', 'dd'])
        for i, content in enumerate(contents):
            if content.name=="dt":
                anchor = content.find('a')
                href = getUrlBase(url) + anchor.get('href')
                title = trim(anchor.getText())
                id_ = getUrlParams(href)

                sb = sb + str((currentIteration*10 + int(i/2) + 1)) + "\t" + \
                 id_["idDoc"] + "\t" + title + "\t" + href
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
        for j, navLink in enumerate(navLinks):
            link = navLink.find('a')
            text = link.getText().strip()
            href = link.get('href')

            href = getUrlBase(url) + trim(href)

            if 'Següent' in text:
                sb = sb + scrapingList(href, currentIteration+1, maxIterations)
    else:
        print("Error: Can't get URL ", statusCode)
    
    return sb