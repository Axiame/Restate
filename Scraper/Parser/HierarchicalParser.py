import requests
from bs4 import BeautifulSoup
from selenium  import webdriver

class HierarchicalParser:
    def __init__(self):
        self.data = []
        self.driver = webdriver.Safari()

    def getHierarchy(self,url,element):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        elements = soup.find(element)
        if elements:
            hierarchy = []
            parent = elements.parent
            while parent:
                hierarchy.append(parent.name)
                parent = parent.parent
            hierarchy.reverse()
            print(" -> ".join(hierarchy))
        else:
            print("L'URL cible n'a pas été trouvée sur la page.")

    def get_all_urls(self, url):
        self.driver.get(url)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        urls = [a['href'] for a in soup.find_all('a', href=True)]
        return urls
    def close(self):
        self.driver.close()


hier = HierarchicalParser()
print(hier.get_all_urls("https://www.leboncoin.fr/locations/offres/nord_pas_de_calais/p-2"))
hier.close()