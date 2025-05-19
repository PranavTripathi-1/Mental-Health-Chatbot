from textblob import TextBlob

def analyze_sentiment(user_input):
    analysis = TextBlob(user_input)
    polarity = analysis.sentiment.polarity
    
    if polarity > 0.2:
        return "You sound happy! That's great to hear 😊"
    elif polarity < -0.2:
        return "I'm here for you. Want to talk about what's bothering you? 🌧️"
    else:
        return "Thanks for sharing. How are you feeling today emotionally?"
# This function uses TextBlob to analyze the sentiment of the user's input.
# It returns a response based on the polarity of the sentiment.