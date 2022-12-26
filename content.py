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
    
    value = ""

    #get URL content
    req = requests.get(url)

    statusCode = req.status_code
    if statusCode == 200:
        print("Get URL", url, statusCode, "OK")
        html = BeautifulSoup(req.text, "html.parser")
    
        #capçalera
        contents = html.find_all(['dt', 'dd'])
        
        organ_contractacio = ""
        codi_expedient = ""
        tipus_tramitacio = ""
        tipus_contracte = ""
        subtitpus_contracte = ""
        procediment_adjudicacio = ""
        compra_publica_innovacio = ""
        denominacio = ""
        get_next_organ_contractacio = False
        get_next_codi_expedient = False
        get_next_tipus_tramitacio = False
        get_next_tipus_contracte = False
        get_next_subtitpus_contracte = False
        get_next_procediment_adjudicacio = False
        get_next_compra_publica_innovacio = False
        get_next_denominacio = False

        for content in contents:
            if(get_next_organ_contractacio):
                organ_contractacio = trim(content.getText())
                get_next_organ_contractacio = False

            if(content.getText().find('rgan de contracta')>=0):
                get_next_organ_contractacio = True

            if(get_next_codi_expedient):
                codi_expedient = trim(content.getText())
                get_next_codi_expedient = False

            if(content.getText().find('Codi d')>=0):
                get_next_codi_expedient = True

            if(get_next_tipus_tramitacio):
                tipus_tramitacio = trim(content.getText())
                get_next_tipus_tramitacio = False

            if(content.getText().find('Tipus de tramitac')>=0):
                get_next_tipus_tramitacio = True

            if(get_next_tipus_contracte):
                tipus_contracte = trim(content.getText())
                get_next_tipus_contracte = False

            if(content.getText().find('Tipus de contracte')>=0):
                get_next_tipus_contracte = True
            
            if(get_next_subtitpus_contracte):
                subtitpus_contracte = trim(content.getText())
                get_next_subtitpus_contracte = False

            if(content.getText().find('Subtipus de contracte')>=0):
                get_next_subtitpus_contracte = True

            if(get_next_procediment_adjudicacio):
                procediment_adjudicacio = trim(content.getText())
                get_next_procediment_adjudicacio = False

            if(content.getText().find('Procediment d')>=0):
                get_next_procediment_adjudicacio = True

            if(get_next_compra_publica_innovacio):
                compra_publica_innovacio = trim(content.getText())
                get_next_compra_publica_innovacio = False

            if(content.getText().find('Compra p')>=0):
                get_next_compra_publica_innovacio = True

            if(get_next_denominacio):
                denominacio = trim(content.getText())
                get_next_denominacio = False

            if(content.getText().find('Denominaci')>=0):
                get_next_denominacio = True

        value += "\t" + organ_contractacio + "\t" + codi_expedient + "\t" + tipus_tramitacio + "\t" + tipus_contracte + "\t" + subtitpus_contracte + "\t" + procediment_adjudicacio + "\t" + compra_publica_innovacio + "\t" + denominacio

        #<span class="pressupost">4.050,00 € sense IVA</span>
        contents = html.find_all('span', 'pressupost')
        if len(contents)>0:
            value += "\t" + trim(contents[0].text.replace('€ sense IVA', ''))
        else:
            value += "\t???"

    return value