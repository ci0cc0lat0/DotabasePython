import requests
import json
import os
import urllib.parse as up
import psycopg2
accountDict = {
"ant":118728071,
"gub":112127522,
"json":122334023,
"andy":106975318,
"matt":110352369,
"rawb":171149001,
"josh":380821421
}

# postgres://database:password@host/user
# port = 5432
conn = psycopg2.connect(database="",user="",password="", host="",port="5432")
cur = conn.cursor()

# gets the last match of the 
def getMostRecentMatch(steam32):
    url = f"https://api.opendota.com/api/players/{steam32}/recentMatches"
    response = requests.get(url)
    data = response.json()
    match_id = data[0]['match_id']
    return match_id

def dataBaseCheck(steam32,match_id):
    cur.execute(f"SELECT steam32, match_id FROM match WHERE steam32 = {steam32} AND match_id ={match_id};")
    if cur.rowcount != 1:
        print(f'No match found for steam ID {steam32} and game {match_id}')
        setMatchData(steam32,match_id)
    else:
        print(f'A match for steam ID {steam32} and game {match_id} has been found')

def setMatchData(steam32,match_id):
    print(steam32,match_id)
    url = f'https://api.opendota.com/api/players/{steam32}/recentMatches'
    response = requests.get(url)
    data = response.json()
    try:
        cur.execute(f"INSERT INTO match VALUES ({steam32}, {data[0]['match_id']}, {data[0]['duration']}, {data[0]['kills']}, {data[0]['assists']}, {data[0]['deaths']}, {data[0]['gold_per_min']}, {data[0]['xp_per_min']})")
        conn.commit()
    except Exception as e:
        print(e)

def main():
    # ant, gub, json, andy, matt, rawb, josh
    friendList = [118728071,112127522,122334023,106975318,110352369,171149001,380821421]
    for x in friendList:
        anyID = x
        recentMatchId = getMostRecentMatch(anyID)
        dataBaseCheck(anyID,recentMatchId)
    cur.close()

if __name__ == '__main__':
    main()
