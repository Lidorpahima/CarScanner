import webbrowser
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, Label, messagebox
from tkinter.font import Font
import requests
import json
from datetime import datetime
import requests
from bs4 import BeautifulSoup


class ButtonManager:
    def __init__(self, canvas):
        self.canvas = canvas
        self.text_items = []
    def clear_canvas(self):
        for text_id in self.text_items:
            self.canvas.delete(text_id)
        self.text_items = []
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
            elif yearsOnRoad > 10:
                agra = 801
        elif AgraLevel == "2":
            if yearsOnRoad < 4:
                agra = 1519
            elif yearsOnRoad < 7:
                agra = 1325
            elif yearsOnRoad < 10:
                agra = 1161
            elif yearsOnRoad > 10:
                agra = 1012
        elif AgraLevel == "3":
            if yearsOnRoad < 4:
                agra = 1831
            elif yearsOnRoad < 7:
                agra = 1602
            elif yearsOnRoad < 10:
                agra = 1403
            elif yearsOnRoad > 10:
                agra = 1224
        elif AgraLevel == "4":
            if yearsOnRoad < 4:
                agra = 2185
            elif yearsOnRoad < 7:
                agra = 1857
            elif yearsOnRoad < 10:
                agra = 1580
            elif yearsOnRoad > 10:
                agra = 1224
        elif AgraLevel == "5":
            if yearsOnRoad < 4:
                agra = 2502
            elif yearsOnRoad < 7:
                agra = 2061
            elif yearsOnRoad < 10:
                agra = 1701
            elif yearsOnRoad > 10:
                agra = 1406
        elif AgraLevel == "6":
            if yearsOnRoad < 4:
                agra = 3552
            elif yearsOnRoad < 7:
                agra = 2664
            elif yearsOnRoad < 10:
                agra = 1998
            elif yearsOnRoad > 10:
                agra = 1495
        elif AgraLevel == "7":
            if yearsOnRoad < 4:
                agra = 5062
            elif yearsOnRoad < 7:
                agra = 3542
            elif yearsOnRoad < 10:
                agra = 2479
            elif yearsOnRoad > 10:
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
    def clear_text(self):
        for text_id in self.text_items:
            self.canvas.delete(text_id)
        self.text_items = []
    def Display_Car_Details(self, entry_carNumber, canvas):
        self.clear_text()
        #~~~~~~~~~~~~~~~~~~~~~~~~~API~~~~~~~~~~~~~~~~~~~~~~~~~~~
        base_url = "https://data.gov.il/api/3/action/datastore_search"
        resource_idInfo = "053cea08-09bc-40ec-8f7a-156f0677aff3"
        resource_idOwn = "bb2355dc-9ec7-4f06-9c3f-3344672171da"
        resourse_idAmount = "5e87a7a1-2f6f-41c1-8aec-7216d52a6cf6"
        resourse_Prices = "39f455bf-6db0-4926-859d-017f34eacbcb"
        resource_TavNeche = "c8b9f9c8-4612-4068-934f-d4acd2e3c06e"
        resourse_CarInfo = "142afde2-6228-49f9-8a29-9b6c3a0cbe40"

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
                hands = []
                handPos = -1
                for record in records:
                    baalut_dt = record.get("baalut_dt", "לא זמין")
                    if(baalut_dt != "לא זמין"):
                        int(baalut_dt)%10
                        handPos = max(handPos, (int(baalut_dt)%10))
                    hands.append(record.get("baalut", "לא זמין"))
                if handPos == -1:
                    handPos = "לא זמין"
                else:
                    handPos = "0"+str(handPos)
                #~~~~~~~~~~~~~~~~~~~~~~~~~AmountOfCars~~~~~~~~~~~~~~~~~~~~~~~~~~~
                AmountOfCars = self.AmountOfCars(shnat_yitzur,degem_nm,degem_cd)
                if AmountOfCars is not None:
                    OnRoad, OffRoad = AmountOfCars
                else:
                    OnRoad = "לא זמין"
                    OffRoad = "לא זמין"
                #~~~~~~~~~~~~~~~~~~~~~~~~~Prices~~~~~~~~~~~~~~~~~~~~~~~~~~~
                params = {
                    "resource_id": resourse_Prices,
                    "filters": json.dumps({
                        "degem_nm": degem_nm,
                        "shnat_yitzur": shnat_yitzur,
                        "degem_cd": degem_cd
                    })
                }
                response = requests.get(base_url, params=params)
                response.raise_for_status()
                records = response.json()["result"]["records"]
                if records:
                    for record in records:
                        price = str(record.get("mehir", "לא זמין"))+ " ש\"ח"
                        shem_yevuan = record.get("shem_yevuan", "לא זמין")
                else:
                    price = "לא זמין"
                    shem_yevuan = "לא זמין"
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
                    print(records)
                    if records:
                        for record in records:
                            kvuzat_agra_cd = record.get("kvuzat_agra_cd", "לא זמין")
                            nefah_manoa = record.get("nefah_manoa", "לא זמין")
                            mishkal_kolel = record.get("mishkal_kolel", "לא זמין")
                            gova = record.get("gova", "לא זמין")
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




                except requests.exceptions.RequestException as err:
                    print(f"Error: {err}")


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
                    (":קבוצת זיהום", kvutzat_zihum),
                    (":האם ירד מהכביש", "X"),
                    (":האם קיים ריקול (קריאת שירות)", "X"),
                    (":מספר הרכבים שעל הכביש", OnRoad),
                    (":מספר הרכבים שירדו מהכביש", OffRoad),
                    (":עלות רכישה בשנת יצור", price),
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
                    (":האם יש ABS", abs_ind),
                    (":האם יש מזגן", mazgan_ind),
                    (":תיבת הילוכים אוטומטית", automatic_ind),
                    (":האם יש חלון בגג", halon_bagg_ind)

                ]

                params = [
                    {"resource_id": resourse_idAmount,"degem_nm": degem_nm},
                    {"resource_id": resource_idOwn, "q": entry_carNumber},
                ]
                suez_one_font_Small = Font(family="Segoe UI Bold", size=11)
                suez_one_font_ = Font(family="Arial Bold Italic", size=13)
                posX = 585
                posY = 132
                self.text_items.append(canvas.create_text(515.0, 112.0, anchor="nw", text=":פרטי רכב", fill="#FFFFFF",font=suez_one_font_))
                self.text_items.append(canvas.create_text(197.0, 111.0, anchor="nw", text=":מידע נוסף", fill="#FFFFFF",font=suez_one_font_))

                for label, value in car_info:
                    self.text_items.append(canvas.create_text(posX, posY, anchor="ne", text=label, fill="#FFFFFF",font=suez_one_font_Small))
                    self.text_items.append(canvas.create_text(posX -277, posY, anchor="nw", text=value, fill="#FFFFFF",font=suez_one_font_Small))
                    posY += 20
                    if posY >= 470:
                        posY= 132
                        posX = 295
                posY =490
                posX = 590
                self.text_items.append(canvas.create_text(590, 490, anchor="ne", text=":היסטורית בעלות", fill="#FFFFFF",
                                                          font=suez_one_font_))
                posY += 20
                self.text_items.append(canvas.create_text(590, posY, anchor="ne", text=f"יד: {handPos}", fill="#FFFFFF",font=suez_one_font_Small))
                posY += 20
                i = len(hands)-1
                for hand in hands:

                    self.text_items.append(canvas.create_text(590, posY, anchor="ne", text=f"\u200e{hand} (0{i})", fill="#FFFFFF",font=suez_one_font_Small))
                    posY += 20
                    i -=1
            else:
                self.WrongNumber(entry_carNumber)


        except requests.exceptions.RequestException as err:
            print(f"Error: {err}")

