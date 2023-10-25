from Scraper.Parser import Parser


class LeboncoinParser(Parser):
    def __init__(self, content):
        super().__init__(content)

    def extract_data(self):
        # Extract data from the soup
        # Return a dictionary
        raise NotImplementedError
