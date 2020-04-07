from bs4 import BeautifulSoup
import requests


def getLinks():
    url = "https://medium.com/tag/technology/archive"
    links = []
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'html.parser')
    rawlinks = soup.findAll('div', {"class": "postArticle-readMore"})
    for link in rawlinks:
        link = link.a.get('href').split("?")[0]
        links.append(link)
        
    return links

if __name__ == "__main__":
    print(getLinks())
