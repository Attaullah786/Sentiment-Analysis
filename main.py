import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
sen = SentimentIntensityAnalyzer()
# Example text
text = input("Please write what you feel: ")
# Perform sentiment analysis
sentiment_scores = sen.polarity_scores(text)
# Interpret the sentiment scores
if sentiment_scores['compound'] >= 0.05:
    sentiment = 'Positive'
elif sentiment_scores['compound'] <= -0.05:
    sentiment = 'Negative'
else:
    sentiment = 'Neutral'
# Print the sentiment and sentiment scores
print("Text:", text)
print("Sentiment:", sentiment)
