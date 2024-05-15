from sentiment import sentiment

# Data for all Movies


class moviesData:
    def __init__(self):
        super().__init__()

    def getMovieData(movieId):
        sentimentsObject = sentiment()
        sentiments = sentimentsObject.getInfo(movieId)
        moviesData = {
            "MovieID": [
                "Movie Name",
                "Duration",
                "Year",
                "Age Rating",
                "Writers",
                "Directors",
                "Story",
                "Poster",
                "Trailer",
                "Sound",
                "Reviews",
            ],
            "Movie1": [
                "Shrek",
                "1h 30m",
                "2001",
                "PG",
                "William Steig, Ted Elliott, Terry Rossio",
                "Andrew Adamson, Vicky Jenson",
                "A mean lord exiles fairytale creatures to the swamp of a grumpy ogre, who must go on a quest and rescue a princess for the lord in order to get his land back.",
                r"Assets\Posters\Shrek+Poster.png",
                r"Assets\Trailers\subtitled\Shrek 2001 Official Trailer_subtitled.mp4",
                r"Assets\Sounds\Shrek 2001 Official Trailer.mp3",
                sentiments,
            ],
            "Movie2": [
                "The Dark Knight",
                "2h 32m",
                "2008",
                "PG-13",
                "Christopher Nolan",
                "Jonathan Nolan, Christopher Nolan, David S. Goyer",
                "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
                r"Assets\Posters\thedarknight.jpg",
                r"Assets\Trailers\subtitled\The Dark Knight (2008) Official Trailer 1 - Christopher Nolan Movie HD_subtitled.mp4",
                r"Assets\Sounds\The Dark Knight (2008) Official Trailer 1 - Christopher Nolan Movie HD.mp3",
                sentiments,
            ],
            "Movie3": [
                "The Matrix",
                "2h 16m",
                "1999",
                "R",
                "Lilly Wachowski, Lana Wachowski",
                "Lilly Wachowski, Lana Wachowski",
                "When a beautiful stranger leads computer hacker Neo to a forbidding underworld, he discovers the shocking truth--the life he knows is the elaborate deception of an evil cyber-intelligence.",
                r"Assets\Posters\The Matrix.jpg",
                r"Assets\Trailers\subtitled\The Matrix (1999) Official Trailer 1 - Sci-Fi Action Movie_subtitled.mp4",
                r"Assets\Sounds\The Matrix (1999) Official Trailer 1 - Sci-Fi Action Movie.mp3",
                sentiments,
            ],
            "Movie4": [
                "Dune: Part Two",
                "2h 46m",
                "2024",
                "PG-13",
                "Denis Villeneuve, Jon Spaihts, Frank Herbert",
                "Denis Villeneuve",
                "Paul Atreides unites with Chani and the Fremen while seeking revenge against the conspirators who destroyed his family.",
                r"Assets\Posters\DunePartTwo.jpg",
                r"Assets\Trailers\subtitled\Dune Part Two  Official Trailer_subtitled.mp4",
                r"Assets\Sounds\Dune Part Two  Official Trailer.mp3",
                sentiments,
            ],
            "Movie5": [
                "Back to the Future",
                "1h 56m",
                "1985",
                "PG",
                "Robert Zemeckis, Bob Gale",
                "Robert Zemeckis",
                "Marty McFly, a 17-year-old high school student, is accidentally sent 30 years into the past in a time-traveling DeLorean invented by his close friend, the maverick scientist Doc Brown.",
                r"Assets\Posters\back-to-the-future-i2795.jpg",
                r"Assets\Trailers\subtitled\Back To The Future (1985) Theatrical Trailer - Michael J Fox Movie HD_subtitled.mp4",
                r"Assets\Sounds\Back To The Future (1985) Theatrical Trailer - Michael J Fox Movie HD.mp3",
                sentiments,
            ],
        }
        return moviesData[movieId]
