import tkinter as tk


class WelcomePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.logo_path = "images\logo.png"
        self.logo_image = tk.PhotoImage(file=self.logo_path)

        self.logo_label = tk.Label(self, image=self.logo_image)
        self.logo_label.pack(pady=100)

        self.after(8000, self.master.show_password_page)  # Schedule navigation to password page after 15 seconds
