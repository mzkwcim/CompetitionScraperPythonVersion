import requests
from bs4 import BeautifulSoup

class ScrapingSystem:
    @staticmethod
    def Loader(url):
        response = requests.get(url)
        if response.status_code == 200:
            html = response.text
            html_document = BeautifulSoup(html, 'html.parser')
            return html_document
        else:
            print("Błąd pobierania danych.")
            return None
