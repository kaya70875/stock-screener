import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

def getResults(article):
    results_list = []
    sia = SentimentIntensityAnalyzer()
    for element in article:
        score = sia.polarity_scores(element['text'])

        results_list.append({
            'header' : element['header'],
            'date' : element['date'],
            'score' : score['compound']
        })
    return results_list
    
        