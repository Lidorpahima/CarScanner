import webbrowser
from pathlib import Path
import os
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, Label, messagebox
from tkinter.font import Font



class ButtonManager:
    def __init__(self):
        self.canvas = Canvas(self.window, bg="black", height=1000, width=600)
        self.canvas.place(x=0, y=0)

    def WrongNumber(number):
        print(f"Wrong number: {number}")

    def send_whatsapp_message(entry_phone):
        phone_number = entry_phone
        try:
            if phone_number == "":
                messagebox.showerror("שגיאה", "אנא הכנס מספר טלפון")
                return
            if phone_number[0] != "0" :
                print("Missing 0 at the start of the number")
                messagebox.showerror("שגיאה", "רשום את המספר כולל ספרת 0 בתחילתו")
                return
            if len(phone_number) != 10 :
                print("valid number")
                messagebox.showerror("שגיאה", "בדוק את מספר הטלפון שנית")
                return
            if not phone_number.isdigit():
                print("non digit number appears")
                messagebox.showerror("שגיאה", "מספר הטלפון יכול להכיל רק ספרות!")
                return
            URL = "https://wa.me/" +"+972"+ phone_number[1:10]
            print(URL)
            webbrowser.open(URL)
        except ValueError:
            print("Please enter a valid number")

    def open_about_window():
        global background_image

        about_window = Toplevel()
        about_window.resizable(False, False)
        about_window.title("אודות")
        about_window.geometry("400x200")
        canvas = Canvas(about_window, width=300, height=300)
        canvas.pack(fill="both", expand=True)
        background_image = PhotoImage(file="assets/frame0/Background-about.png")
        canvas.create_image(0, 0, image=background_image, anchor="nw")
        canvas.create_text(
            200, 100,
            text="אני מבין עד כמה זה יכול להיות מאתגר לחפש\n מידע על רכב.  פעמים רבות אנחנו מוצאים את עצמנו משקיעים\n שעות בחיפושים,מבלי למצוא את המידע שאנחנו צריכים\n או שעדיין לא ברור מה באמת חשוב לדעת.אני מקווה\n שהיישום הזה יסייע לכם להימנע מהתחושה של תסכול\n .ויאפשר לכם לבצע את החיפושים בצורה חכמה וקלילה \n :מייל ליצירת קשר\n"
                 "Lidorpahima28@gmail.com",
            font=("Suez One", 12),
            fill="White",
            justify="center"
        )
    def Display_Car_Details(self, entry_carNumber, canvas):
        car_number = entry_carNumber
        if not car_number :
            print("Please enter a valid number")
            messagebox.showerror("שגיאה", "אנא הכנס מספר רכב")
            return
        if len(car_number) > 8 or len(car_number) <= 6:
            messagebox.showerror("שגיאה", "מספר רכב חייב להיות בעל 7 או 8 ספרות")
            return
        car_details = f"פרטי רכב עבור מספר {car_number}"
        suez_one_font_Small = Font(family="Suez One", size=11)
        canvas.create_text(535.0,112.0,anchor="nw",text=":פרטי רכב",fill="#FFFFFF", font=suez_one_font_Small)
        canvas.create_text(223.0,111.0,anchor="nw",text=":מידע נוסף",fill="#FFFFFF",font=suez_one_font_Small)



