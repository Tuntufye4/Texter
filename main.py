import tkinter as tk
from welcome_page import WelcomePage
from password_page import PasswordPage
from analysis_page import AnalysisPage


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Texter")
        self.geometry("800x600")
        self.resizable(False, False)
        self.iconbitmap("images\logo.png")

        self.welcome_page = WelcomePage(self)
        self.password_page = PasswordPage(self)
        self.analysis_page = AnalysisPage(self)

        self.current_page = None
        self.show_welcome_page()

    def show_welcome_page(self):
        if self.current_page:
            self.current_page.pack_forget()

        self.current_page = self.welcome_page
        self.current_page.pack()

    def show_password_page(self):
        if self.current_page:
            self.current_page.pack_forget()

        self.current_page = self.password_page
        self.current_page.pack()

    def show_analysis_page(self):
        if self.current_page:
            self.current_page.pack_forget()

        self.current_page = self.analysis_page
        self.current_page.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
