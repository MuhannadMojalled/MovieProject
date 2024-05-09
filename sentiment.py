from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from nltk.corpus import stopwords


class sentiment:
    def __init__(self):
        super().__init__()

    def returnInfo(self, detailed_sentiments):
        reviews = []
        for sentiment in detailed_sentiments:
            reviews.append(
                [
                    f"{sentiment['The Review']}",
                    f"{sentiment['Review classification']}",
                ]
            )
        return reviews

    def MovieSentimentReview(self, reviews):
        sia = SentimentIntensityAnalyzer()
        vectorizer = TfidfVectorizer()

        # Calculate TF-IDF scores to get the most importent words
        tfidfMatrix = vectorizer.fit_transform(reviews, stopwords.words("english"))
        featureNames = vectorizer.get_feature_names_out()

        detailed_reviews = []
        # this iterartion will go throghout all the reviews provided to Know if they are 'Positive', 'Negative', 'Neutral'
        for review, tfidfVec in zip(reviews, tfidfMatrix):
            blob = TextBlob(review)
            vaderScores = sia.polarity_scores(review)
            tfidfScores = np.array(tfidfVec.todense()).flatten()

            # Find top 2 significant words based on TF-IDF scores that we calculated
            top_indices = np.argsort(tfidfScores)[-2:]
            topWord = []
            for index in top_indices:
                if tfidfScores[index] > 0:
                    word = featureNames[index]
                    topWord.append(word)

            # we will append the reviews to a format way
            def classify_sentiment(polarity):
                if polarity > 0.05:
                    return "This Movie review is Positive"
                elif polarity < -0.05:
                    return "This Movie review is Negative"
                else:
                    return "This Movie review is Neutral"

            detailed_reviews.append(
                {
                    "The Review": review,
                    "polarity Of the review": round(blob.sentiment.polarity, 4),
                    "subjectivity": round(blob.sentiment.subjectivity, 4),
                    "intensity": round(vaderScores["compound"], 3),
                    "Review classification": classify_sentiment(
                        blob.sentiment.polarity
                    ),
                    "Key words": topWord,
                }
            )

        return detailed_reviews

    # *Delete This After Editing*  Example reviews, Muhanned choice the best method that you would like on providing The Reviews.
    reviews = [
        "got the 4D experience by forgetting to drink water today and watching this extremely dehydrated",
        "not bad if u ever just feel like staring at the color orange and not feeling a single emotion for two and a half hours",
        "favourite movie.",
        "155 minutes of industrial design and thousand-yard-stares while Hans Zimmer honks at you with his giant mechanical goose.",
    ]

    def getInfo(self):
        print(self.reviews)
        s = self.MovieSentimentReview(self.reviews)
        sentiments = self.returnInfo(s)
        return sentiments
