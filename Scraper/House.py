class House:
    def __init__(self, address, price, sqft, description, image_urls, links):
        self.address = address
        self.price = price
        self.sqft = sqft
        self.description = description
        self.image_urls = image_urls
        self.links = links
    def afficher_detail(self):
        print("Address: " + self.address)
        print("Price: " + self.price)
        print("Square feet: " + self.sqft)
        print("Description: " + self.description)
        print("Image urls: " + str(self.image_urls))
        print("Links: " + str(self.links))
    def to_dict(self):
        return {
            "address": self.address,
            "price": self.price,
            "sqft": self.sqft,
            "description": self.description,
            "image_urls": self.image_urls,
            "links": self.links
        }

appart = House(
    "123 rue de la paix",
    "1000000",
    "1000",
    "Une maison de rêve",
    ["https://www.google.com"],
    ["https://www.google.com"]
)
appart.afficher_detail()
print(appart.to_dict())