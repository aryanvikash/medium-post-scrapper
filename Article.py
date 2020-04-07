from bs4 import BeautifulSoup
import requests
import unicodedata


article = []
# link = "https://medium.com/free-code-camp/ill-never-bring-my-phone-on-an-international-flight-again-neither-should-you-e9289cde0e5f"


def getArticle(link):
    final = ""
    r = requests.get(link)
    soup = BeautifulSoup(r.content ,"html.parser")
    rawparas = soup.findAll("article")
    
    
    for r in rawparas:
            para = r.findAll("p")
            for p in para:
                final += str(p.text)


    return final

if __name__ == "__main__":
    print(getArticle(link))