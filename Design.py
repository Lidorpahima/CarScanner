from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
from tkinter.font import Font
from ButtonManager import ButtonManager

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class CarScannerApp:
    def __init__(self, window):
        self.window = window
        self.window.geometry("600x1000")
        self.window.configure(bg="#FFFFFF")
        self.app_icon = PhotoImage(file="assets/frame0/CarIcon.png")
        self.window.title("CarScanner")
        self.window.iconphoto(False, self.app_icon)
        self.window.geometry("+{}+{}".format(0, 0))
        self.canvas = Canvas(
            self.window,
            bg="black",
            height=1000,
            width=600,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.suez_one_font = Font(family="Arial Bold Italic", size=17)
        self.background_image = PhotoImage(file=relative_to_assets("Background.png"))
        self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")

        # ENTRY CAR NUMBER TXT
        self.canvas.create_text(
            427.0,
            18.0,
            anchor="nw",
            text=":הכנס מספר רכב ",
            fill="#FFFFFF",
            font=self.suez_one_font
        )
        # ENTRY WHATSAPP NUMBER TXT
        self.canvas.create_text(
            317.0,
            881.5,
            anchor="nw",
            text=":שלח הודעת ווצאפ למספר",
            fill="#FFFFFF",
            font=self.suez_one_font
        )

        # TOP LINE
        self.canvas.create_rectangle(
            41.0,
            104.9999890626442,
            558.0,
            106.0,
            fill="#FFFFFF",
            outline=""
        )

        # BOTTOM LINE
        self.canvas.create_rectangle(
            41.0,
            874.9999890626442,
            558.0,
            875.0,
            fill="#FFFFFF",
            outline=""
        )

        # SEARCH BUTTON
        self.button_image_1 = PhotoImage(file=relative_to_assets("Search.png"))
        self.search_button = Button(
            self.window,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: ButtonManager.Display_Car_Details(self,self.entry_carNumber.get(), self.canvas),
            relief="flat",
            bg="grey19",
            activebackground="grey19"
        )
        self.search_button.place(
            x=171.0,
            y=60.0,
            width=257.0,
            height=36.0
        )

        # HISTORY BUTTON
        self.button_image_2 = PhotoImage(file=relative_to_assets("History.png"))
        self.history_button = Button(
            self.window,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat",
            bg="grey19",
            activebackground="grey19"
        )
        self.history_button.place(
            x=11.0,
            y=41.0,
            width=92.0,
            height=51.56756591796875
        )

        # ABOUT BUTTON
        self.button_image_3 = PhotoImage(file=relative_to_assets("About.png"))
        self.about_button = Button(
            self.window,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: ButtonManager.open_about_window(),
            relief="flat",
            bg="grey19",
            activebackground="grey19"
        )
        self.about_button.place(
            x=17.0,
            y=9.0,
            width=75.0,
            height=22.37837791442871
        )

        # SEND WHATSAPP BUTTON
        self.button_image_4 = PhotoImage(file=relative_to_assets("SendWH.png"))
        self.send_whatsapp_button = Button(
            self.window,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: ButtonManager.send_whatsapp_message(self.entry_phone.get()),
            relief="flat",
            bg="grey19",
            activebackground="grey19"
        )
        self.send_whatsapp_button.place(
            x=199.0,
            y=913.0,
            width=216.0,
            height=33.08108139038086
        )
        #MID LINE
        self.canvas.create_rectangle(
            298.9999999431105,
            125.0,
            300.0,
            469.0,
            fill="#FFFFFF",
            outline=""
        )

        # ENTRY CAR NUMBER
        self.entry_image_1 = PhotoImage(file=relative_to_assets("EntryBoxCarNumber.png"))
        self.entry_bg_1 = self.canvas.create_image(
            309.5,
            44.0,
            image=self.entry_image_1
        )
        self.entry_carNumber = Entry(
            self.window,
            bd=0,
            bg="white",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_carNumber.pack(pady=10)
        self.entry_carNumber.place(
            x=213.0,
            y=20.0,
            width=192.0,
            height=22.0
        )

        # ENTRY WHATSAPP NUMBER
        self.entry_image_2 = PhotoImage(file=relative_to_assets("EntryBoxPhoneNumber.png"))
        self.entry_bg_2 = self.canvas.create_image(
            199.0,
            906.5,
            image=self.entry_image_2
        )

        self.entry_phone = Entry(
            self.window,
            bd=0,
            bg="white",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_phone.place(
            x=92.0,
            y=884.0,
            width=208.0,
            height=21.0
        )

        # YOUR RESPONSIBILITY!
        self.canvas.create_text(
            25, 950,
            anchor="nw",
            text="היישום הנוכחי אינו קשור או אחראי למידע המוצג בו. כל הפרטים והמידע המסופקים באפליקציה מקורם מתוך מקורות\n ,אינטרנטיים שונים, ואחריות השימוש בהם חלה על המשתמש בלבד. אין לראות במידע המוצג ייעוץ מקצועי או מחייב \n.וכל בעיה או נזק שעלול להיגרם כתוצאה מהשימוש במידע זה היא באחריות המשתמש",
            fill="#FFFFFF",
            font=("Arial Italic", 9),
            justify="center"
        )

        self.window.resizable(False, False)

if __name__ == "__main__":
    window = Tk()
    app = CarScannerApp(window)
    window.mainloop()
