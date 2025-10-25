# main.py
import tkinter as tk
from app.ui.main_window import MainWindow
from app.data.database import init_db

def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
    init_db()

if __name__ == "__main__":
    main()
