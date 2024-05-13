from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from nltk.corpus import stopwords

# class for sentiment analysis of the movie reviews


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

    reviews = {
        "Movie1": [
            "here is actually no reason to watch this",
            "Damn this really ruined Shrek’s track record",
            "if there's at least one thing this film got right, it's that taking the stamps oD envelopes in -postboxes truly is one of the most evil things you can do",
            "every time I watch this a new quote absolutely sends me. this time it was 'avast, ye cookie!' i honest to god almost cried",
            "THIS MOVIE IS JUST ACTION UPON ACTION UPON ACTION THEY DONT LET U REST ONE MOMENT EVERYTHING IS SO FUCKING GOOD",
        ],
        "Movie2": [
            "I'm not trying to be contrarian here, or drop a hyperbolic statement. I just find TDK to be one of the more overrated films in recent times. The editing, dialogue.....it's so clunky.",
            "This gets worse every time I watch it.",
            "the best superhero movie ever made. Period",
            "The greatest comic book movie of all time.",
            "Probably the movie that made me realize that super cool fights aren't the most compelling part of a superhero film. This film molded my 'film-making style' and I hope to create something at least half as good as this in my lifetime.",
        ],
        "Movie3": [
            "Every time I watch The Matrix I am certain it’s the best movie of all time",
            "I hate this film I hate their stupid sunglasses I hate their stupid coats I HATE IT ALL",
            "I really wanted to love this movie but i didn't even like it. apologies to my man keanu reeves.",
            "I'll say I engaged a bit more on with this on rewatch. Epic moments of action. This is actually pretty decent. I'm not like in LOVE with it but it has some nice stuD.",
            " this is actually like the coolest movie ever had to show it to my girlfriend after just watching it yesterday for the first time ",
        ],
        "Movie4": [
            "This is truly the cinematic event of our generation… don’t take it for granted 100/100",
            "Easily the second best movie starring Timothée and Florence",
            "The worst film I've ever seen (I accidentally walked into Madame Web).",
            "If Dune has 1,000 haters, i’m one of them. If Dune has 10 haters, i’m one of them. If Dune has 1 hater, it’s me. If Dune has no haters, i’m dead.",
            "I don’t think it was such a good idea to give the messiah the nuclear launch codes",
        ],
        "Movie5": [
            "Back to the future is a top 5 movie of all time. One of the most brilliant pieces of art that has ever been created. The acting, the score, the script and most important the many chekhovs guns ake this film a masterpiece!",
            "It is so boring and overrated! The only reason people like it because it was original, it’s not anymore and it sucks",
            "I'ts one of the movie's that you only really watch with your family.But i personally love that.",
            "i have never been so immensely pissed off at a movie in my life",
            "Man I can watch this trilogy 5 times and i can watch this trilogy 500 times, it never gets old for me. these movies are classics and constantly stand the test of time for film. I love rewatching this trilogy. Up next is part 2",
        ],
    }

    def getInfo(self, movieId):
        s = self.MovieSentimentReview(self.reviews[movieId])
        sentiments = self.returnInfo(s)
        # print(sentiments)
        return sentiments
