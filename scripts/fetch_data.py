import requests
import json

# Bundesliga URLS
BetikaBLURL = "https://api.betika.com/v1/uo/matches?tab=upcoming&sub_type_id=1,186&sport_id=14&tag_id=&competition_id=214&sort_id=2&period_id=9&esports=false"
SportPesaBLURL = "https://www.ke.sportpesa.com/api/upcoming/games?type=prematch&sportId=1&section=top&leagueId=76390&markets_layout=multiple&o=startTime"
Bet22BLURL = "https://22bet.co.ke/LineFeed/Get1x2_VZip?sports=1&champs=96463&count=50&lng=en&tf=3000000&mode=4&partner=151&getEmpty=true"
MelBetBLUrl = "https://melbet.ke/LineFeed/Get1x2_VZip?sports=1&champs=96463&count=50&lng=en&tf=1000000&mode=4&partner=225&getEmpty=true&gr=277"
X1BetBLURL = "https://1xbet.co.ke/LineFeed/Get1x2_VZip?sports=1&champs=96463&count=50&lng=en&tf=2200000&mode=4&country=87&partner=61&getEmpty=true"

# Laliga URLS
SportPesaLLURL = "https://www.ke.sportpesa.com/api/upcoming/games?type=prematch&sportId=1&section=top&leagueId=76837&markets_layout=multiple&o=startTime"
BetikaLLURL = "https://api.betika.com/v1/uo/matches?tab=upcoming&sub_type_id=1,186&sport_id=14&tag_id=&competition_id=14482&sort_id=2&period_id=9&esports=false"
Bet22LLURL = "https://22bet.co.ke/LineFeed/Get1x2_VZip?sports=1&champs=127733&count=50&lng=en&tf=3000000&mode=4&partner=151&getEmpty=true"
MelBetLLUrl = "https://melbet.ke/LineFeed/Get1x2_VZip?sports=1&champs=127733&count=50&lng=en&tf=1000000&mode=4&partner=225&getEmpty=true&gr=277"
X1BetLLURL = "https://1xbet.co.ke/LineFeed/Get1x2_VZip?sports=1&champs=127733&count=50&lng=en&tf=2200000&mode=4&country=87&partner=61&getEmpty=true"

# Premier League URLS
BetikaPLURL = "https://api.betika.com/v1/uo/matches?&tab=upcoming&sub_type_id=1,186&sport_id=14&tag_id=&competition_id=222&sort_id=2&period_id=9&esports=fals"
SportPesaPLURL = "https://www.ke.sportpesa.com/api/upcoming/games?type=prematch&sportId=1&section=top&leagueId=67600&markets_layout=multiple&o=startTime&pag_count=15&pag_min=1"
Bet22PLURL = "https://22bet.co.ke/LineFeed/Get1x2_VZip?sports=1&champs=88637&count=50&lng=en&tf=3000000&mode=4&partner=151&getEmpty=true"
MelBetPLUrl = "https://melbet.ke/LineFeed/Get1x2_VZip?champs=88637&count=50&lng=en&tf=1000000&mode=4&partner=225&getEmpty=true&gr=277"
X1BetPLURL = "https://1xbet.co.ke/LineFeed/Get1x2_VZip?sports=1&champs=88637&count=50&lng=en&tf=2200000&mode=4&country=87&partner=61&getEmpty=true"

# Serie a URLS
SportPesaSAURL = "https://www.ke.sportpesa.com/api/upcoming/games?type=prematch&sportId=1&section=top&leagueId=67358&markets_layout=multiple&o=startTime"
BetikaSAURL = "https://api.betika.com/v1/uo/matches?tab=upcoming&sub_type_id=1,186&sport_id=14&tag_id=&competition_id=182&sort_id=2&period_id=9&esports=false"
Bet22SAURL = "https://22bet.co.ke/LineFeed/Get1x2_VZip?sports=1&champs=110163&count=50&lng=en&tf=3000000&mode=4&partner=151&getEmpty=true"
MelBetSAUrl = "https://melbet.ke/LineFeed/Get1x2_VZip?sports=1&champs=110163&count=50&lng=en&tf=1000000&mode=4&partner=225&getEmpty=true&gr=277"
X1BetSAURL = "https://1xbet.co.ke/LineFeed/Get1x2_VZip?sports=1&champs=110163&count=50&lng=en&tf=2200000&mode=4&country=87&partner=61&getEmpty=true"





def fetch_data(league, url, jsonFile, site):
    res = requests.get(url)
    print(f"Fetching {league} odds...")
    print(f"{site} Status: ", res.status_code)
    resJson = json.loads(res.text)
    resObj = json.dumps(resJson, indent=4, sort_keys=True)
    with open(jsonFile, "a") as o:
        o.write(resObj)

def process_data():
    # fetch premier league
    fetch_data("premier league", SportPesaPLURL, "./json/PLJson/sportPesa_premierleague.json", "sportpesa")
    fetch_data("premier league", BetikaPLURL, "./json/PLJson/betika_premierleague.json", "betika")
    fetch_data("premier league", Bet22PLURL, "./json/PLJson/bet22_premierleague.json", "22bet")
    fetch_data("premier league", MelBetPLUrl, "./json/PLJson/melbet_premierleague.json", "melbet")
    fetch_data("premier league", X1BetPLURL, "./json/PLJson/1xbet_premierleague.json", "1xbet")

    # fetch bundesliga data  
    fetch_data("bundesliga", SportPesaBLURL, "./json/BLJson/sportPesaBundesLiga.json", "sportpesa")
    fetch_data("bundesliga", BetikaBLURL, "./json/BLJson/betikaBundesLiga.json", "betika")
    fetch_data("bundesliga", Bet22BLURL, "./json/BLJson/22betBundesLiga.json", "22bet")
    fetch_data("bundesliga", MelBetBLUrl, "./json/BLJson/melbetBundesLiga.json", "melbet")
    fetch_data("bundesliga", X1BetBLURL, "./json/BLJson/1xbetBundesLiga.json", "1xbet")

    # fetch la liga data
    fetch_data("la liga", SportPesaLLURL, "./json/LLJson/sportPesaLaLiga.json", "sportpesa")
    fetch_data("la liga", BetikaLLURL, "./json/LLJson/betikaLaLiga.json", "betika")
    fetch_data("la liga", Bet22LLURL, "./json/LLJson/22betLaLiga.json", "22bet")
    fetch_data("la liga", MelBetLLUrl, "./json/LLJson/melbetLaLiga.json", "melbet")
    fetch_data("la liga", X1BetLLURL, "./json/LLJson/1xbetLaLiga.json", "1xbet")



    # fetch serie a league
    fetch_data("serie a", SportPesaSAURL, "./json/SAJson/sportPesaSA.json", "sportpesa")
    fetch_data("serie a", BetikaSAURL, "./json/SAJson/betikaSA.json", "betika")
    fetch_data("serie a", Bet22SAURL, "./json/SAJson/22betSA.json", "22bet")
    fetch_data("serie a", MelBetSAUrl, "./json/SAJson/melbetSA.json", "melbet")
    fetch_data("serie a", X1BetSAURL, "./json/SAJson/1xbetSA.json", "1xbet")


if __name__ == "__main__":
    process_data()