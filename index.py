import tkinter as tk
from core.classes import DuckWordle

if __name__ == "__main__":
    window = tk.Tk()
    window.config(bg="white")
    window.resizable(False, False)
    
    logo_path = "./assets/images/duck.png"
    logo = tk.PhotoImage(file=logo_path)
    window.iconphoto(True, logo)

    window_height = 650
    window_width = 500

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))

    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    window.title("DuckWordle")
    app = DuckWordle(window)
    app.mainloop()