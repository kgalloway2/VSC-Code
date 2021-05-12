from tkinter import *
from tkinter.ttk import *
from urllib.request import urlopen
import io
from PIL import Image, ImageTk

root = Tk()
root.title("Card Display")
root.geometry("1366x690")

card_selecter = Combobox()


photo_url = "https://c1.scryfall.com/file/scryfall-cards/normal/front/1/c/1ce91e38-4601-4354-ad1b-2c5c1c70da17.jpg?1562551661"
card_page = urlopen(photo_url)
card_picture = io.BytesIO(card_page.read())
pil_img = Image.open(card_picture)
tk_img = ImageTk.PhotoImage(pil_img)

label = Label(root, image=tk_img)
label.grid(column=0,row=0)

mainloop()

