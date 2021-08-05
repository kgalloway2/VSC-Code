import random
import math


default_deck = ['wasabi'] * 6 +  ['egg'] * 5 +  ['salmon'] * 10 +  ['squid'] * 5 +  ['sashimi'] * 14 +  ['tempura'] * 14 +  [
                'dumpling'] * 14 + ['maki1'] * 6 + ['maki2'] * 12 + ['maki3'] * 8 + ['pudding'] * 10 +  ['chopstick'] * 4

dumpling_map = {0:0,1:1,2:3,3:6,4:10,5:15,6:15,7:15,8:15,9:15,10:15}

def score_maki(selected_cards):
    num_maki = []
    result1 = []
    result2 = []
    for i in selected_cards:
        num_maki.append(i.count("maki1") + i.count("maki2") * 2 + i.count("maki3") * 3)
    
    # find persons(s) with max maki
    max_maki = max(num_maki)
    if num_maki.count(max_maki) > 1:
        people_with_max = []
        num_people_with_max = 0
        for j in num_maki:
            people_with_max.append(False)
            if j == max_maki:
                people_with_max[-1] = True
                num_people_with_max += 1
        num_points_for_max = 6  // num_people_with_max

        for i in range(len(people_with_max)):
            if people_with_max[i]:
                result1.append({i: num_points_for_max})

    elif num_maki.count(max_maki) == 1:
        person_with_max = num_maki.index(max_maki)
        num_points_for_max = 6
        result1.append({person_with_max: num_points_for_max})

    # find person(s) with second most maki
    if len(result1) == 1:
        # calculate result2
        second_max = 0
        for i in num_maki:
            if i > second_max and i < max_maki:
                second_max = i
        if num_maki.count(second_max) > 1:
        
            people_with_second_max = []
            num_people_with_second_max = 0
            for j in num_maki:
                people_with_second_max.append(False)
                if j == second_max:
                    people_with_second_max[-1] = True
                    num_people_with_second_max += 1
            num_points_for_second_max = 6  // num_people_with_second_max

            for i in range(len(people_with_second_max)):
                if people_with_second_max[i]:
                    result2.append({i: num_points_for_second_max})

        elif num_maki.count(second_max) == 1:
            person_with_second_max = num_maki.index(second_max)
            num_points_for_second_max = 6
            result2.append({person_with_second_max: num_points_for_second_max})

    return result1, result2

def score_pudding(selected_cards):
    num_pudding = []
    result1 = []
    result2 = []
    for i in selected_cards:
        num_pudding.append(i.count("pudding"))
    
    # find person(s) with max pudding
    max_pudding = max(num_pudding)
    if num_pudding.count(max_pudding) > 1:
        people_with_max = []
        num_people_with_max = 0
        for j in num_pudding:
            people_with_max.append(False)
            if j == max_pudding:
                people_with_max[-1] = True
                num_people_with_max += 1
        num_points_for_max = 6  // num_people_with_max

        for i in range(len(people_with_max)):
            if people_with_max[i]:
                result1.append({i: num_points_for_max})

    elif num_pudding.count(max_pudding) == 1:
        person_with_max = num_pudding.index(max_pudding)
        num_points_for_max = 6
        result1.append({person_with_max: num_points_for_max})

    # find person(s) with least pudding
    
    min_pudding = min(num_pudding)
    if num_pudding.count(min_pudding) > 1:
    
        people_with_min_pudding = []
        num_people_with_min_pudding = 0
        for j in num_pudding:
            people_with_min_pudding.append(False)
            if j == min_pudding:
                people_with_min_pudding[-1] = True
                num_people_with_min_pudding += 1
        num_points_for_min_pudding = math.ceil(-6 / num_people_with_min_pudding)

        for i in range(len(people_with_min_pudding)):
            if people_with_min_pudding[i]:
                result2.append({i: num_points_for_min_pudding})

    elif num_pudding.count(min_pudding) == 1:
        person_with_min_pudding = num_pudding.index(min_pudding)
        num_points_for_min_pudding = -6
        result2.append({person_with_min_pudding: num_points_for_min_pudding})

    return result1, result2

