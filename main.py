from crawlers.get_news import GetNews
from analysis.sentiment_analysis import Analysis
from data.database import insertResults

import threading

def getArticles(pair_name , results):
    news = GetNews(pair_name)
    articles = news.fetchTW(max_news=7)
    results.append(articles)

def getSentimentAnalysisResults(articles , results):
    analysis = Analysis()
    for element in articles:
        score = analysis.sentimentAnalysis(input=element['header'] + element['text'])
            
        Sresults = {
                    'Company' : element['company'],
                    'Header' : element['header'],
                    'Date' : element['date'],
                    'Label' : score}

        results.append(Sresults)


stocks = ['ARCLK' , 'LOGO' , 'OYAKC']

threads = []
thread_results = []

analyze_threads = []
analyze_results = []

def startFetchingProcess():
    
    for symbol in stocks:
        thread = threading.Thread(target=getArticles , args=(symbol, thread_results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def startAnalyzingProcess():
    for article in thread_results:
        thread = threading.Thread(target=getSentimentAnalysisResults , args=(article , analyze_results))
        analyze_threads.append(thread)
        thread.start()

    for thread in analyze_threads:
        thread.join()

def show_results():
    for results in analyze_results:
        print(f'Results : {results}')

def main():

    startFetchingProcess()
    startAnalyzingProcess()

    show_results()
    #insertResults(analyze_results)

if __name__ == '__main__':
    main()