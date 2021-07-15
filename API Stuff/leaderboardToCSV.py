# this script takes a leaderboard from the api and creates a csv with its data
import requests
import csv

# note that this is a specific leaderboard link for super mario sunshine any%
# now it is shadow of the colossus (2018)
# now it is smb 1
response = requests.get("https://www.speedrun.com/api/v1/leaderboards/om1m3625/category/w20p0zkn")

numRuns = len(response.json()["data"]["runs"])

i = 0
with open('SMB1Leaderboard.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, 
                        delimiter=',',
                        quotechar='|', 
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["place","date", "verification_status",
                    "emulator", "platform", "region", "realtime"])
    while i < numRuns:
        # access the ith leaderboard entry  
        ithRun = response.json()["data"]["runs"][i]
        # write ith entry data to csv file
        writer.writerow([ithRun["place"],
                        ithRun["run"]["date"],
                        ithRun["run"]["status"]["status"],
                        ithRun["run"]["system"]["emulated"],
                        ithRun["run"]["system"]["platform"],
                        ithRun["run"]["system"]["region"],
                        ithRun["run"]["times"]["realtime_t"]
                        ])
        # print("wrote ", i+1, "th place to file")
        i += 1