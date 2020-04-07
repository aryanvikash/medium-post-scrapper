from bs4 import BeautifulSoup
import requests

# link = "https://medium.com/free-code-camp/ill-never-bring-my-phone-on-an-international-flight-again-neither-should-you-e9289cde0e5f"


def Getimage(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.content, "html.parser")

    image = soup.find('figure')

    s = soup.find("img")
    return s['src']


