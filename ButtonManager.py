import threading
import time
import tkinter as tk
import webbrowser

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, Label, messagebox
from tkinter.font import Font
import json
from datetime import datetime
import requests
import itertools

from ImageSlider import ImageSlider


class ButtonManager:
    def __init__(self, canvas):
        self.canvas = canvas
        self.text_items = []
        self.text_data = []
        self.history = self.readHistory()
        self.image_slider = None
        self.loading_gif_frames = [tk.PhotoImage(file='assets/frame0/Loading.gif', format='gif -index %i' % i) for i in range(63)]
        self.loading_gif = itertools.cycle(self.loading_gif_frames)
        self.loading_item = None
        self.verified_gif_frames = [tk.PhotoImage(file='assets/frame0/verified.gif', format='gif -index %i' % i) for i in range(73)]
        self.verified_gif = itertools.cycle(self.verified_gif_frames)
        self.verified_item = None




    def setImages(self,images):
        self.image_slider = images
    def WrongNumber(self,number):
        messagebox.showerror("שגיאה", "לא קיים מספר רכב במערכת עבור מספר זה: "+number)

    def agraCalculation(self,yearsOnRoad,AgraLevel):
        AgraLevel= str(AgraLevel)
        agra = "לא זמין"
        if AgraLevel == "1":
            if yearsOnRoad < 4:
                agra = 1194
            elif yearsOnRoad < 7:
                agra = 1046
            elif yearsOnRoad < 10:
                agra = 917
            elif yearsOnRoad >= 10:
                agra = 801
        elif AgraLevel == "2":
            if yearsOnRoad < 4:
                agra = 1519
            elif yearsOnRoad < 7:
                agra = 1325
            elif yearsOnRoad < 10:
                agra = 1161
            elif yearsOnRoad >= 10:
                agra = 1012
        elif AgraLevel == "3":
            if yearsOnRoad < 4:
                agra = 1831
            elif yearsOnRoad < 7:
                agra = 1602
            elif yearsOnRoad < 10:
                agra = 1403
            elif yearsOnRoad >= 10:
                agra = 1224
        elif AgraLevel == "4":
            if yearsOnRoad < 4:
                agra = 2185
            elif yearsOnRoad < 7:
                agra = 1857
            elif yearsOnRoad < 10:
                agra = 1580
            elif yearsOnRoad >= 10:
                agra = 1224
        elif AgraLevel == "5":
            if yearsOnRoad < 4:
                agra = 2502
            elif yearsOnRoad < 7:
                agra = 2061
            elif yearsOnRoad < 10:
                agra = 1701
            elif yearsOnRoad >= 10:
                agra = 1406
        elif AgraLevel == "6":
            if yearsOnRoad < 4:
                agra = 3552
            elif yearsOnRoad < 7:
                agra = 2664
            elif yearsOnRoad < 10:
                agra = 1998
            elif yearsOnRoad >= 10:
                agra = 1495
        elif AgraLevel == "7":
            if yearsOnRoad < 4:
                agra = 5062
            elif yearsOnRoad < 7:
                agra = 3542
            elif yearsOnRoad < 10:
                agra = 2479
            elif yearsOnRoad >= 10:
                agra = 1737
        return agra
    def AmountOfCars(self, ModelYear, degem,demgem_cd):
        base_url = "https://data.gov.il/api/3/action/datastore_search"
        resource_id = "5e87a7a1-2f6f-41c1-8aec-7216d52a6cf6"
        degem = str(degem)
        ModelYear = str(ModelYear)
        demgem_cd = str(demgem_cd)
        params = {
            "resource_id": "5e87a7a1-2f6f-41c1-8aec-7216d52a6cf6",
            "filters": json.dumps({
                "degem_nm": degem,
                "shnat_yitzur": ModelYear,
                "degem_cd": demgem_cd
            })
        }


        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            records = response.json()["result"]["records"]
            if records:
                onRoad = 0
                offRoad = 0
                for record in records:
                    amount = record.get("mispar_rechavim_pailim", "לא זמין")
                    offamount = record.get("mispar_rechavim_le_pailim", "לא זמין")
                    if amount != "לא זמין":
                        onRoad += int(amount)
                    if offamount != "לא זמין":
                        offRoad += int(offamount)

                return onRoad, offRoad
            else:
                return None
        except requests.exceptions.RequestException as err:
            print(f"Error: {err}")

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
            URL = f"https://wa.me/+972{phone_number[1:10]}/?text=שלום לגבי הרכב אשמח לדעת עוד פרטים"
            webbrowser.open(URL)
        except ValueError:
            print("Please enter a valid number")

    def show_loading(self):
        self.loading_item = self.canvas.create_image(65,300, anchor="nw", image=next(self.loading_gif))
        self.animate_loading()

    def show_loadingVerified(self):
        self.verified_item = self.canvas.create_image(100, 300, anchor="nw", image=next(self.verified_gif))
        self.animate_Verified()
    def hide_loading(self):
        if self.loading_item:
            self.canvas.delete(self.loading_item)
            self.loading_item = None
            self.canvas.update()
    def hide_loadingVerified(self):
        if self.verified_item:
            self.canvas.delete(self.verified_item)
            self.verified_item = None
            self.canvas.update()
    def animate_loading(self):
        if self.loading_item:
            self.canvas.itemconfig(self.loading_item, image=next(self.loading_gif))
            self.canvas.after(100, self.animate_loading)
    def animate_Verified(self):
        if self.verified_item:
            self.canvas.itemconfig(self.verified_item, image=next(self.verified_gif))
            self.canvas.after(100, self.animate_Verified)
    def open_about_window(self):
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
    def clear_text(self):
        for text_id in self.text_items:
            self.canvas.delete(text_id)
        self.text_items = []


    def animate_loading(self):
        if self.loading_item:
            self.canvas.itemconfig(self.loading_item, image=next(self.loading_gif))
            self.canvas.after(100, self.animate_loading)
    def animate_Verified(self):
        if self.verified_item:
            self.canvas.itemconfig(self.verified_item, image=next(self.verified_gif))
            self.canvas.after(100, self.animate_Verified)
    def display_text(self):
        for item in self.text_data:
            posX, posY, anchor, text, fill, font = item
            self.text_items.append(self.canvas.create_text(posX, posY, anchor=anchor, text=text, fill=fill, font=font))
        self.text_data = []

    def Display_Car_Details(self, entry_carNumber, canvas,windows):
        if not entry_carNumber or not entry_carNumber.isdigit() or len(entry_carNumber) < 6 or len(entry_carNumber) > 8:
            messagebox.showerror("שגיאה", "בדוק את מספר הרכב שהזנת")
            return
        if self.image_slider:
            self.clear_text()
            self.image_slider.delete_images()
        self.show_loading()
        self.saveHistory(entry_carNumber)
        thread = threading.Thread(target=self.get_car_details, args=(entry_carNumber,canvas,windows))
        thread.start()

    def get_car_details(self, entry_carNumber, canvas,window):
        #~~~~~~~~~~~~~~~~~~~~~~~~~API~~~~~~~~~~~~~~~~~~~~~~~~~~~
        base_url = "https://data.gov.il/api/3/action/datastore_search"
        resource_idInfo = "053cea08-09bc-40ec-8f7a-156f0677aff3"
        resource_idOwn = "bb2355dc-9ec7-4f06-9c3f-3344672171da"
        resourse_idAmount = "5e87a7a1-2f6f-41c1-8aec-7216d52a6cf6"
        resourse_Prices = "39f455bf-6db0-4926-859d-017f34eacbcb"
        resource_TavNeche = "c8b9f9c8-4612-4068-934f-d4acd2e3c06e"
        resourse_CarInfo = "142afde2-6228-49f9-8a29-9b6c3a0cbe40"
        resourseLastKm = "56063a99-8a3e-4ff4-912e-5966c0279bad"
