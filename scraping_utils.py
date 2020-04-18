# Get parameters of URL. Returns dictionary of parameters.
# For example:
#   Input:  http://www.server-name.com/index.html?t=202004171629&p=1
#   Output: {
#       "t": "202004171629",
#       "p": "1"
#   }
#
# @param url:string
# @return dictionary {param1:value1, param2:value2}
def getUrlParams(url):
    
    #no params
    if not url or not '?' in url:
        return {}

    #exists '?' but parameters string is empty
    values = url.split("?")[1]
    if len(values) <= 0:
        return {}

    #get params
    params = {}
    for value in values.split("&"):
        
        if not '=' in value: #it hasn't value
            params[value] = ''
        else:
            key_value = value.split("=")
            params[key_value[0]] = key_value[1]

    return params


# Get URL without filename and parameters.
# For example:
#   Input:  http://www.server-name.com/index.html?t=202004171629&p=1
#   Output: http://www.server-name.com/
#   
# @param url:string
# @return string
def getUrlBase(url):

    #no url
    if not url:
        return ""

    #no params
    if not '?' in url:
        return url

    #get url protocol like http, https, ...
    protocol = url[0:url.find("://")+3]

    #remove protocol
    url = url.replace(protocol, "")

    #remove params
    url = url.split("?")[0] 

    #url hasn't path
    if url.rfind("/")<=0:
        return protocol+url

    #get filename
    filename = url[url.rfind("/")+1:len(url)]
    
    return protocol+url.replace(filename, "")


# Trim a string.
#
# @param string
# return string
def trim(s):
    if not s:
        return ""
    
    s = s.replace('\t', '')
    s = s.replace('\r', '')
    s = s.replace('\n', '')
    s = s.strip()
    return s