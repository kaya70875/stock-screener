from utils.get_news import GetNews
from data.sentiment_analysis import Analysis

def getArticles(pair_name):
    news = GetNews(pair_name)

    return news.fetchTW()

def getSentimentAnalysisResults(articles):
    Sresults = []
    analysis = Analysis()
    for article in articles:
        score = analysis.sentimentAnalysis(input=article['text'])
        
        results = {'Header' : article['header'],
                'Date' : article['date'],
                'Label' : score}

        Sresults.append(results)

    return Sresults

articles = getArticles('AAPL')

results = getSentimentAnalysisResults(articles=articles)

for result in results:
    print(f'Results : {result}')
