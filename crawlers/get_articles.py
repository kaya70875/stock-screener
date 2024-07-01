from bs4 import BeautifulSoup
import requests

def createSession():
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
               'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
               'Accept-Language' : 'en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7,tr;q=0.6'}
    cookies = {'sessionid' : '9dkbdqrund5t80f8785llxc9u369fjyd;',
               'sessionid_sign' : 'v2:zjpTijL+WMwysOpE4hGGeRxHHUlaOLI15fMjDyC8Srw=;'}
    session = requests.Session()
    session.headers.update(headers)
    session.cookies.update(cookies)

    return session

def getArticleElements(links , session):
    articles = []

    for link in links:
        url = link
        r = session.get(url)
        soup = BeautifulSoup(r.content , 'html.parser')
        
        all_text = ''
        container = soup.find('div' , {'class':'body-KX2tCBZq body-pIO_GYwT content-pIO_GYwT body-RYg5Gq3E'})
        article_texts = container.find_all('p')

        for text in article_texts:
            all_text+=text.text

        header = soup.find('h1' , {'class':'title-KX2tCBZq'}).text
        
        container_date = soup.find('span' , {'class':'container-JpONEtnA'})
        date = container_date.find('span').text

        article_data = {
            'header' : header,
            'date' : date,
            'text' : all_text
        }

        articles.append(article_data)
    return articles
         
