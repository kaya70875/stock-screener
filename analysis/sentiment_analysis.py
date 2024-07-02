from transformers import pipeline
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification

class Analysis:
    def __init__(self):
        'Sentiment Analysis for News and Headers'
    
    def sentimentAnalysis(self , input : str):
        tokenizer = AutoTokenizer.from_pretrained('ProsusAI/finbert')
        model = AutoModelForSequenceClassification.from_pretrained('ProsusAI/finbert')

        nlp = pipeline('sentiment-analysis' , model=model , tokenizer=tokenizer , max_length=512 , truncation=True)
        score = nlp(input)
        return score[0]['label']