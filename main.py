import sentiment_analysis as sa

# テキストを入力として受け取り、感情分析を実行します
def main():
    text = "Everything seems to be going wrong."
    sentiment = sa.analyze_sentiment(text)
    print("感情: ", sentiment)

if __name__ == "__main__":
    main()