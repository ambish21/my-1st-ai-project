from textblob import TextBlob
def check_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the sentiment polarity (ranges from -1 (negative) to 1 (positive))
    sentiment = blob.sentiment.polarity
    
    # Return sentiment type based on polarity
    if sentiment > 0:
        return "Positive Sentiment"
    elif sentiment < 0:
        return "Negative Sentiment"
    else:
        return "Neutral Sentiment"
