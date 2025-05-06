from tkinter import Frame, StringVar, Label, Button, Entry, messagebox, font, PhotoImage
from core.utils import *

class DuckWordle(Frame):
    def __init__(self, window):
        super().__init__(window)
        self.window = window
        self.green = "#43A047"
        self.yellow = "#E4A81D"
        self.gray = "#757575"
        self.row = 0
        self.guess = StringVar()
        self.guess.trace_add("write", lambda *args: limit(self.guess))
        self.guess.trace_add("write", lambda *args: autoupper(self.guess))
        self.guess.trace_add("write", lambda *args: remove_non_letters(self.guess))
        self.words, self.hidden_word = read_words()
        self.create_widgets()

    def create_widgets(self):
        self.label = Label(
            self.window, text="DUCKWORDLE", bg="white",
            font=("Arial", 30, "bold"))
        self.label.pack(pady=25)

        self.boxes_frame = Frame(self.window, bg="white")
        self.boxes_frame.pack(side="top")

        for i in range(6):
            for j in range(5):
                boxes = Label(
                    self.boxes_frame, width=4, height=2, highlightthickness=2,
                    text=" ", bg="white", highlightbackground="#E0E0E0",
                    font=font.Font(family="Arial", size=15, weight="bold")
                )
                boxes.grid(column=j, row=i, padx=3, pady=3)

        check_path = "./assets/images/check.png"
        self.check = PhotoImage(file=check_path)

        self.down_bar_frame = Frame(self.window, bg="white")
        self.down_bar_frame.pack(side="bottom", pady=50)

        self.button = Button(
            self.down_bar_frame, command=self.submit_word, image=self.check, bg="#E2E8F0",
            activebackground="#A9AEB4", activeforeground="white",
            bd=0, width=50, height=50, relief="sunken")
        self.button.bind("<Enter>", self.on_enter)
        self.button.bind("<Leave>", self.on_leave)
        self.button.pack(side="right", padx=20)
    
        self.entry = Entry(
            self.down_bar_frame, font=("Arial", "20", "bold"), textvariable=self.guess,
            bd=0, bg="#E2E8F0", justify="center")
        self.entry.pack(side="bottom", pady=10, padx=20)
        self.entry.config(width=7)

    def on_enter(self, event):
        self.button.config(bg="#A9AEB4")

    def on_leave(self, event):
        self.button.config(bg="#E2E8F0")

    def submit_word(self):
        guess = self.guess.get().lower()
        if len(guess) != 5:
            return messagebox.showerror("Error", "La palabra debe tener 5 letras.")
    
        if guess not in self.words:
            return messagebox.showerror("Error", "La palabra no se encuentra en la lista de palabras.")
        
        if self.row <= 6:
            color_match(self, guess)

        self.row = self.row + 1
        if self.row <= 6 and self.hidden_word == guess:
            messagebox.showinfo("Ganaste", "¡Felicidades! Ganaste el DuckWordle")
            self.master.destroy()
            self.master.quit()
        elif self.row == 6 and self.hidden_word != guess:
            messagebox.showinfo("Perdiste", f"La palabra era {self.hidden_word}. ¡Inténtalo de nuevo!")
            self.master.destroy()
            self.master.quit()