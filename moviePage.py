import customtkinter
from PIL import Image
from tkVideoPlayer import TkinterVideo
from movieData import moviesData
import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

# the page for each movie


class moviePage(customtkinter.CTkToplevel):
    def __init__(self, master, movieId):
        super().__init__()
        movieData = moviesData.getMovieData(movieId)
        self.title(movieData[0])
        self.geometry("1000x650")
        self.minsize(1000, 650)
        # main zero
        window = customtkinter.CTkTabview(self, width=950, height=550)
        window.pack(pady=10, padx=10, side="top")
        window.pack_propagate(False)
        window.add("Movie")
        window.add("Trailer")
        window.add("Reviews")

        # Frame for movie pic and more info
        frame1 = customtkinter.CTkFrame(
            master=window.tab("Movie"),
            width=200,
            height=550,
        )
        frame1.pack(
            pady=10,
            padx=10,
            side="left",
            anchor="sw",
        )
        frame1.pack_propagate(0)

        # movie pic frame
        frame2 = customtkinter.CTkFrame(
            master=frame1,
            width=200,
            height=250,
        )
        frame2.pack(
            pady=10,
            padx=10,
        )
        frame2.pack_propagate(0)

        # more info frame
        frame3 = customtkinter.CTkFrame(master=frame1, width=200, height=250)
        frame3.pack(
            pady=10,
            padx=10,
        )
        frame3.pack_propagate(0)

        year = customtkinter.CTkLabel(
            frame3,
            text="\nAge rating: " + movieData[3],
            font=("Arial", 18),
            wraplength=150,
        )
        year.pack(padx=5, pady=5)
        year.pack_propagate()
        age = customtkinter.CTkLabel(
            frame3,
            text="\nYear: " + movieData[2],
            font=("Arial", 18),
            wraplength=150,
        )
        age.pack(padx=5, pady=5)
        age.pack_propagate()
        duration = customtkinter.CTkLabel(
            frame3,
            text="\nDuration: " + movieData[1],
            font=("Arial", 18),
            wraplength=150,
        )
        duration.pack(padx=5, pady=5)
        duration.pack_propagate()

        # Movie title frame
        frame4 = customtkinter.CTkFrame(
            master=window.tab("Movie"), width=700, height=50, fg_color="#252526"
        )
        frame4.pack(
            pady=20,
            padx=10,
            side="top",
            anchor="ne",
        )
        frame4.pack_propagate(0)

        title = customtkinter.CTkLabel(frame4, text=movieData[0], font=("Arial", 25))
        title.pack(padx=5, pady=5)

        # Movie description frame
        frame5 = customtkinter.CTkFrame(
            master=window.tab("Movie"), width=700, height=450, fg_color="#252526"
        )
        frame5.pack(
            padx=10,
            side="right",
            anchor="ne",
        )
        frame5.pack_propagate(0)
        story = customtkinter.CTkLabel(
            frame5,
            text="\nStory: " + movieData[6],
            font=("Arial", 25),
            wraplength=650,
        )
        story.pack(padx=5, pady=5)

        director = customtkinter.CTkLabel(
            frame5,
            text="Directors: " + movieData[5],
            font=("Arial", 25),
            wraplength=650,
        )
        director.pack(padx=5, pady=5)

        writer = customtkinter.CTkLabel(
            frame5,
            text="Writers: " + movieData[4],
            font=("Arial", 25),
            wraplength=650,
        )
        writer.pack(padx=5, pady=5)

        img = Image.open(movieData[7])
        width, height = 200, 300
        img = img.resize((width, height))
        tkimage = customtkinter.CTkImage(img, size=(200, 300))
        img_label = customtkinter.CTkLabel(
            frame2,
            text=movieData[3],
            text_color="white",
            font=("Arial", 25),
            compound="center",
            image=tkimage,
        )
        img_label.pack(fill=customtkinter.BOTH)

        pygame.mixer.init()

        def play():
            try:
                paused
            except NameError:
                pygame.mixer.music.load(movieData[9])
                pygame.mixer.music.play()
            else:
                pygame.mixer.music.unpause()

        def pause():
            global paused
            paused = True
            pygame.mixer.music.pause()

        trailer = customtkinter.CTkLabel(
            window.tab("Trailer"),
            text="Movie Trailer",
            font=("Arial", 15),
            wraplength=150,
        )
        trailer.pack(padx=5, pady=5)
        trailer.pack_propagate()

        video_player = TkinterVideo(master=window.tab("Trailer"), scaled=True)
        video_player.pack(padx=20, pady=10, anchor="center", expand=True, fill="both")
        video_player.load(movieData[8])

        buttonPlay = customtkinter.CTkButton(
            master=window.tab("Trailer"),
            text="Play",
            command=lambda: [video_player.play(), play()],
        )
        buttonPlay.pack(pady=5)

        buttonPause = customtkinter.CTkButton(
            master=window.tab("Trailer"),
            text="Pause",
            command=lambda: [video_player.pause(), pause()],
        )
        buttonPause.pack(pady=5)

        reviews = customtkinter.CTkLabel(
            window.tab("Reviews"),
            text="Movie Reviews",
            font=("Arial", 15),
            wraplength=150,
        )
        reviews.pack(padx=5, pady=5)
        reviews.pack_propagate()
        textbox = customtkinter.CTkTextbox(
            master=window.tab("Reviews"), width=500, height=350
        )
        textbox.configure(state="disabled")
        textbox.pack()
        textbox.tag_config("Positive", foreground="green")
        textbox.tag_config("Negative", foreground="red")
        textbox.tag_config("Neutral", foreground="white")

        for review in movieData[10]:
            if "Positive" in review[1]:
                textbox.configure(state="normal")
                textbox.insert(
                    "0.0",
                    str(len(movieData[10]) - (movieData[10].index(review)))
                    + "- Review: "
                    + review[0]
                    + "\nAnalysis: "
                    + review[1]
                    + "\n",
                    tags="Positive",
                )
                textbox.configure(state="disabled")
            elif "Negative" in review[1]:
                textbox.configure(state="normal")
                textbox.insert(
                    "0.0",
                    str(len(movieData[10]) - (movieData[10].index(review)))
                    + "- Review: "
                    + review[0]
                    + "\nAnalysis: "
                    + review[1]
                    + "\n",
                    tags="Negative",
                )
                textbox.configure(state="disabled")
            else:
                textbox.configure(state="normal")
                textbox.insert(
                    "0.0",
                    str(len(movieData[10]) - (movieData[10].index(review)))
                    + "- Review: "
                    + review[0]
                    + "\nAnalysis: "
                    + review[1]
                    + "\n",
                    tags="Neutral",
                )
                textbox.configure(state="disabled")
