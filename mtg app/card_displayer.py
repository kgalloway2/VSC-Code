from tkinter import *
from tkinter.ttk import *
from urllib.request import urlopen
import io
from PIL import Image, ImageTk

root = Tk()
root.title("Card Display")
root.geometry("1366x690")

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
    
    list_box_update(data)

def list_box_update(data):
    list_box.delete(0,'end')

    for item in data:
        list_box.insert('end', item["name"])

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
    if list_box.curselection() == ():
        return -1
    else:
        return list_box.curselection()

# functions to change shown picture

def show_picture(card_name):
    if card_name == 'default':
        photo_url = "https://c1.scryfall.com/file/scryfall-cards/normal/front/0/3/036ef8c9-72ac-46ce-af07-83b79d736538.jpg?1562730661"
    else:
        photo_url = url_of(index_of(card_name))
    card_page = urlopen(photo_url)
    card_picture = io.BytesIO(card_page.read())
    pil_img = Image.open(card_picture)
    tk_img = ImageTk.PhotoImage(pil_img)
    picture = Label(root)
    picture.configure(image=tk_img)
    picture.image = tk_img
    picture.grid(column=0,row=0)

# widgets for display

cards = [{"name": "Static Orb", "scryfall_uri": "https://scryfall.com/card/7ed/319/static-orb?utm_source=api", "image_uris": {"small": "https://c1.scryfall.com/file/scryfall-cards/small/front/8/6/86bf43b1-8d4e-4759-bb2d-0b2e03ba7012.jpg?1562242171", "normal": "https://c1.scryfall.com/file/scryfall-cards/normal/front/8/6/86bf43b1-8d4e-4759-bb2d-0b2e03ba7012.jpg?1562242171", "large": "https://c1.scryfall.com/file/scryfall-cards/large/front/8/6/86bf43b1-8d4e-4759-bb2d-0b2e03ba7012.jpg?1562242171", "png": "https://c1.scryfall.com/file/scryfall-cards/png/front/8/6/86bf43b1-8d4e-4759-bb2d-0b2e03ba7012.png?1562242171", "art_crop": "https://c1.scryfall.com/file/scryfall-cards/art_crop/front/8/6/86bf43b1-8d4e-4759-bb2d-0b2e03ba7012.jpg?1562242171", "border_crop": "https://c1.scryfall.com/file/scryfall-cards/border_crop/front/8/6/86bf43b1-8d4e-4759-bb2d-0b2e03ba7012.jpg?1562242171"}, "mana_cost": "{3}", "cmc": 3.0, "type_line": "Artifact", "oracle_text": "As long as Static Orb is untapped, players can't untap more than two permanents during their untap steps.", "colors": [], "color_identity": [], "keywords": [], "rulings_uri": "https://api.scryfall.com/cards/86bf43b1-8d4e-4759-bb2d-0b2e03ba7012/rulings"}, 
{"name": "Sensory Deprivation", "scryfall_uri": "https://scryfall.com/card/m14/71/sensory-deprivation?utm_source=api", "image_uris": {"small": "https://c1.scryfall.com/file/scryfall-cards/small/front/7/0/7050735c-b232-47a6-a342-01795bfd0d46.jpg?1562830795", "normal": "https://c1.scryfall.com/file/scryfall-cards/normal/front/7/0/7050735c-b232-47a6-a342-01795bfd0d46.jpg?1562830795", "large": "https://c1.scryfall.com/file/scryfall-cards/large/front/7/0/7050735c-b232-47a6-a342-01795bfd0d46.jpg?1562830795", "png": "https://c1.scryfall.com/file/scryfall-cards/png/front/7/0/7050735c-b232-47a6-a342-01795bfd0d46.png?1562830795", "art_crop": "https://c1.scryfall.com/file/scryfall-cards/art_crop/front/7/0/7050735c-b232-47a6-a342-01795bfd0d46.jpg?1562830795", "border_crop": "https://c1.scryfall.com/file/scryfall-cards/border_crop/front/7/0/7050735c-b232-47a6-a342-01795bfd0d46.jpg?1562830795"}, "mana_cost": "{U}", "cmc": 1.0, "type_line": "Enchantment \u2014 Aura", "oracle_text": "Enchant creature\nEnchanted creature gets -3/-0.", "colors": ["U"], "color_identity": ["U"], "keywords": ["Enchant"], "rulings_uri": "https://api.scryfall.com/cards/7050735c-b232-47a6-a342-01795bfd0d46/rulings"}, 
{"name": "Road of Return", "scryfall_uri": "https://scryfall.com/card/c19/34/road-of-return?utm_source=api", "image_uris": {"small": "https://c1.scryfall.com/file/scryfall-cards/small/front/e/7/e718b21b-46d1-4844-985c-52745657b1ac.jpg?1568003608", "normal": "https://c1.scryfall.com/file/scryfall-cards/normal/front/e/7/e718b21b-46d1-4844-985c-52745657b1ac.jpg?1568003608", "large": "https://c1.scryfall.com/file/scryfall-cards/large/front/e/7/e718b21b-46d1-4844-985c-52745657b1ac.jpg?1568003608", "png": "https://c1.scryfall.com/file/scryfall-cards/png/front/e/7/e718b21b-46d1-4844-985c-52745657b1ac.png?1568003608", "art_crop": "https://c1.scryfall.com/file/scryfall-cards/art_crop/front/e/7/e718b21b-46d1-4844-985c-52745657b1ac.jpg?1568003608", "border_crop": "https://c1.scryfall.com/file/scryfall-cards/border_crop/front/e/7/e718b21b-46d1-4844-985c-52745657b1ac.jpg?1568003608"}, "mana_cost": "{G}{G}", "cmc": 2.0, "type_line": "Sorcery", "oracle_text": "Choose one \u2014\n\u2022 Return target permanent card from your graveyard to your hand.\n\u2022 Put your commander into your hand from the command zone.\nEntwine {2} (Choose both if you pay the entwine cost.)", "colors": ["G"], "color_identity": ["G"], "keywords": ["Entwine"], "rulings_uri": "https://api.scryfall.com/cards/e718b21b-46d1-4844-985c-52745657b1ac/rulings", "preview": {"source": "Magicshibby", "source_uri": "https://www.youtube.com/watch?v=39MC2wBcf00&t=7m51s", "previewed_at": "2019-08-05"}}, 
{"name": "Storm Crow", "scryfall_uri": "https://scryfall.com/card/9ed/100/storm-crow?utm_source=api", "image_uris": {"small": "https://c1.scryfall.com/file/scryfall-cards/small/front/0/3/036ef8c9-72ac-46ce-af07-83b79d736538.jpg?1562730661", "normal": "https://c1.scryfall.com/file/scryfall-cards/normal/front/0/3/036ef8c9-72ac-46ce-af07-83b79d736538.jpg?1562730661", "large": "https://c1.scryfall.com/file/scryfall-cards/large/front/0/3/036ef8c9-72ac-46ce-af07-83b79d736538.jpg?1562730661", "png": "https://c1.scryfall.com/file/scryfall-cards/png/front/0/3/036ef8c9-72ac-46ce-af07-83b79d736538.png?1562730661", "art_crop": "https://c1.scryfall.com/file/scryfall-cards/art_crop/front/0/3/036ef8c9-72ac-46ce-af07-83b79d736538.jpg?1562730661", "border_crop": "https://c1.scryfall.com/file/scryfall-cards/border_crop/front/0/3/036ef8c9-72ac-46ce-af07-83b79d736538.jpg?1562730661"}, "mana_cost": "{1}{U}", "cmc": 2.0, "type_line": "Creature \u2014 Bird", "oracle_text": "Flying (This creature can't be blocked except by creatures with flying or reach.)", "power": "1", "toughness": "2", "colors": ["U"], "color_identity": ["U"], "keywords": ["Flying"], "rulings_uri": "https://api.scryfall.com/cards/036ef8c9-72ac-46ce-af07-83b79d736538/rulings"}, 
{"name": "Walking Sponge", "scryfall_uri": "https://scryfall.com/card/ulg/47/walking-sponge?utm_source=api", "image_uris": {"small": "https://c1.scryfall.com/file/scryfall-cards/small/front/b/1/b125d1e7-5d9b-4997-88b0-71bdfc19c6f2.jpg?1562863790", "normal": "https://c1.scryfall.com/file/scryfall-cards/normal/front/b/1/b125d1e7-5d9b-4997-88b0-71bdfc19c6f2.jpg?1562863790", "large": "https://c1.scryfall.com/file/scryfall-cards/large/front/b/1/b125d1e7-5d9b-4997-88b0-71bdfc19c6f2.jpg?1562863790", "png": "https://c1.scryfall.com/file/scryfall-cards/png/front/b/1/b125d1e7-5d9b-4997-88b0-71bdfc19c6f2.png?1562863790", "art_crop": "https://c1.scryfall.com/file/scryfall-cards/art_crop/front/b/1/b125d1e7-5d9b-4997-88b0-71bdfc19c6f2.jpg?1562863790", "border_crop": "https://c1.scryfall.com/file/scryfall-cards/border_crop/front/b/1/b125d1e7-5d9b-4997-88b0-71bdfc19c6f2.jpg?1562863790"}, "mana_cost": "{1}{U}", "cmc": 2.0, "type_line": "Creature \u2014 Sponge", "oracle_text": "{T}: Target creature loses your choice of flying, first strike, or trample until end of turn.", "power": "1", "toughness": "1", "colors": ["U"], "color_identity": ["U"], "keywords": [], "rulings_uri": "https://api.scryfall.com/cards/b125d1e7-5d9b-4997-88b0-71bdfc19c6f2/rulings"}, 
{"name": "Ravnica at War", "scryfall_uri": "https://scryfall.com/card/war/28/ravnica-at-war?utm_source=api", "image_uris": {"small": "https://c1.scryfall.com/file/scryfall-cards/small/front/e/0/e0f83824-43c6-4101-88fd-9109958b23e2.jpg?1557576051", "normal": "https://c1.scryfall.com/file/scryfall-cards/normal/front/e/0/e0f83824-43c6-4101-88fd-9109958b23e2.jpg?1557576051", "large": "https://c1.scryfall.com/file/scryfall-cards/large/front/e/0/e0f83824-43c6-4101-88fd-9109958b23e2.jpg?1557576051", "png": "https://c1.scryfall.com/file/scryfall-cards/png/front/e/0/e0f83824-43c6-4101-88fd-9109958b23e2.png?1557576051", "art_crop": "https://c1.scryfall.com/file/scryfall-cards/art_crop/front/e/0/e0f83824-43c6-4101-88fd-9109958b23e2.jpg?1557576051", "border_crop": "https://c1.scryfall.com/file/scryfall-cards/border_crop/front/e/0/e0f83824-43c6-4101-88fd-9109958b23e2.jpg?1557576051"}, "mana_cost": "{3}{W}", "cmc": 4.0, "type_line": "Sorcery", "oracle_text": "Exile all multicolored permanents.", "colors": ["W"], "color_identity": ["W"], "keywords": [], "rulings_uri": "https://api.scryfall.com/cards/e0f83824-43c6-4101-88fd-9109958b23e2/rulings", "preview": {"source": "Wizards of the Coast", "source_uri": "https://www.twitch.tv/videos/404095372", "previewed_at": "2019-03-31"}}, 
]

card_selecter = Entry(root)
card_selecter.grid(column=1,row=0)
card_selecter.bind('<KeyRelease>', on_key_release)

list_box = Listbox(root)
list_box.grid(column=2,row=0)
list_box.bind('<<ListBoxSelect>>', on_select)
list_box_update(cards)

show_pic_button = Button(root, text='Show Selected Card') 
show_pic_button.configure(command=lambda :show_picture(list_box.get(selection())))
show_pic_button.grid(column=3, row=0)

# show_picture('default')

mainloop()