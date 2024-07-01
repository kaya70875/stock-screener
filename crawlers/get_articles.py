from bs4 import BeautifulSoup

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
         
