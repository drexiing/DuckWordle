import os
import io
import re
import sys
import random
from colorama import Fore

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
    duck_words_path = "./assets/duck_words.txt"
    es_words_path = "./assets/es_words.txt"

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