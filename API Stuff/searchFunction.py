# based on the assumption in firstAPI.py line 96, I'm going to build a binary searching function for games
# currently finds exact matches for game titles while disregarding capitalization and punctuation
# kinda slow but that could be from api request limits or inefficiency of algorithm
import requests

def searchAPI(search_term):
    search_term = search_term.lower()
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for x in search_term:
        if x in punc:
            search_term = search_term.replace(x, "")
    # print(search_term)
    left_index = 0
    right_index = 24023
    while True:
        if left_index >= right_index:
            return "Search complete. No results."
        mid = (right_index + left_index) // 2
        current_response = requests.get("https://www.speedrun.com/api/v1/games?offset=" + str(mid))
        if current_response.status_code == 200:
            mid_name = current_response.json()["data"][0]["names"]["international"]
            mid_name = mid_name.lower()
            for x in mid_name:
                if x in punc:
                    mid_name = mid_name.replace(x, "")
            # print("just found: ", mid_name)
            if mid_name == search_term:
                return "uri abbreviation: " + current_response.json()["data"][0]["abbreviation"]
            elif mid_name < search_term:
                left_index = mid
            else: 
                right_index = mid
        else:
            return "Search inconclusive. Status code: " + str(current_response.status_code)


print(searchAPI("the legend of zelda: twilight princess hd"))