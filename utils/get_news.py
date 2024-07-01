from crawlers.get_links import getDynamicElement
from crawlers.get_articles import getArticleElements
from utils.session import QSession

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
                'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language' : 'en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7,tr;q=0.6'}
cookies = {'sessionid' : '9dkbdqrund5t80f8785llxc9u369fjyd;',
                'sessionid_sign' : 'v2:zjpTijL+WMwysOpE4hGGeRxHHUlaOLI15fMjDyC8Srw=;'}

class GetNews:
    def __init__(self , pair):
        'FETCH FROM TWO DIFFIRENT SOURCES AND THEN ANALYSE IT.'
        self.pair = pair
    def fetchTW(self):
        links = getDynamicElement(self.pair)

        session = QSession(headers=headers , cookies=cookies).createSession()
        article = getArticleElements(links , session)
            
        return article
    