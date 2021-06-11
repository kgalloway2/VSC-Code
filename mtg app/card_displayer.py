from tkinter import *
from tkinter.ttk import *
from urllib.request import urlopen
import io
from PIL import Image, ImageTk
import ast
import os

with open('trimmed_cards.txt', 'r') as f_in:
    pre_all_cards = [line for line in f_in]

pre_all_cards.pop(0)
pre_all_cards[-1] = pre_all_cards[-1][0:-1]

all_cards = []
for card in pre_all_cards:
    all_cards.append((ast.literal_eval(card)))


root = Tk()
root.title("Decklist Submission Screen")
root.geometry("683x345")

# functions for submission screen

def import_decklist():
    deck_name = deck_name_entry.get()
    unfiltered_cards_string = decklist_entry.get("1.0", "end")
    unfiltered_cards_list = unfiltered_cards_string.split("\n")
    filtered_cards = []
    for line in unfiltered_cards_list:
        if line:
            begin_index = line.index("x") + 2
            end_index = line.index("(") - 1
            new_line = line[begin_index:end_index]
            filtered_cards.append(new_line)
    with open("saved_decks.txt", 'a') as decks:
        decks.write("*** " + deck_name + '\n')
        for card in filtered_cards:
            decks.write(str(card) + '\n')
    saved_decks_list.insert('end', deck_name)

def index_of(card_name):
        card_name = card_name.strip().lower()
        if card_name == '':
            return -1
        for i in range(len(all_cards)):
            if all_cards[i][0]["name"].strip().lower() == card_name:
                return i

def format_cards_for_game(card_list):
    card_list.sort()
    card_list = list(dict.fromkeys(card_list))
    new_card_list = []
    for card in card_list:
        new_card_list.append(all_cards[index_of(card)])
    return new_card_list

def get_decklists():
    decklist_indices = saved_decks_list.curselection()
    deck_names = []
    card_list = []
    for i in decklist_indices:
        deck_names.append(saved_decks_list.get(i))
    for deck in deck_names:
        with open("saved_decks.txt", 'r') as decks_file:
            add_to_list = False
            for line in decks_file:
                if line == "*** " + deck:
                    add_to_list = True
                elif line[0:3] == "***":
                    add_to_list = False
                elif add_to_list:
                    card_list.append(line)
    return card_list

def delete_deck_function():
    decklist_indices = saved_decks_list.curselection()
    deck_names = []
    new_file = []
    for i in decklist_indices:
        deck_names.append(saved_decks_list.get(i))
    for deck in deck_names:
        with open("saved_decks.txt", 'r') as decks_file:
            keep_line = True
            for line in decks_file:
                if line[0:3] == "***":
                    if line == "*** " + deck:
                        keep_line = False
                    else:
                        keep_line = True
                if keep_line:
                    new_file.append(line)
    os.remove("saved_decks.txt")
    with open("saved_decks.txt", 'w') as new_decks_file:
        for line in new_file:
            new_decks_file.write(str(line))
    for index in decklist_indices:
        saved_decks_list.delete(index)
    


decklist_entry = Text(root)
decklist_entry.place(x=1,y=1)
decklist_entry['height'] = 21
decklist_entry['width'] = 50

saved_label = Label(root, text="Deck Name:")
saved_label.place(x = 406, y = 1)

deck_name_entry = Entry(root)
deck_name_entry.place(x=473,y=1)

import_decklists_button = Button(root, text='Import') 
import_decklists_button.configure(command=lambda :import_decklist())
import_decklists_button.place(x=602,y=0)

saved_label = Label(root, text="Saved Decks:")
saved_label.place(x = 406, y = 110)

deck_names = []
with open('saved_decks.txt', 'r') as decks:
    for line in decks:
        if line[0:3] == "***":
            deck_names.append(line[4:])

saved_decks_list = Listbox(root, selectmode='multiple')
saved_decks_list.place(x = 406, y = 130)
saved_decks_list['height'] = 13
saved_decks_list['width'] = 25
for deck in deck_names:
    saved_decks_list.insert('end', deck)

begin_game = Button(root, text="Start Game")
begin_game.configure(command=lambda :begin_game(format_cards_for_game(get_decklists())))
begin_game.place(x=406,y=60)

