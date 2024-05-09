import tkinter as tk
from tkinter import *
from tkvideo import tkvideo
import customtkinter
from PIL import Image, ImageTk
from tkVideoPlayer import TkinterVideo
import pygame

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

# creating the main window
root = customtkinter.CTk()

# setting the title and size of the window
root.title("Image Editor")
root.geometry("1000x650")
root.minsize(1000, 650)

# main zero
window = customtkinter.CTkTabview(master=root, width=950, height=550)
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
    frame3, text="more info about the movie", font=("Arial", 20), wraplength=150
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

title = customtkinter.CTkLabel(frame4, text="Movie Title", font=("Arial", 25))
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
    frame5, text="Movie Description", font=("Arial", 25), wraplength=650
)
Desc.pack(padx=5, pady=5)


img = Image.open(r"Shrek+Poster.png")
width, height = 200, 300
img = img.resize((width, height))
tkimage = ImageTk.PhotoImage(img, size=(10, 10))
img_label = tk.Label(frame2, image=tkimage)
img_label.pack(fill=tk.BOTH)

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


root.mainloop()
