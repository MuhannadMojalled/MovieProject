import customtkinter
from PIL import Image
from tkVideoPlayer import TkinterVideo
import pygame


class moviePage(customtkinter.CTkToplevel):
    def __init__(self, master, title):
        super().__init__()
        self.title(title)
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

        moreinfo = customtkinter.CTkLabel(
            frame3,
            text="""\nMore Info
            Released: 2001
            Age rating: PG
            Duration: 1h 30m""",
            font=("Arial", 18),
            wraplength=150,
        )
        moreinfo.pack(padx=5, pady=5)
        moreinfo.pack_propagate()

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

        title = customtkinter.CTkLabel(frame4, text="Shrek", font=("Arial", 25))
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
        Desc = customtkinter.CTkLabel(
            frame5,
            text="""Movie Description\n
            A mean lord exiles fairytale creatures to the swamp of a grumpy ogre, who must go on a quest and rescue a princess for the lord in order to get his land back.\n
            Directors: Andrew Adamson, Vicky Jenson\n
            Writers: William SteigTed Elliott, Terry Rossio\n
            Stars: Mike MyersEddie Murphy, Cameron Diaz""",
            font=("Arial", 25),
            wraplength=650,
        )
        Desc.pack(padx=5, pady=5)

        img = Image.open(
            r"C:\Users\muasu\Desktop\Python\380 enviroment\Shrek+Poster.png"
        )
        width, height = 200, 300
        img = img.resize((width, height))
        tkimage = customtkinter.CTkImage(img, size=(200, 300))
        img_label = customtkinter.CTkLabel(
            frame2,
            text="PG",
            text_color="black",
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
                pygame.mixer.music.load(
                    r"C:\Users\muasu\Downloads\y2mate.com - Shrek 2001 Official Trailer.mp3"
                )
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
        video_player.load(r"C:\Users\muasu\Downloads\Shrek 2001 Official Trailer.mp4")

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

        # Frame for movie pic and more info
        frame30 = customtkinter.CTkFrame(
            master=window.tab("Reviews"),
            width=200,
            height=550,
        )
        frame30.pack(
            pady=10,
            padx=10,
            side="left",
            anchor="sw",
        )
        frame30.pack_propagate(0)