delete_deck = Button(root, text="Delete")
delete_deck.configure(command=lambda :delete_deck_function())
delete_deck.place(x=600,y=130)

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
        ability_list.delete(0,'end')
        abilities = card["oracle_text"].split('\n')

        for item in abilities:
            ability_list.insert('end', item)

    # functions for updating the stack

    def add_ability_to_stack(card, ability):
        new_insert = "x1: " + card + ": " + ability
        the_stack.insert("1.0", "\n\n")
        the_stack.insert("1.0", new_insert)

    def delete_ability_from_stack():
        top_ability = the_stack.get("1.0", "3.0")
        first_chars = []
        for i in range(8):
            first_chars.append(top_ability[i:i + 1])
        if first_chars[0] != "x" or (first_chars[1] == "1" and first_chars[2] == ":"):
            the_stack.delete("1.0", "3.0")
        else:
            current_num = ""
            last_index = -1
            for j in first_chars:
                if j in "0123456789":
                    current_num += j
                elif j == ":":
                    last_index = first_chars.index(":")
            current_num = int(current_num) - 1
            new_insert = "x" + str(current_num) + the_stack.get("1.0", "3.0")[last_index:]
            the_stack.delete("1.0", "3.0")
            the_stack.insert("1.0", new_insert)

    def delete_entire_stack():
        the_stack.delete("1.0", "end")

    def add_multi_to_stack(card, ability,num_times):
        new_insert = "x" + str(num_times) + ": " + card + ": " + ability
        the_stack.insert("1.0", "\n\n")
        the_stack.insert("1.0", new_insert)

    def add_card_to_stack(card):
        the_stack.insert("1.0", "\n\n")
        the_stack.insert("1.0", card)

    def add_notes_to_stack(card, ability, notes):
        new_insert = "x1: " + card + ": " + ability + " With notes: " + notes
        the_stack.insert("1.0", "\n\n")
        the_stack.insert("1.0", new_insert)

    # functions for rulings

    def view_rulings(card):
        index = index_of(card)
        rulings_url = cards[index]["rulings_uri"]
        rulings_page = urlopen(rulings_url)
        rulings_string = rulings_page.read().decode('UTF-8')
        rulings_string = rulings_string[:-1]
        rulings_list = rulings_string.split('\"data\":')
        actual_rulings = ast.literal_eval(rulings_list[1])
        rulings = []
        for dictionary in actual_rulings:
            rulings.append(dictionary["comment"])
        
        rulings_page = Tk()
        page_title = "Card Rulings - " + card
        rulings_page.title(page_title)
        rulings_page.geometry("500x500")

        rulings_text = Text(rulings_page)
        rulings_text.place(x=1,y=1)
        rulings_text['height'] = 30
        rulings_text['width'] = 60
        rulings_text['wrap'] = WORD
        
        for ruling in rulings:
            rulings_text.insert("end", ruling)
            rulings_text.insert("end", "\n\n")

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

    show_rulings_button = Button(displayer, text='View Rulings') 
    show_rulings_button.configure(command=lambda :view_rulings(card_list.get(selection())))
    show_rulings_button.place(x=745,y=1)

    ability_list = Listbox(displayer)
    ability_list.place(x=630,y=25)
    ability_list['height'] = 6
    ability_list['width'] = 120
    ability_list.bind('<<ListBoxSelect>>', on_select)
    ability_list_update({"name": "Storm Crow", "scryfall_uri": "https://scryfall.com/card/9ed/100/storm-crow?utm_source=api", "image_uris": {"small": "https://c1.scryfall.com/file/scryfall-cards/small/front/0/3/036ef8c9-72ac-46ce-af07-83b79d736538.jpg?1562730661", "normal": "https://c1.scryfall.com/file/scryfall-cards/normal/front/0/3/036ef8c9-72ac-46ce-af07-83b79d736538.jpg?1562730661", "large": "https://c1.scryfall.com/file/scryfall-cards/large/front/0/3/036ef8c9-72ac-46ce-af07-83b79d736538.jpg?1562730661", "png": "https://c1.scryfall.com/file/scryfall-cards/png/front/0/3/036ef8c9-72ac-46ce-af07-83b79d736538.png?1562730661", "art_crop": "https://c1.scryfall.com/file/scryfall-cards/art_crop/front/0/3/036ef8c9-72ac-46ce-af07-83b79d736538.jpg?1562730661", "border_crop": "https://c1.scryfall.com/file/scryfall-cards/border_crop/front/0/3/036ef8c9-72ac-46ce-af07-83b79d736538.jpg?1562730661"}, "mana_cost": "{1}{U}", "cmc": 2.0, "type_line": "Creature \u2014 Bird", "oracle_text": "Flying (This creature can't be blocked except by creatures with flying or reach.)", "power": "1", "toughness": "2", "colors": ["U"], "color_identity": ["U"], "keywords": ["Flying"], "rulings_uri": "https://api.scryfall.com/cards/036ef8c9-72ac-46ce-af07-83b79d736538/rulings"})

    the_stack = Text(displayer)
    the_stack.place(x=630,y=200)
    the_stack['height'] = 28
    the_stack['width'] = 90
    the_stack['wrap'] = WORD

    add_to_stack_button = Button(displayer, text='Add to stack.')
    add_to_stack_button.configure(command= lambda :add_ability_to_stack(card_list.get(ACTIVE), ability_list.get(ACTIVE)))
    add_to_stack_button.place(x=630, y = 130)

    delete_from_stack_button = Button(displayer, text='Delete top ability from stack.')
    delete_from_stack_button.configure(command=lambda :delete_ability_from_stack())
    delete_from_stack_button.place(x=713, y = 130)

    delete_entire_stack_button = Button(displayer, text='Clear the stack.')
    delete_entire_stack_button.configure(command=lambda :delete_entire_stack())
    delete_entire_stack_button.place(x=879, y = 130)

    stack_info = Label(displayer, text="To remove an ability from the middle of the stack, highlight and delete it.")
    stack_info.place(x=970, y=133)

    add_multiple_to_stack_button = Button(displayer, text='Add to stack times: ')
    add_multiple_to_stack_button.configure(command= lambda :add_multi_to_stack(card_list.get(ACTIVE), ability_list.get(ACTIVE), int(add_multiple_entry.get())))
    add_multiple_to_stack_button.place(x=630, y = 160)
    add_multiple_entry = Entry(displayer, width=3)
    add_multiple_entry.place(x=748, y = 162)

    add_card_to_stack_button = Button(displayer, text='Add card to stack.')
    add_card_to_stack_button.configure(command= lambda :add_card_to_stack(card_list.get(ACTIVE)))
    add_card_to_stack_button.place(x=775, y = 160)

    add_notes_entry = Entry(displayer)
    add_notes_entry.place(x=1015, y = 162)
    add_notes_to_stack_button = Button(displayer, text='Add to stack with note: ')
    add_notes_to_stack_button.configure(command= lambda :add_notes_to_stack(card_list.get(ACTIVE), ability_list.get(ACTIVE), add_notes_entry.get()))
    add_notes_to_stack_button.place(x=880, y = 160)

    show_picture('default')

mainloop()