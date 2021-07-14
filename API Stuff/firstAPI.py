import requests
import json

def print_json_object(obj):
    text = json.dumps(obj, sort_keys = True, indent = 4)
    print(text)

# let's inspect what the api has -------------------------

# response = requests.get("https://www.speedrun.com/api")

# print(response.status_code)

# print(type(response.json()))
# print(response.json())

# print_json_object(response.json())

# let's inspect the regions --------------------------------

# response2 = requests.get("https://www.speedrun.com/api/v1/regions")

# print(response2.status_code)
# print_json_object(response2.json())

# let's try finding an endpoint that wants parameters

# response3 = requests.get("https://www.speedrun.com/api/v1/games?max=1000")

# print_json_object(response3.json())

# for game in response3.json()["data"]:
#     if "Mario" in game["names"]["international"]:
#         print(game["names"]["international"])

# print(response3.json()["pagination"])


# so we are limited to 200 elements per page which means we need need to make multiple calls offsetting by 200 each time

# let's attempt 10000 calls---------------------------------------------------

# for i in range(50):
#     current_offset = str(i * 200)
#     current_response = requests.get("https://www.speedrun.com/api/v1/games?max=200&offset=" + current_offset)
#     for game in current_response.json()["data"]:
#         if "Mario" in game["names"]["international"]:
#             print(game["names"]["international"])

# seems that 10000 only gets us in the K's

# let's attempt the same thing but for Zelda to hopefully narrow results. this time attempt 100000 ---------------------------

# for i in range(500):
#     current_offset = str(i * 200)
#     current_response = requests.get("https://www.speedrun.com/api/v1/games?max=200&offset=" + current_offset)
#     for game in current_response.json()["data"]:
#         if "Zelda" in game["names"]["international"]:
#             print(game["names"]["international"])
#     if (i % 50 == 0):
#         print("----------", 100 * (i + 1) * 200 / 100000, "% complete", "----------")
#         print("----------", (i + 1) * 200, "games viewed", "----------")

# seems to be less than 40000 games -------------------------------------------------
# speedrun.com says 24,023 games

# total_game_count = 0
# for i in range(121):
#     current_offset = str(i * 200)
#     current_response = requests.get("https://www.speedrun.com/api/v1/games?max=200&offset=" + current_offset)
#     for game in current_response.json()["data"]:
#         if "Zelda" in game["names"]["international"]:
#             print(game["names"]["international"])
#     total_game_count += current_response.json()["pagination"]["size"]
#     if (i % 10 == 0 or i >= 110):
#         print("----------", round(100 * total_game_count / 24023,2), "% complete", "----------")
#         print("----------", total_game_count, "total games viewed", "----------")

# now how do I find a specific game? do I have to search? or can I make an api request?

response = requests.get("https://www.speedrun.com/api/v1/games/The_Legend_of_Zelda")

print(response.status_code)

print_json_object(response.json())

# that worked but i was very specific about the uri link --------------------------

# just 'zelda' and 'thelegendofzelda' failed
response = requests.get("https://www.speedrun.com/api/v1/games/thelegendofzelda")

print(response.status_code)

print_json_object(response.json())

# I believe it uses the "abbreviation" attribute found in the data