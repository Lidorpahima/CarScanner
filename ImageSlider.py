import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

class ImageSlider:
    def __init__(self, root, canvas, image_urls, image_urlsBigger):
        self.root = root
        self.canvas = canvas
        self.image_urls = image_urls
        self.image_urlsBigger = image_urlsBigger
        self.current_index = 0
        self.images = []
        self.buttons = []
        self.left_button = tk.Button(root, text="⬅️", command=self.previous_image, bg="grey19", fg="#ffffff", font=("Arial", 16))
        self.left_button.place(x=117, y=740, anchor="center")

        self.right_button = tk.Button(root, text="➡️", command=self.next_image, bg="grey19", fg="#ffffff", font=("Arial", 16))
        self.right_button.place(x=480.0, y=740, anchor="center")
        self.buttons.append(self.left_button)
        self.buttons.append(self.right_button)
        self.show_image()

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

        self.current_image_id = self.canvas.create_image(300, 750, anchor="center", image=self.original_image)
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

        # הצגת התמונה בחלון החדש
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