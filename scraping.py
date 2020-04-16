from bs4 import BeautifulSoup #https://www.crummy.com/software/BeautifulSoup/bs4/doc/
import requests
import sys
import codecs

#Maximum number of pages to scrap
maxPages = 1000

def explore(url, c, fileName, iteration):

    if iteration>=maxPages:
        print("Error: The maximum number of iterations has been reached.")
        return 0

    if not url:
        print("Error: URL is empty.")
        return 0

    #Get URL
    req = requests.get(url)

    statusCode = req.status_code
    if statusCode == 200:
        print("Iteration", iteration+1 ,"Get URL", url, statusCode, "OK")
        html = BeautifulSoup(req.text, "html.parser")

        #<dt>
        #   <a href="...">Title</a>
        #</dt>
        contents = html.find_all('dt')
        for i, content in enumerate(contents):
            anchor = content.find('a')
            href = baseUrl + anchor.get('href')
            title = anchor.getText()

            #Result
            f.write(title + "\t" + href + "\n")
        
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

            href = href.replace('\r', '')
            href = href.replace('\n', '')
            href = baseUrl + href

            if 'Següent' in text:
                explore(href, baseUrl, fileName, iteration+1)
    else:
        print("Error: Can't get URL ", statusCode)
#!end function explore()

#Validate params
if len(sys.argv)<3:
    print("Insufficient number of arguments. You must define URL and output file name.")
    exit()

#arg1
url = sys.argv[1]
if not url or 'http' not in url:
    print("Invald URL:", url)
    exit()

#arg2
fileName = sys.argv[2]

#Calculate baseUrl (URL without name file and parameters)
baseUrl = url.split("?")
baseUrl = baseUrl[0][0:baseUrl[0].rfind("/")]+"/"

#Open output file
f = codecs.open(fileName, "a", "utf-8")

#Scrap URL
explore(url, baseUrl, f, 0)

#Close file
f.close()