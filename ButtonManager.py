import webbrowser
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, Label, messagebox
from tkinter.font import Font
import os

import bs4
import requests
from bs4 import BeautifulSoup


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
        suez_one_font_Small = Font(family="Segoe UI Bold", size=11)
        suez_one_font_ = Font(family="Arial Bold Italic", size=13)
        #Fetch car details
        #CHECK IF CAR NUMBER IS VALID
        url = f"https://www.find-car.co.il/car/private/{car_number}"
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        if soup.find('h1').get_text():
            print(soup.find('h1').get_text())

        if soup.find('h1').get_text().strip() == "אופס לא מצאנו את הרכב שחיפשת":
            print("Car number not found")
            messagebox.showerror("שגיאה", "לא קיים מספר רכב כזה במערכת")
            return

        url = f"https://meshumeshet.com/c/{car_number}"  # לדוגמה בלבד

        canvas.create_text(515.0,112.0,anchor="nw",text=":פרטי רכב",fill="#FFFFFF", font=suez_one_font_)
        canvas.create_text(203.0,111.0,anchor="nw",text=":מידע נוסף",fill="#FFFFFF",font=suez_one_font_)

        response = requests.get(url)
        response.raise_for_status()
        ##
        '''''
        SAVE_FOLDER = "assets/Downloaded"
        if not os.path.exists(SAVE_FOLDER):
            os.makedirs(SAVE_FOLDER)

        try:
            # שליחת בקשה לאתר
            response = requests.get(url)

            # אם הבקשה הצליחה (סטטוס 200)
            if response.status_code == 200:
                # יצירת שם קובץ ייחודי לפי כתובת ה-URL של האתר
                file_name = f"{hash(url)}.html"
                file_path = os.path.join(SAVE_FOLDER, file_name)

                # שמירה של התוכן כקובץ HTML
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(response.text)
                print(f"File saved as: {file_path}")
            else:
                print(f"Failed to fetch the website. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error occurred: {e}")
            '''
###
        soup = BeautifulSoup(response.content, 'html.parser')
        data_list = []
        info_list = []
        posX = 585
        posY = 132

        for dt, dd in zip(soup.find_all('dt'), soup.find_all('dd')):
            data_list.append((dt.get_text(), dd.get_text()))

        for item in data_list:
            text = f"{item[1]}  :\u200e{item[0]}"
            canvas.create_text(posX, posY, anchor="ne", text=text, fill="#FFFFFF", font=suez_one_font_Small)
            posY += 20  # רווח בין השורות

        for li in soup.find_all('li'):
            question = li.find('b')
            if question:
                question_text = question.get_text(strip=True)
                question_text = question_text[:-1]
                question.extract()
                answer_text = li.get_text(strip=True)
                info_list.append((question_text, answer_text))

        for item in info_list:
            text = f"{item[1]}  :\u200e{item[0]}"
            canvas.create_text(posX, posY, anchor="ne", text=text, fill="#FFFFFF", font=suez_one_font_Small)
            if posY >= 459:
                posY = 132
                posX = 283
            else:
                posY += 20  # רווח בין השורות
        posY = 500
        posX = 585

        rows = soup.find_all('tr')
        relevant_data = []

        for row in rows:
            cells = row.find_all('td')  # קבלת כל ה-TD בשורה
            if not cells:  # אם השורה ריקה, ממשיכים
                continue

            # בדיקת אורך הטקסט בכל תא
            for cell in cells:
                text = cell.get_text(strip=True)
                if len(text) > 20:  # אם יש טקסט ארוך מ-20 תווים
                    break
            else:
                # אם לא נשברנו, מוסיפים את השורה
                relevant_data.append([cell.get_text(strip=True) for cell in cells])
                continue
            break  # שבירת הלולאה הראשית אם נמצא טקסט ארוך מ-20 תווים

        print("Filtered relevant data:", relevant_data)
        # הדפסת הנתונים הרלוונטיים
        for item in relevant_data:
            text = f"בעלות {item[2]} {item[1]} :\u200e{item[0]} "
            canvas.create_text(posX, posY, anchor="ne", text=text, fill="#FFFFFF", font=suez_one_font_Small)
            if posY >= 700:
                posY = 500
                posX = 283
            else:
                posY += 20


