from selenium import webdriver
import chromedriver_autoinstaller

from crawlers.handle_dynamicWeb import getDynamicElement
from crawlers.get_articles import getArticleElements , createSession
from sentiment_analysis import getResults

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

links = getDynamicElement(driver , 'ARCLK')

session = createSession()
article = getArticleElements(links , session)

# Sentiment Analysis #
results = getResults(article)
print(results)