def score_tempura(selected_cards):
    tempura_points = []
    for i in selected_cards:
        tempura_points.append((i.count("tempura") // 2) * 5)
    
    return tempura_points

def score_sashimi(selected_cards):
    sashimi_points = []
    for i in selected_cards:
        sashimi_points.append((i.count("sashimi") // 3) * 10)
    
    return sashimi_points

def score_dumplings(selected_cards):
    dumpling_points = []
    for i in selected_cards:
        num_dumpling = i.count("dumpling")
        dumpling_points.append(dumpling_map[num_dumpling])
    
    return dumpling_points

def score_wasabi(selected_cards):
    wasabi_points = []
    for i in selected_cards:
        wasabi_indices = []
        for x in range(len(i)):
            if i[x] == "wasabi":
                wasabi_indices.append(x)

        current_points = 0
        for x in range(len(i)):
            if i[x] == "squid":
                current_points += 3
                for y in wasabi_indices:
                    if x > y:
                        current_points += 6
                        wasabi_indices.remove(y)
                        break
                
            elif i[x] == "salmon":
                current_points += 2
                for y in wasabi_indices:
                    if x > y:
                        current_points += 4
                        wasabi_indices.remove(y)
                        break

            elif i[x] == "egg":
                current_points += 1
                for y in wasabi_indices:
                    if x > y:
                        current_points += 2
                        wasabi_indices.remove(y)
                        break
        wasabi_points.append(current_points)

    return wasabi_points
        

def run_game(num_players):
    this_game_deck = default_deck.copy()
    random.shuffle(this_game_deck)
    round_num = 0
    round_scores = []
    pudding_tracker = [0] * num_players
    totals = [0] * num_players
    
    while round_num < 3:
        player_list = []
        selected_cards = []
        # deal hands
        for i in range(num_players):
            # print(this_game_deck)
            player_list.append(this_game_deck[:10 - (num_players - 2)])
            # print(player_list)
            this_game_deck = this_game_deck[10 - (num_players - 2):]
            # print(this_game_deck)
            selected_cards.append([])
        
        # play a round

        while player_list[1]:
            # each player selects a card
            for i in range(num_players):
                first_card_index = random.randint(0, len(player_list[i]) - 1)
                selected_cards[i].append(player_list[i][first_card_index])
                player_list[i].pop(first_card_index)

                if "chopstick" in selected_cards[i]:
                    use_chopstick = random.random()
                    if use_chopstick > 0.5:
                        # use the chopstick
                        selected_cards[i].remove("chopstick")
                        player_list[i].append("chopstick")
                        second_card_index = random.randint(0, len(player_list[i]) - 1)
                        selected_cards[i].append(player_list[i][second_card_index])
                        player_list[i].pop(second_card_index)

        # score this round
        
        round_scores.append([]) 
        for i in range(num_players): 
            round_scores[round_num].append(0)

        # 2 member list of lists of dictionaires mapping player number to number of points
        maki_points = score_maki(selected_cards)

        for x in maki_points[0]:
            for key in x.keys():
                round_scores[round_num][key] += x[key]
        
        for x in maki_points[1]:
            for key in x.keys():
                round_scores[round_num][key] += x[key]

        tempura_points = score_tempura(selected_cards)
        for x in range(len(tempura_points)):
            round_scores[round_num][x] += tempura_points[x]

        sashimi_points = score_sashimi(selected_cards)
        for x in range(len(sashimi_points)):
            round_scores[round_num][x] += sashimi_points[x]

        dumpling_points = score_dumplings(selected_cards)
        for x in range(len(dumpling_points)):
            round_scores[round_num][x] += dumpling_points[x]

        wasabi_points = score_wasabi(selected_cards)
        for x in range(len(wasabi_points)):
            round_scores[round_num][x] += wasabi_points[x]

        for i in range(len(selected_cards)):
            pudding_tracker[i] += selected_cards[i].count("pudding")

        print(round_scores[round_num])
        round_num += 1
        
    pudding_points = score_pudding(selected_cards)

    for x in pudding_points[0]:
        for key in x.keys():
            round_scores[-1][key] += x[key]
    
    if num_players > 2:
        for x in pudding_points[1]:
            for key in x.keys():
                round_scores[-1][key] += x[key]

    for j in range(3):
        for i in range(num_players):
            totals[i] += round_scores[j][i]


    print(totals)
    

run_game(4)