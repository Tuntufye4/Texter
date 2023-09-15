import tkinter as tk
from tkinter import messagebox


class PasswordPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="white")

        self.password_label = tk.Label(
            self,
            text="Enter Password:",
            font=("Arial", 20),
            pady=20,
            bg="white"
        )
        self.password_label.pack()

        self.password_entry = tk.Entry(
            self,
            font=("Arial", 16),
            show="*",
            bg="white"
        )
        self.password_entry.pack()

        self.submit_button = tk.Button(
            self,
            text="Submit",
            font=("Arial", 16),
            command=self.check_password,
            bg="black",
            fg="white",
            width=10
        )
        self.submit_button.pack()

    def check_password(self):
        entered_password = self.password_entry.get()
        expected_password = "t1234m"

        if entered_password == expected_password:
            self.master.show_analysis_page()
        else:
            messagebox.showerror("Invalid Password", "Please enter the correct password.")

