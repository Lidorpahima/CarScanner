import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from tkinter import ttk
class ImageSlider:
    def __init__(self, root, canvas, image_urls, image_urlsBigger):
        self.root = root
        self.canvas = canvas
        self.image_urls = image_urls
        self.image_urlsBigger = image_urlsBigger
        self.current_index = 0
        self.images = []
        self.buttons = []
        self.auto_slide_enabled = True
        self.remaining_time = 3000
        self.time_step = 100
        self.progress = 0

        self.style = ttk.Style(root)
        self.style.theme_use('default')
        self.style.configure("success.Striped.Horizontal.TProgressbar",
                             troughcolor="gray19",
                             background="green",
                             lightcolor="lime",
                             darkcolor="darkgreen")
        self.style.layout("success.Striped.Horizontal.TProgressbar",
                          [('Horizontal.Progressbar.trough',
                            {'children': [('Horizontal.Progressbar.pbar', {'side': 'left', 'sticky': 'ns'})],
                             'sticky': 'nswe'}),
                           ('Horizontal.Progressbar.label', {'sticky': ''})])

        # פס זרימה
        self.progress_bar = ttk.Progressbar(root, orient="horizontal", mode="determinate", length=300,
                                            style="success.Striped.Horizontal.TProgressbar")
        self.progress_bar.place(x=300, y=840, anchor="center")
        self.progress_bar["maximum"] = self.remaining_time

        self.left_button = tk.Button(root, text="⬅️", command=self.previous_image, bg="grey19", fg="#ffffff",
                                     font=("Arial", 16))
        self.left_button.place(x=117, y=740, anchor="center")

        self.right_button = tk.Button(root, text="➡️", command=self.next_image, bg="grey19", fg="#ffffff",
                                      font=("Arial", 16))
        self.right_button.place(x=480.0, y=740, anchor="center")
        self.buttons.append(self.left_button)
        self.buttons.append(self.right_button)

        self.pause_button = tk.Button(root, text="⏯", command=self.toggle_auto_slide, bg="grey19", fg="#ffffff",
                                      font=("Arial", 16))
        self.pause_button.place(x=117, y=805, anchor="center")



        self.show_image()

        self.auto_slide()

    def load_image_from_url(self, url):
        try:
            response = requests.get(url)
            image_data = Image.open(BytesIO(response.content))
            return image_data
        except Exception as e:
            print(f"Error loading image: {e}")

    def delete_images(self):
        for button in self.buttons:
            button.destroy()
        for image_id in self.images:
            self.canvas.delete(image_id)
        self.buttons.clear()
        self.images.clear()

    def show_image(self):
        image_data = self.load_image_from_url(self.image_urls[self.current_index])
        self.original_image = ImageTk.PhotoImage(image_data)

        if hasattr(self, 'current_image_id'):
            self.canvas.delete(self.current_image_id)

        self.current_image_id = self.canvas.create_image(300, 730, anchor="center", image=self.original_image)
        self.images.append(self.current_image_id)
        self.canvas.tag_bind(self.current_image_id, "<Button-1>", self.open_image_in_window)

    def previous_image(self):
        self.current_index = (self.current_index - 1) % len(self.image_urls)
        self.show_image()

    def next_image(self):
        self.current_index = (self.current_index + 1) % len(self.image_urls)
        self.show_image()

    def open_image_in_window(self, event):
        image_window = tk.Toplevel(self.root)
        image_window.geometry("1200x850")
        image_window.geometry("+{}+{}".format(0, 0))
        image_window.title("תמונה בגודל מלא")
        image_window.configure(bg="grey19")

        image_data = self.load_image_from_url(self.image_urlsBigger[self.current_index])
        self.original_image_full = ImageTk.PhotoImage(image_data)

        image_label = tk.Label(image_window, image=self.original_image_full, bg="black")
        image_label.pack(expand=True)

        left_button = tk.Button(image_window, text="⬅️", command=lambda: self.change_image(image_window, -1),
                                bg="grey19", fg="#ffffff", font=("Arial", 16))
        left_button.place(x=50, y=400, anchor="center")

        right_button = tk.Button(image_window, text="➡️", command=lambda: self.change_image(image_window, 1),
                                 bg="grey19", fg="#ffffff", font=("Arial", 16))
        right_button.place(x=1155, y=400, anchor="center")

        close_button = tk.Button(image_window, text="סגור", command=image_window.destroy, bg="grey19", fg="#ffffff")
        close_button.pack(pady=10)

    def change_image(self, image_window, direction):
        self.current_index = (self.current_index + direction) % len(self.image_urls)
        self.show_image()
        image_window.destroy()
        self.open_image_in_window(None)

    def auto_slide(self):
        if self.auto_slide_enabled:
            if self.progress < self.remaining_time:
                self.progress += self.time_step
                self.progress_bar["value"] = self.progress
                self.root.after(self.time_step, self.auto_slide)
            else:
                self.progress = 0
                self.progress_bar["value"] = 0
                self.next_image()
                self.auto_slide()
        else:
            self.progress_bar.stop()

    def toggle_auto_slide(self):
        self.auto_slide_enabled = not self.auto_slide_enabled
        if self.auto_slide_enabled:
            self.pause_button.config(text="▶")
            self.auto_slide()
        else:
            self.pause_button.config(text="❚❚")
            self.progress_bar.stop()
