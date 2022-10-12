import bs4
import requests
import re
import pandas

sites = ["https://www.ibm.com/cloud/learn/natural-language-processing", "https://en.wikipedia.org/wiki/Natural_language_processing", "https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP", "https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html", "https://www.datarobot.com/blog/what-is-natural-language-processing-introduction-to-nlp/"]
conteudos = []

for site in sites:
    url = requests.get(site).content

    soup = bs4.BeautifulSoup(url, "html.parser")
    conteudo = soup.text
    for data in soup(['style', 'script']):
        data.decompose()
    conteudo = ' '.join(soup.stripped_strings)
    conteudo = re.sub("[\n\t]", "", conteudo)
    splitters = re.split("[!?.;:]", conteudo)
    conteudos.append(splitters)