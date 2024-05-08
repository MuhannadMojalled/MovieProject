from tkinter import *
from tkvideo import tkvideo
import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

# creating the main window
root = customtkinter.CTk()

# setting the title and size of the window
root.title("Image Editor")
root.geometry("1000x850")

# frame zero
frame0 = customtkinter.CTkFrame(master=root, width=960, height=100)
frame0.pack(pady=10, padx=10)
frame0.pack_propagate(0)

my_label = Label(root)
my_label.pack()
# player = tkvideo(
#     r"C:\Users\muasu\Videos\Presentation1.mp4",
#     my_label,
#     loop=1,
#     size=(640, 360),
# )
# player.play()

root.mainloop()
