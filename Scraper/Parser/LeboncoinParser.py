from Scraper.Parser import Parser
from bs4 import BeautifulSoup


class LeboncoinParser(Parser):
    def get_appartement_link(self,city):
        url = "https://www.leboncoin.fr/locations/offres/nord_pas_de_calais/p-1"
        links = []

    def extract_data(self):
        # Extract data from the soup
        # Return a dictionary
        raise NotImplementedError
