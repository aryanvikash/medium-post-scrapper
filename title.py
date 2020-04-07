from bs4 import BeautifulSoup
import requests

TitleList = []



def get_title(link):
        r = requests.get(link)
        soup = BeautifulSoup(r.content, "html.parser")
        Title = soup.find("title")
        return Title