#~~~~~~~~~~~~~~~~~~~~~~~~Font~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        suez_one_font_Small = Font(family="Segoe UI Bold", size=11)
        suez_one_font_Smallest = Font(family="Segoe UI Bold", size=8)
        suez_one_font_ = Font(family="Arial Bold Italic", size=13)
        suez_one_font_Big = Font(family="Arial Bold Italic", size=16)

#~~~~~~~~~~~~~~~~~~~~~~~~~HistorySaving~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~CAR INFO~~~~~~~~~~~~~~~~~~~~~~~~~~~

        params={
            "resource_id": resource_idInfo,
            "q": entry_carNumber
        }
        try :
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            records = response.json()["result"]["records"]
            if records:
                for record in records:
                    mispar_rechev = record.get("mispar_rechev", "לא זמין")
                    tozeret_nm = record.get("tozeret_nm", "0")
                    ramat_gimur = record.get("ramat_gimur", "לא זמין")
                    shnat_yitzur = record.get("shnat_yitzur", "לא זמין")
                    tokef_dt = record.get("tokef_dt", "לא זמין")
                    baalut = record.get("baalut", "לא זמין")
                    misgeret = record.get("misgeret", "לא זמין")
                    tzeva_rechev = record.get("tzeva_rechev", "לא זמין")
                    zmig_kidmi = record.get("zmig_kidmi", "לא זמין")
                    zmig_ahori = record.get("zmig_ahori", "לא זמין")
                    sug_delek = record.get("sug_delek_nm", "לא זמין")
                    moed_aliya_lakvish = record.get("moed_aliya_lakvish", "לא זמין")
                    degem = record.get("kinuy_mishari", "לא זמין")
                    kvutzat_zihum = record.get("kvutzat_zihum", "לא זמין")
                    degem_nm = record.get("degem_nm", "לא זמין")
                    degem_cd = record.get("degem_cd", "לא זמין")
                #~~~~~~~~~~~~~~~~~~~~~~~~~CAR HAND~~~~~~~~~~~~~~~~~~~~~~~~~~~
                params = {
                    "resource_id": resource_idOwn,
                    "q": entry_carNumber
                }
                response = requests.get(base_url, params=params)
                response.raise_for_status()
                records = response.json()["result"]["records"]
                i = 0
                posY = 530
                posX = 590
                if records:
                    for record in records:
                        baalut = record.get("baalut", "לא זמין")
                        baalut_dt = record.get("baalut_dt", "לא זמין")
                        if(baalut_dt != "לא זמין"):
                            baalut_dt =str(baalut_dt)
                            baalutData = f"שינוי בעלות בתאריך: {baalut_dt[4:]}/{baalut_dt[:4]} - {baalut}"
                            if baalut != "סוחר":
                                self.text_data.append((posX, posY, "ne", f"\u200e{baalutData} (0{i})","#FFFFFF", suez_one_font_Small))
                                if posY >= 600:
                                    posY = 510
                                    posX = posX - 290
                                posY += 20
                                i += 1
                i-=1
                if not records:
                    self.text_data.append((590, posY, "ne", "לא זמין", "#FFFFFF",suez_one_font_Small))

                #~~~~~~~~~~~~~~~~~~~~~~~~~AmountOfCars~~~~~~~~~~~~~~~~~~~~~~~~~~~
                AmountOfCars = self.AmountOfCars(shnat_yitzur,degem_nm,degem_cd)
                if AmountOfCars is not None:
                    OnRoad, OffRoad = AmountOfCars
                else:
                    OnRoad = "לא זמין"
                    OffRoad = "לא זמין"
                #~~~~~~~~~~~~~~~~~~~~~~~~~KmLastTest~~~~~~~~~~~~~~~~~~~~~~~~~~~
                try:
                    params = {
                        "resource_id": resourseLastKm,
                        "q": entry_carNumber
                    }
                    response = requests.get(base_url, params=params)
                    response.raise_for_status()
                    records = response.json()["result"]["records"]
                    if records:
                        for record in records:
                            kilometer_test_aharon = record.get("kilometer_test_aharon", "לא זמין")
                            rishum_rishon_dt = record.get("rishum_rishon_dt", "לא זמין")
                            if rishum_rishon_dt != "לא זמין":
                                rishum_rishon_dt =str(rishum_rishon_dt)
                                rishum_rishon_dt = f"עדכון אחרון בתאריך:  {rishum_rishon_dt[:11]} {kilometer_test_aharon} ק''מ"
                                self.text_data.append((350, 480, "ne", f"\u200e{rishum_rishon_dt}","#FFFFFF", suez_one_font_))
                except requests.exceptions.RequestException as err:
                    print(f"Error: {err}")
                #~~~~~~~~~~~~~~~~~~~~~~~~~TavNeche~~~~~~~~~~~~~~~~~~~~~~~~~~~
                try:

                    params = {
                        "resource_id": resource_TavNeche,
                        "q": entry_carNumber
                        }
                    response = requests.get(base_url, params=params)
                    response.raise_for_status()
                    records = response.json()["result"]["records"]
                    tav_neche = "X"
                    sug_tav = "X"
                    if records:
                        for record in records:
                            tav_neche = record.get("MISPAR RECHEV", "X")
                            sug_tav = record.get("SUG TAV", "X")

                except requests.exceptions.RequestException as err:
                    print(f"Error: {err}")
                    tav_neche = "לא זמין"
                    sug_tav = "לא זמין"

                #~~~~~~~~~~~~~~~~~~~~~~~~~CarInfo~~~~~~~~~~~~~~~~~~~~~~~~~~~
                try:
                    params = {
                        "resource_id": resourse_CarInfo,
                        "filters":json.dumps({
                            "degem_nm": degem_nm,
                            "shnat_yitzur": shnat_yitzur,
                            "ramat_gimur": ramat_gimur
                        })
                    }
                    response = requests.get(base_url, params=params)
                    response.raise_for_status()
                    records = response.json()["result"]["records"]
                    if records:
                        for record in records:
                            kvuzat_agra_cd = record.get("kvuzat_agra_cd", "לא זמין")
                            nefah_manoa = record.get("nefah_manoa", "לא זמין")
                            mishkal_kolel = record.get("mishkal_kolel", "לא זמין")
                            hanaa_nm = record.get("hanaa_nm", "לא זמין")
                            mazgan_ind = record.get("mazgan_ind", "לא זמין")
                            abs_ind = record.get("abs_ind", "לא זמין")
                            kariot_avir_source = record.get("kariot_avir_source", "לא זמין")
                            merkav = record.get("merkav", "לא זמין")
                            mispar_dlatot = record.get("mispar_dlatot", "לא זמין")
                            koah_sus = record.get("koah_sus", "לא זמין")
                            mispar_moshavim = record.get("mispar_moshavim", "לא זמין")
                            kosher_grira_im_blamim = record.get("kosher_grira_im_blamim", "לא זמין")
                            kosher_grira_bli_blamim = record.get("kosher_grira_im_blamim", "לא זמין")
                            automatic_ind = record.get("automatic_ind", "לא זמין")
                            halon_bagg_ind = record.get("halon_bagg_ind", "לא זמין")

                        if abs_ind == 1:abs_ind = "V"
                        if automatic_ind == 1:automatic_ind = "V"
                        elif automatic_ind == 0 : automatic_ind = "X"
                        if mazgan_ind == 1:mazgan_ind = "V"
                        elif mazgan_ind == 0 : mazgan_ind = "X"
                        if halon_bagg_ind == 1:halon_bagg_ind = "V"
                        else: halon_bagg_ind = "X"

                        yearsOnRoad = datetime.now().year - shnat_yitzur
                        agra = self.agraCalculation(yearsOnRoad, kvuzat_agra_cd)
                        agra = f"{str(agra)} ₪"



                except requests.exceptions.RequestException as err:
                    print(f"Error: {err}")

                #~~~~~~~~~~~~~~~~~~~~~~~~~CarReview~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                base_url = f"https://autoboom.co.il/api/check_car/{entry_carNumber}"
                try:
                    params = {
                        "resource_id": resourse_CarInfo,
                        "translation": "he",
                        "size[]": ["300x300", "200x200", "800x800", "1200x1200"]
                    }

                    response = requests.get(base_url, params=params)
                    response.raise_for_status()
                    data = response.json()
                    carInfo  = []
                    top_speed = data.get("success", {}).get("modification", {}).get("top_speed", {}).get("value","לא זמין")
                    acceleration_to_100 =(data.get("success", {}).get("modification", {}).get("acceleration_to_100",{}).get("value", "לא זמין"))
                    maximum_power_rpm =(data.get("success", {}).get("modification", {}).get("maximum_power_rpm",{}).get("value", "לא זמין"))
                    fuel_tank_capacity = (data.get("success", {}).get("modification", {}).get("fuel_tank_capacity",{}).get("value", "לא זמין"))
                    fuel_consumption_mixed = (data.get("success", {}).get("modification", {}).get("fuel_consumption_mixed",{}).get("value", "לא זמין"))
                    if fuel_consumption_mixed is not None and fuel_consumption_mixed > 0:
                        fuel_mixed = f"{(100 / fuel_consumption_mixed):.2f} ק''מ לליטר"
                    else:
                        fuel_mixed = "לא זמין"

                    records = response.json()["success"]["photos"]
                    image_urls = []
                    rating = []
                    image_urlsBigger = []
                    for record in records:
                        if "300x300" in record and "1200x1200" in record:
                            image_urls.append(record["300x300"]["url"])
                            image_urlsBigger.append(record["1200x1200"]["url"])
                    self.text_data.append((425, 855, "ne", " © Images provided by Autoboom. All rights reserved by their respective owners.", "#FFFFFF", suez_one_font_Smallest))

                    records = response.json()["success"]["vehicle"]
                    rating.append(data.get("success", {}).get("body", {}).get("rating", "לא זמין"))
                    rating.append(data.get("success", {}).get("configuration", {}).get("rating", "לא זמין"))
                    rating.append(data.get("success", {}).get("vehicle", {}).get("safety_rating", "לא זמין").get("value", "לא זמין"))
                    rating.append(data.get("success", {}).get("body", {}).get("generation", "לא זמין").get("rating", "לא זמין"))


                    review_count = data.get("success", {}).get("body", {}).get("rating", {})

                except requests.exceptions.RequestException as err:
                    print(f"Error: {err}")
                    car_review = "לא זמין"
                    image_urls = []
                    image_urlsBigger = []
                #~~~~~~~~~~~~~~~~~~~~~~~~~Reviews~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                #SOONN
                #~~~~~~~~~~~~~~~~~~~~~~~~~DisplayInfo~~~~~~~~~~~~~~~~~~~~~~~~~~~
                try:
                    shnat_yitzur = int(shnat_yitzur)
                except ValueError:
                    shnat_yitzur = 0
                car_info = [
                    (":מספר רכב", mispar_rechev),
                    (":תוצרת", tozeret_nm),
                    (":רמת גימור", ramat_gimur),
                    (":תוקף רשיון", tokef_dt),
                    (":בעלות נוכחית", baalut),
                    (":שלדה", misgeret),
                    (":צבע רכב", tzeva_rechev),
                    (":צמיג קדמי", zmig_kidmi),
                    (":צמיג אחורי", zmig_ahori),
                    (":סוג דלק", sug_delek),
                    (":עלייה לכביש", moed_aliya_lakvish),
                    (":דגם", degem),
                    (":האם ירד מהכביש", "X"),
                    (":האם קיים ריקול (קריאת שירות)", "X"),
                    (":מספר הרכבים שעל הכביש", OnRoad),
                    (":מספר הרכבים שירדו מהכביש", OffRoad),
                    (":תו נכה", tav_neche),
                    (":קבוצת אגרה", kvuzat_agra_cd),
                    (":אגרה שנתית", agra),
                    (":נפח מנוע",nefah_manoa ),
                    (":משקל כולל", mishkal_kolel),
                    (":הנעה", hanaa_nm),
                    (":מרכב", merkav),
                    (":מספר דלתות", mispar_dlatot),
                    (":כוח סוס", koah_sus),
                    (":מספר מושבים", mispar_moshavim),
                    (":כשר גרירה עם בלמים", kosher_grira_im_blamim),
                    (":כשר גרירה בלי בלמים", kosher_grira_bli_blamim),
                    (":הספק מירבי בסל''ד", maximum_power_rpm),
                    (":תאוצה 0 ל-100 קמ''ש","שניות "+ str(acceleration_to_100) ),
                    (":צריכת דלק משולבת", fuel_mixed),
                    (":תיבת הילוכים אוטומטית", automatic_ind),
                    (":קיבולת מיכל דלק","ליטר " +str(fuel_tank_capacity)),
                    (":מהירות מרבית", top_speed)

                ]

                params = [
                    {"resource_id": resourse_idAmount,"degem_nm": degem_nm},
                    {"resource_id": resource_idOwn, "q": entry_carNumber},
                ]

                posX = 585
                posY = 132
                self.text_data.append((515.0, 112.0, "nw", ":פרטי רכב", "#FFFFFF",suez_one_font_))
                self.text_data.append((197.0, 111.0, "nw", ":מידע נוסף", "#FFFFFF",suez_one_font_))

                for label, value in car_info:
                    self.text_data.append((posX, posY, "ne", label, "#FFFFFF",suez_one_font_Small))
                    self.text_data.append((posX -277, posY,"nw",value, "#FFFFFF",suez_one_font_Small))
                    posY += 20
                    if posY >= 470:
                        posY= 132
                        posX = 295

                ''''
                #New Version update soon
                if rating >= 4:
                    colorRating = "#36c316"
                elif rating < 4:
                    colorRating = "#fbc153"
                elif rating < 2:
                    colorRating = "#f02a2a"
                self.text_data.append((140, 480, "ne", f"⭐{rating}({review_count})", colorRating,suez_one_font_Big))
                '''
                self.text_data.append((590, 490, "ne", ":היסטורית בעלות", "#FFFFFF", suez_one_font_))
                self.text_data.append((590, 510, "ne",f"יד: 0{i}", "#FFFFFF",suez_one_font_Small))

                i = 0
                posY = 700
                for info in carInfo:
                    self.text_data.append((500, posY, "ne",info , "#FFFFFF",suez_one_font_Big))
                    posY +=40
            else:
                self.WrongNumber(entry_carNumber)
                self.hide_loading()
                return
            #~~~~~~~~~~~~~~~~~~~~~~~~~ImageSlider~~~~~~~~~~~~~~~~~~~~~~~~~~~
            self.hide_loading()
            self.show_loadingVerified()
            time.sleep(2)
            slider = ImageSlider(window, canvas, image_urls, image_urlsBigger)
            self.setImages(slider)
            self.hide_loadingVerified()
            self.display_text()

            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        except requests.exceptions.RequestException as err:
            print(f"Error: {err}")
            self.hide_loading()

    def HistoryWindow(self, window):
        global background_image
        try:

            history_window = Toplevel()
            history_window.resizable(False, False)
            history_window.title("היסטוריה")
            history_window.geometry("300x500")


            canvas = Canvas(history_window, width=300, height=500)
            canvas.pack(fill="both", expand=True)
            background_image = PhotoImage(file="assets/frame0/Background-History.png")
            canvas.create_image(0, 0, image=background_image, anchor="nw")
            canvas.create_text(150, 30, text=":היסטורית חיפושים", font=("Segoe UI Bold", 12), fill="White",
                               justify="center")

            listbox = tk.Listbox(history_window, height=10, bg="grey19", fg="white",justify="center", font=("Segoe UI Bold", 12))
            listbox.place(x=50, y=70, width=200)

            for item in self.history:
                listbox.insert(tk.END, item)


            def on_select(event):
                selected_index = listbox.curselection()
                if selected_index:
                    selected_item = listbox.get(selected_index)
                    print(f"Selected: {selected_item}")
                    self.Display_Car_Details(selected_item, self.canvas,window)
                    history_window.destroy()

            listbox.bind("<<ListboxSelect>>", on_select)

        except Exception as e:
            print(f"An error occurred: {e}")

    def saveHistory(self, carNumber):
        try:
            with open("History.txt", "a") as file:
                if carNumber not in self.history:
                    self.history.append(carNumber)
                    file.write(carNumber + "\n")


        except Exception as e:
            print(f"Error saving history: {e}")

    def readHistory(self):
        try:
            with open("History.txt", "r") as file:
                lines = file.readlines()
                return [line.strip() for line in lines]
        except FileNotFoundError:
            with open("History.txt", "w") as file:
                return []
