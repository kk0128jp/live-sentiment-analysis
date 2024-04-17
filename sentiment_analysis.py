from textblob import TextBlob

def analyze_sentiment(text):
    # TextBlobオブジェクトを作成し、テキストを解析します
    blob = TextBlob(text)
    
    # 感情分析を行います
    sentiment = blob.sentiment.polarity
    
    # 感情の極性に基づいて結果を返します
    if sentiment > 0:
        return 'positive'
    elif sentiment < 0:
        return 'negative'
    else:
        return 'neutral'