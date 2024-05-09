import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
from moviePage import moviePage


class main(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Main Window")
        window = customtkinter.CTkFrame(master=self, width=950, height=350)
        window.pack(pady=10, padx=10, side="top")
        window.pack_propagate(False)
        title = customtkinter.CTkLabel(window, text="ALL MOVIES", font=("Arial", 25))
        title.pack(padx=5, pady=5)
        self.icon_images = [
            ("Movie1", r"movieProject\Assets\Posters\Shrek+Poster.png", 1),
            ("Movie1", r"movieProject\Assets\Posters\Shrek+Poster.png", 2),
            ("Movie1", r"movieProject\Assets\Posters\Shrek+Poster.png", 3),
            ("Movie1", r"movieProject\Assets\Posters\Shrek+Poster.png", 4),
            ("Movie1", r"movieProject\Assets\Posters\Shrek+Poster.png", 5),
            # Add more images here
        ]

        self.create_icons(window)

    def create_icons(self, window):
        for i in range(len(self.icon_images)):
            img = Image.open(self.icon_images[i][1])
            width, height = 200, 300
            img = img.resize((width, height))
            img = ImageTk.PhotoImage(img, size=(10, 10))
            btn = tk.Button(
                window,
                image=img,
                command=lambda title=self.icon_images[i][0]: self.open_page(
                    title,
                ),
            )
            btn.image = (
                img  # Keep a reference to the image to prevent garbage collection
            )
            s = ""
            if self.icon_images[i][2] % 2 == 0:
                s = "left"
            else:
                s = "right"
            btn.pack(padx=15, pady=10, side=s, anchor="center")

    def open_page(
        self,
        title,
    ):
        page = moviePage(
            self,
            title,
        )
        page.grab_set()  # Prevent interactions with main window
        page.wait_window()  # Wait for page window to be closed


if __name__ == "__main__":
    customtkinter.set_appearance_mode("system")
    customtkinter.set_default_color_theme("dark-blue")
    app = main()
    app.mainloop()
