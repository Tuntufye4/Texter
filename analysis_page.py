import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import summarize
import text_to_speech
import entity_recognition
import word_frequency
import sentiment_analysis
import matplotlib.pyplot as plt


class AnalysisPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.filename = None

        self.upload_button = tk.Button(
            self,
            text="Upload File",
            font=("Arial", 16),
            command=self.upload_file,
            bg="black",
            fg="white",
            width=15
        )
        self.upload_button.pack(pady=20)

        self.summarize_button = tk.Button(
            self,
            text="Summarize Document",
            font=("Arial", 16),
            command=self.summarize_document,
            bg="black",
            fg="white",
            width=20
        )
        self.summarize_button.pack(pady=10)

        self.speech_button = tk.Button(
            self,
            text="Convert to Speech",
            font=("Arial", 16),
            command=self.convert_to_speech,
            bg="black",
            fg="white",
            width=20
        )
        self.speech_button.pack(pady=10)

        self.entity_button = tk.Button(
            self,
            text="Recognize Entities",
            font=("Arial", 16),
            command=self.recognize_entities,
            bg="black",
            fg="white",
            width=20
        )
        self.entity_button.pack(pady=10)

        self.frequency_button = tk.Button(
            self,
            text="Calculate Word Frequency",
            font=("Arial", 16),
            command=self.calculate_word_frequency,
            bg="black",
            fg="white",
            width=20
        )
        self.frequency_button.pack(pady=10)

        self.sentiment_button = tk.Button(
            self,
            text="Analyze Sentiment",
            font=("Arial", 16),
            command=self.analyze_sentiment,
            bg="black",
            fg="white",
            width=20
        )
        self.sentiment_button.pack(pady=10)

    def upload_file(self):
        filetypes = (
            ("Text Files", "*.txt"),
            ("PDF Files", "*.pdf"),
            ("All Files", "*.*")
        )
        filename = filedialog.askopenfilename(filetypes=filetypes)
        if filename:
            self.filename = filename
            messagebox.showinfo("File Uploaded", "File uploaded successfully.")

    def summarize_document(self):
        if not self.filename:
            messagebox.showerror("Error", "Please upload a file first.")
            return

        summary = summarize.summarize_document(self.filename)
        messagebox.showinfo("Summarize Document", f"Summary:\n{summary}")

    def convert_to_speech(self):
        if not self.filename:
            messagebox.showerror("Error", "Please upload a file first.")
            return

        text_to_speech.convert_to_speech(self.filename)
        messagebox.showinfo("Convert to Speech", "File converted to speech successfully.")

    def recognize_entities(self):
        if not self.filename:
            messagebox.showerror("Error", "Please upload a file first.")
            return

        entities = entity_recognition.recognize_entities(self.filename)
        messagebox.showinfo("Recognize Entities", f"Entities:\n{entities}")

    def calculate_word_frequency(self):
        if not self.filename:
            messagebox.showerror("Error", "Please upload a file first.")
            return

        word_freq = word_frequency.calculate_word_frequency(self.filename)

        labels = list(word_freq.keys())
        values = list(word_freq.values())

        plt.bar(labels, values)
        plt.xlabel("Words")
        plt.ylabel("Frequency")
        plt.title("Word Frequency")
        plt.show()

    def analyze_sentiment(self):
        if not self.filename:
            messagebox.showerror("Error", "Please upload a file first.")
            return

        sentiment_scores = sentiment_analysis.analyze_sentiment(self.filename)

        labels = sentiment_scores.keys()
        values = list(sentiment_scores.values())

        plt.bar(labels, values)
        plt.xlabel("Sentiment")
        plt.ylabel("Score")
        plt.title("Sentiment Analysis")
        plt.show()
