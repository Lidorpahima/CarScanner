import tkinter as tk
from tkinter import Canvas
from tkinter.font import Font

# יצירת חלון ראשי
window = tk.Tk()
window.geometry("600x700")
window.configure(bg="#FFFFFF")

# יצירת Canvas
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=700,
    width=600,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# הגדרת הפונט
suez_one_font = Font(family="Suez One", size=24)

# הוספת טקסט עם הפונט החדש
canvas.create_text(
    422.0,
    18.0,
    anchor="nw",
    text="הכנס מספר רכב: ",
    fill="#FFFFFF",
    font=suez_one_font
)

# הפעלת חלון
window.mainloop()
