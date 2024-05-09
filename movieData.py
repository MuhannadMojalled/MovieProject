from sentiment import sentiment


class moviesData:
    def __init__(self):
        super().__init__()

    def getMovieData(movieId):
        sentimentsObject = sentiment()
        sentiments = sentimentsObject.getInfo()
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
            ],
            "Movie1": [
                "Shrek",
                "1h 30m",
                "2001",
                "PG",
                "William Steig, Ted Elliott, Terry Rossio",
                "Andrew Adamson, Vicky Jenson",
                "A mean lord exiles fairytale creatures to the swamp of a grumpy ogre, who must go on a quest and rescue a princess for the lord in order to get his land back.",
                r"movieProject\Assets\Posters\Shrek+Poster.png",
                r"movieProject\Assets\Trailers\Shrek 2001 Official Trailer.mp4",
                r"movieProject\Assets\Sounds\y2mate.com - Shrek 2001 Official Trailer.mp3",
                sentiments,
            ],
        }
        return moviesData[movieId]
