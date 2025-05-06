import os
import io
import re
import sys
import random

from colorama import Fore
from tkinter import Label, font, StringVar

def read_words():
    """
    Reads and filters word lists from two text files, then selects a random hidden word.

    Returns:
        tuple: A tuple containing a list of all filtered words from both files,
        and single word randomly chosen from the filtered duck word list to be used as the hidden word.

    Raises:
        SystemExit: If either 'duck_words.txt' or 'es_words.txt' is not found in the './assets/' directory.
    """
    words = []
    duck_words_path = "./assets/data/duck_words.txt"
    es_words_path = "./assets/data/es_words.txt"

    if not os.path.exists(duck_words_path):
        print(Fore.RED + "El archivo 'duck_words.txt' no se ha encontrado en la carpeta de assets.")
        sys.exit(1)
    
    if not os.path.exists(es_words_path):
        print(Fore.RED + "El archivo 'es_words.txt' no se ha encontrado en la carpeta de assets.")
        sys.exit(1)

    words = []
    with open(duck_words_path, "r", encoding="utf-8") as fr:
        filtered = word_filter(fr)
        words += filtered

    hidden_word = random.choice(words)

    with open(es_words_path, "r", encoding="utf-8") as fr:
        filtered = word_filter(fr)
        words += filtered

    return words, hidden_word

def word_filter(file: io.TextIOWrapper):
    """
    Filters words from a text file, returning only 5-letter words 
    without accented vowels.

    Parameters:
        file (`io.TextIOWrapper`): 
            A text file object opened in read mode. Each line is expected to contain a word.

    Returns:
        list[str]: 
            A list of words that are exactly 5 letters long and don't contain accented vowels (á, é, í, ó, ú).
    """
    lines = [line.strip() for line in file if line.strip()]
    filtered = [line for line in lines if len(line) == 5 and not re.search("[áéíóú]", line)]
    return filtered

def limit(text: StringVar):
    """
    Limits the text length of the text input.

    Parameters:
        text (`tk.StringVar()`): The text string variable.
    """
    if len(text.get()) > 0:
        text.set(text.get()[:5])

def color_match(self, guess: str):
    """
    Checks which characters in the user's word match the hidden word,
    and changes the colors of the boxes.

    Parameters:
        self (`self`): The instance of DuckWordle class.
        guess (`str`): The guessed word.
    """
    char_list = list(self.hidden_word)
    edited_word = ""
    
    for c1, c2 in zip(self.hidden_word, guess):
        if c1 == c2:
            edited_word += c1
        else:
            edited_word += "#"

    for i, (c1, c2) in enumerate(zip(self.hidden_word, guess)):
        self.boxes = Label(
            self.boxes_frame, width=4, height=2, bg=self.gray,
            text=c2.upper(), font=font.Font(family="Arial", size=15, weight="bold"),
            fg="white", highlightthickness=2, highlightbackground=self.gray
        )
        self.boxes.grid(column=i, row=self.row, padx=3, pady=3)
        
        # Right position (green)
        if c1 == c2:
            self.boxes["bg"] = self.green
            self.boxes["highlightbackground"] = self.green
            continue

        # Not in hidden word (gray)
        if (c2 not in self.hidden_word) or (char_list.count(c2) <= edited_word.count(c2)):
            continue

        # Bad position in hidden word (yellow)
        self.boxes["bg"] = self.yellow
        self.boxes["highlightbackground"] = self.yellow
        char_list.remove(c2)

def autoupper(text: StringVar):
    """
    Automatically uppers the text input.

    Parameters:
        text (`tk.StringVar()`): The text string variable.
    """
    text.set(text.get().upper())

def remove_non_letters(text: StringVar):
    """
    Removes the non-alphabetical characters.

    Parameters:
        text (`tk.StringVar()`): The text string variable.
    """
    value = text.get()
    if not value:
        return

    allowed_chars = "abcdefghijklmnñopqrstuvwxyz"

    if value[-1].lower() not in allowed_chars:
        text.set(value[:-1])