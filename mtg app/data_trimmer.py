import json
import fileinput

file_name = "oracle_cards.json"
with open(file_name, encoding='utf-8') as file:
    data = json.load(file)
    
    for i in data:
        try:
            i.pop("object")
        except KeyError:
            pass
        try:
            i.pop("id")
        except KeyError:
            pass
        try:
            i.pop("oracle_id")
        except KeyError:
            pass
        try:
            i.pop("multiverse_ids")
        except KeyError:
            pass
        try:
            i.pop("mtgo_id")
        except KeyError:
            pass
        try:
            i.pop("mtgo_foil_id")
        except KeyError:
            pass
        try:
            i.pop("arena_id")
        except KeyError:
            pass
        try:
            i.pop("tcgplayer_id")
        except KeyError:
            pass
        try:
            i.pop("cardmarket_id")
        except KeyError:
            pass
        try:
            i.pop("lang")
        except KeyError:
            pass
        try:
            i.pop("released_at")
        except KeyError:
            pass
        try:
            i.pop("uri")
        except KeyError:
            pass
        try:
            i.pop("layout")
        except KeyError:
            pass
        try:
            i.pop("highres_image")
        except KeyError:
            pass
        try:
            i.pop("image_status")
        except KeyError:
            pass
        try:
            i.pop("art_crop")
        except KeyError:
            pass
        try:
            i.pop("border_crop")
        except KeyError:
            pass
        try:
            i.pop("produced_mana")
        except KeyError:
            pass
        try:
            i.pop("all_parts")
        except KeyError:
            pass
        try:
            i.pop("legalities")
        except KeyError:
            pass
        try:
            i.pop("games")
        except KeyError:
            pass
        try:
            i.pop("reserved")
        except KeyError:
            pass
        try:
            i.pop("foil")
        except KeyError:
            pass
        try:
            i.pop("nonfoil")
        except KeyError:
            pass
        try:
            i.pop("oversized")
        except KeyError:
            pass
        try:
            i.pop("promo")
        except KeyError:
            pass
        try:
            i.pop("reprint")
        except KeyError:
            pass
        try:
            i.pop("variation")
        except KeyError:
            pass
        try:
            i.pop("set")
        except KeyError:
            pass
        try:
            i.pop("set_name")
        except KeyError:
            pass
        try:
            i.pop("set_type")
        except KeyError:
            pass
        try:
            i.pop("set_uri")
        except KeyError:
            pass
        try:
            i.pop("set_search_uri")
        except KeyError:
            pass
        try:
            i.pop("scryfall_set_uri")
        except KeyError:
            pass
        try:
            i.pop("prints_search_uri")
        except KeyError:
            pass
        try:
            i.pop("collector_number")
        except KeyError:
            pass
        try:
            i.pop("digital")
        except KeyError:
            pass
        try:
            i.pop("rarity")
        except KeyError:
            pass
        try:
            i.pop("flavor_text")
        except KeyError:
            pass
        try:
            i.pop("card_back_id")
        except KeyError:
            pass
        try:
            i.pop("artist")
        except KeyError:
            pass
        try:
            i.pop("artist_ids")
        except KeyError:
            pass
        try:
            i.pop("illustration_id")
        except KeyError:
            pass
        try:
            i.pop("border_color")
        except KeyError:
            pass
        try:
            i.pop("frame")
        except KeyError:
            pass
        try:
            i.pop("full_art")
        except KeyError:
            pass
        try:
            i.pop("textless")
        except KeyError:
            pass
        try:
            i.pop("booster")
        except KeyError:
            pass
        try:
            i.pop("story_spotlight")
        except KeyError:
            pass
        try:
            i.pop("edhrec_rank")
        except KeyError:
            pass
        try:
            i.pop("prices")
        except KeyError:
            pass
        try:
            i.pop("related_uris")
        except KeyError:
            pass

with open('trimmed_cards.txt', 'w') as json_file:
  json.dump(data, json_file)

with fileinput.FileInput('trimmed_cards.txt', inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace("{\"name\":", "\n{\"name\":"), end='')



# "name":"Ruthless Knave","scryfall_uri":"https://scryfall.com/card/xln/119/ruthless-knave?utm_source=api",
# "normal":"https://c1.scryfall.com/file/scryfall-cards/normal/front/1/c/1ce91e38-4601-4354-ad1b-2c5c1c70da17.jpg?1562551661",
# "large":"https://c1.scryfall.com/file/scryfall-cards/large/front/1/c/1ce91e38-4601-4354-ad1b-2c5c1c70da17.jpg?1562551661",
# "png":"https://c1.scryfall.com/file/scryfall-cards/png/front/1/c/1ce91e38-4601-4354-ad1b-2c5c1c70da17.png?1562551661",
# "mana_cost":"{2}{B}","cmc":3.0,"type_line":"Creature — Orc Pirate",
# "oracle_text":"{2}{B}, Sacrifice a creature: Create two Treasure tokens. (They're artifacts with \"{T}, Sacrifice this artifact: Add one mana of any color.\")\nSacrifice three Treasures: Draw a card.",
# "power":"3","toughness":"2","colors":["B"],"color_identity":["B"],"keywords":[],
# "rulings_uri":"https://api.scryfall.com/cards/1ce91e38-4601-4354-ad1b-2c5c1c70da17/rulings",

  