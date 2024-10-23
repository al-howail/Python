import tkinter as tk
from time import time

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.sample_text = "The quick brown fox jumps over the lazy dog"
        self.text_length = len(self.sample_text)

        self.label = tk.Label(root, text=self.sample_text, font=("Arial", 16))
        self.label.pack(pady=20)

        self.text_entry = tk.Entry(root, font=("Arial", 16))
        self.text_entry.pack(pady=20)
        self.text_entry.bind("<Return>", self.calculate_speed)

        self.result_label = tk.Label(root, text="", font=("Arial", 16))
        self.result_label.pack(pady=20)

        self.start_time = None

        self.start_button = tk.Button(root, text="Start", command=self.start_test, font=("Arial", 14))
        self.start_button.pack(pady=20)

    def start_test(self):
        self.text_entry.delete(0, tk.END)
        self.text_entry.focus()
        self.start_time = time()
        self.result_label.config(text="")

    def calculate_speed(self, event):
        end_time = time()
        time_taken = end_time - self.start_time
        words_per_minute = (self.text_length / 5) / (time_taken / 60)
        self.result_label.config(text=f"Typing Speed: {words_per_minute:.2f} WPM")

if __name__ == "__main__":
    root = tk.Tk()
    test = TypingSpeedTest(root)
    root.mainloop()
