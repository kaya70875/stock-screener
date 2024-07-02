from crawlers.get_news import GetNews
from analysis.sentiment_analysis import Analysis

import threading

def getArticles(pair_name , results):
    news = GetNews(pair_name)
    articles = news.fetchTW(max_news=7)
    results.append(articles)

def getSentimentAnalysisResults(articles):
    Sresults = []
    analysis = Analysis()
    for article in articles:
        for element in article:
            score = analysis.sentimentAnalysis(input=element['header'] + element['text'])
            
            results = {
                    'Company' : element['company'],
                    'Header' : element['header'],
                    'Date' : element['date'],
                    'Label' : score}

            Sresults.append(results)

    return Sresults

stocks = ['AAPL' , 'TSLA']
threads = []
thread_results = []

all_articles = []

for symbol in stocks:
    thread = threading.Thread(target=getArticles , args=(symbol, thread_results))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

results = getSentimentAnalysisResults(articles=thread_results)

for result in results:
    print(f'Results : {result}')
