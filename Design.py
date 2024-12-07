from pathlib import Path
import os
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter.font import Font
import os
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("600x700")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg="black",
    height = 700,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
suez_one_font = Font(family="Suez One", size=17)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    300.0,
    350.0,
    image=image_image_1
)

canvas.create_text(
    427.0,
    16.0,
    anchor="nw",
    text=":הכנס מספר רכב ",
    fill="#FFFFFF",
    font=suez_one_font
)

canvas.create_text(
    317.0,
    623.0,
    anchor="nw",
    text=":שלח הודעת ווצאפ למספר",
    fill="#FFFFFF",
    font=suez_one_font
)

canvas.create_rectangle(
    41.0,
    101.9999890626442,
    558.0,
    103.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    41.0,
    617.9999890626442,
    558.0,
    619.0,
    fill="#FFFFFF",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    window,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    bg="grey19",  # ודא שהרקע של הכפתור תואם לרקע החלון
    activebackground="grey19" # רקע פעיל תואם לרקע החלון
)
button_1.place(
    x=171.0,
    y=60.0,
    width=257.0,
    height=36.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    window,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat",
    bg="grey19",           # ודא שהרקע של הכפתור תואם לרקע החלון
    activebackground="grey19" # רקע פעיל תואם לרקע החלון
)
button_2.place(
    x=11.0,
    y=41.0,
    width=92.0,
    height=51.56756591796875
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    window,
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat",
    bg="grey19",  # ודא שהרקע של הכפתור תואם לרקע החלון
    activebackground="grey19" # רקע פעיל תואם לרקע החלון
)
button_3.place(
    x=17.0,
    y=9.0,
    width=75.0,
    height=22.37837791442871
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    window,
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat",
    bg="grey19",  # ודא שהרקע של הכפתור תואם לרקע החלון
    activebackground="grey19" # רקע פעיל תואם לרקע החלון
)
button_4.place(
    x=199.0,
    y=661.0,
    width=216.0,
    height=33.08108139038086
)

canvas.create_rectangle(
    298.9999999431105,
    125.0,
    300.0,
    425.0,
    fill="#FFFFFF",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    309.5,
    44.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="white",
    fg="#000716",
    highlightthickness=0

)
entry_1.place(
    x=213.0,
    y=20.0,
    width=192.0,
    height=22.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    199.0,
    650.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="white",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=92.0,
    y=629.0,
    width=208.0,
    height=21.0
)
suez_one_font_Small = Font(family="Suez One", size=11)
canvas.create_text(
    535.0,
    112.0,
    anchor="nw",
    text="פרטי רכב",
    fill="#FFFFFF",
    font=suez_one_font_Small
)

canvas.create_text(
    223.0,
    111.0,
    anchor="nw",
    text="מידע נוסף", 
    fill="#FFFFFF",
    font=suez_one_font_Small

)

window.resizable(False, False)
window.mainloop()
