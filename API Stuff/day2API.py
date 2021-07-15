# more work with speedrun.com API

import requests
import json

def print_json_object(obj):
    text = json.dumps(obj, sort_keys = True, indent = 4)
    print(text)

# going to start by inspecting data to look at runs ------------------------

# response = requests.get("https://www.speedrun.com/api/v1/runs")

# print_json_object(response.json())
# print_json_object(response.json()["data"][0])

# now what about multiple runs from a specific game -----------------------------

# response = requests.get("https://www.speedrun.com/api/v1/games/sms")

# print_json_object(response.json())

# so there is a link for runs in the object returned
# also a link for the leaderboard "https://www.speedrun.com/api/v1/leaderboards/v1pxjz68/category/n2y3r8do"
# let's see what that looks like-----------------------------------------------------------------------------------------


# response = requests.get("https://www.speedrun.com/api/v1/leaderboards/v1pxjz68/category/n2y3r8do")

# for i in range(500):
#     print(response.text[i], end= "")

# print_json_object(response.json()["data"]["runs"][0])

# let's attempt to make a csv of the leaderboards from super mario sunshine in another script

# now what if I want to see the various categories of a game----------------------------------------

# response = requests.get("https://www.speedrun.com/api/v1/games/sms")

# print_json_object(response.json())

# there is a link for that in the links part of the data! what does that look like? ------------------------------

response = requests.get("https://www.speedrun.com/api/v1/games/v1pxjz68/categories")

print_json_object(response.json())
# so the data is a list of dictionaries with a dict for each category