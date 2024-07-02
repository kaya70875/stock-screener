from utils.get_news import GetNews
from data.sentiment_analysis import Analysis

def getArticles(*pair_name):
    news = GetNews(pair_name)

    return news.fetchTW()

def getSentimentAnalysisResults(articles):
    Sresults = []
    analysis = Analysis()
    for article in articles:
        for element in article:
            score = analysis.sentimentAnalysis(input=element['header'] + element['text'])
            
            results = {'Header' : element['header'],
                    'Date' : element['date'],
                    'Label' : score}

            Sresults.append(results)

    return Sresults

articles = getArticles('AAPL' , 'ARCLK' , 'TSLA' , 'OYAKC')

results = getSentimentAnalysisResults(articles=articles)

for result in results:
    print(f'Results : {result}')
