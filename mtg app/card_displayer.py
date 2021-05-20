from tkinter import *
from tkinter.ttk import *
from urllib.request import urlopen
import io
from PIL import Image, ImageTk
import ast

# all_cards = open("C:/Users/kgtrm/Documents/VSC Code/mtg app/trimmed_cards.txt")

with open('trimmed_cards.txt', 'r') as f_in:
    pre_all_cards = [line for line in f_in]

pre_all_cards.pop(0)
pre_all_cards[-1] = pre_all_cards[-1][0:-1]


all_cards = []
for card in pre_all_cards:
    all_cards.append((ast.literal_eval(card)))

# print(all_cards[0:3])

root = Tk()
root.title("Decklist Submission Screen")
root.geometry("683x345")

# functions for submission screen

def get_cards():
    unfiltered_cards_string = decklist_entry.get("1.0", "end")
    unfiltered_cards_list = unfiltered_cards_string.split("\n")
    filtered_cards = []
    for line in unfiltered_cards_list:
        if line:
            begin_index = line.index("x") + 2
            end_index = line.index("(") - 1
            new_line = line[begin_index:end_index]
            filtered_cards.append(new_line)
    return filtered_cards

def index_of(card_name):
        card_name = card_name.strip().lower()
        if card_name == '':
            return -1
        for i in range(len(all_cards)):
            if all_cards[i][0]["name"].strip().lower() == card_name:
                return i

def format_cards_for_game(card_list):
    new_card_list = []
    for card in card_list:
        new_card_list.append(all_cards[index_of(card)])
    return new_card_list

decklist_entry = Text()
decklist_entry.grid(column=0,row=0)
decklist_entry['height'] = 21
decklist_entry['width'] = 50

import_decklists_button = Button(root, text='Import Decklists') 
import_decklists_button.configure(command=lambda :begin_game(format_cards_for_game(get_cards())))
import_decklists_button.grid(column=1,row=0)

def begin_game(current_game_cards):
    displayer = Tk()
    displayer.title("Card Display")
    displayer.geometry("1366x690")

    # functions for autocomplete list

    def on_key_release(event):
        value = event.widget.get()
        value = value.strip().lower()

        if value == '':
            data = cards
        else:
            data = []
            for item in cards:
                if value in item["name"].lower():
                    data.append(item)
        
        card_list_update(data)

    def card_list_update(data):
        card_list.delete(0,'end')

        for item in data:
            card_list.insert('end', item["name"])

    def on_select(event):
        print('(event) previous:', event.widget.get('active'))
        print('(event) current:', event.widget.get(event.widget.curselection()))
        print('---')

    # functions for finding photo url of given card

    def index_of(card_name):
        card_name = card_name.strip().lower()
        if card_name == '':
            return -1
        for i in range(len(cards)):
            if cards[i]["name"].strip().lower() == card_name:
                return i

    def url_of(index):
        if index == -1:
            return "https://c1.scryfall.com/file/scryfall-cards/normal/front/0/3/036ef8c9-72ac-46ce-af07-83b79d736538.jpg?1562730661"
        return cards[index]["image_uris"]["normal"]

    def selection():
        if card_list.curselection() == ():
            return -1
        else:
            return card_list.curselection()

    # functions to change shown picture

    def show_picture(card_name):
        if card_name == 'default':
            index_of_card = 0
            photo_url = url_of(index_of_card)
        else:
            index_of_card = index_of(card_name)
            photo_url = url_of(index_of_card)
        ability_list_update(cards[index_of_card])
        card_page = urlopen(photo_url)
        card_picture = io.BytesIO(card_page.read())
        pil_img = Image.open(card_picture)
        tk_img = ImageTk.PhotoImage(pil_img,master=displayer)
        picture = Label(displayer)
        picture.configure(image=tk_img)
        picture.image = tk_img
        picture.place(x=1,y=1)

    # functions for ability list

    def ability_list_update(card):
        ability_list.delete("1.0", "end")
        abilities = card["oracle_text"].split('\n')
        for ability in abilities:
            ability_list.insert('end', ability)
            ability_list.insert('end', "\n\n")

    # widgets for display


    cards = []
    for card in current_game_cards:
        cards.append(card[0])

    card_selecter = Entry(displayer)
    card_selecter.place(x=500,y=1)
    card_selecter.bind('<KeyRelease>', on_key_release)

    card_list = Listbox(displayer)
    card_list.place(x=500,y=25)
    card_list['height'] = 40
    card_list.bind('<<ListBoxSelect>>', on_select)
    card_list_update(cards)

    show_pic_button = Button(displayer, text='Show Selected Card') 
    show_pic_button.configure(command=lambda :show_picture(card_list.get(selection())))
    show_pic_button.place(x=630,y=1)

    ability_list = Text(displayer)
    ability_list.place(x=630,y=25)
    ability_list['height'] = 20
    ability_list['width'] = 20
    ability_list['wrap'] = WORD
    # ability_list.bind('<<ListBoxSelect>>', on_select)
    ability_list_update({"name": "Storm Crow", "scryfall_uri": "https://scryfall.com/card/9ed/100/storm-crow?utm_source=api", "image_uris": {"small": "https://c1.scryfall.com/file/scryfall-cards/small/front/0/3/036ef8c9-72ac-46ce-af07-83b79d736538.jpg?1562730661", "normal": "https://c1.scryfall.com/file/scryfall-cards/normal/front/0/3/036ef8c9-72ac-46ce-af07-83b79d736538.jpg?1562730661", "large": "https://c1.scryfall.com/file/scryfall-cards/large/front/0/3/036ef8c9-72ac-46ce-af07-83b79d736538.jpg?1562730661", "png": "https://c1.scryfall.com/file/scryfall-cards/png/front/0/3/036ef8c9-72ac-46ce-af07-83b79d736538.png?1562730661", "art_crop": "https://c1.scryfall.com/file/scryfall-cards/art_crop/front/0/3/036ef8c9-72ac-46ce-af07-83b79d736538.jpg?1562730661", "border_crop": "https://c1.scryfall.com/file/scryfall-cards/border_crop/front/0/3/036ef8c9-72ac-46ce-af07-83b79d736538.jpg?1562730661"}, "mana_cost": "{1}{U}", "cmc": 2.0, "type_line": "Creature \u2014 Bird", "oracle_text": "Flying (This creature can't be blocked except by creatures with flying or reach.)", "power": "1", "toughness": "2", "colors": ["U"], "color_identity": ["U"], "keywords": ["Flying"], "rulings_uri": "https://api.scryfall.com/cards/036ef8c9-72ac-46ce-af07-83b79d736538/rulings"})

    show_picture('default')

mainloop()