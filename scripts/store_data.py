import time
import json
import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")

from premierleaguearb.models import SportpesaPremierLeague, X1betPremierLeague, MelBetPremierLeague, Bet22PremierLeague, BetikaPremierLeague


def formatString(str):
    joinedStr = str.replace(" ", "")
    # trimmedStr = joinedStr[0:7]
    return joinedStr.lower()


def formatDate(date):
    return date[5:16]

pl_teams = {  # premier league
    "arsenal": ["Arsenal"],
    "astonvilla": ["Aston Villa"],
    "brentford": ["Brentford"],
    "brighton": ["Brighton", "BRIGHTON", "Brighton & Hove Albion"],
    "burnely": ["Burnley", "BURNLEY"],
    "chelsea": ["Chelsea", "CHELSEA"],
    "crystalpalace": ["Crystal Palace"],
    "everton": ["Everton"],
    "leeds": ["Leeds", "Leeds United"],
    "leicester": ["Leicester", "Leicester City"],
    "liverpool": ["Liverpool", "LIVERPOOL"],
    "mancity": ["Manchester City", "MAN CITY"],
    "manunited": ["Manchester Utd", "MAN UTD", "Manchester United"],
    "newcastle": ["Newcastle", "NEWCASTLE", "Newcastle United"],
    "norwichcity": ["Norwich City", "Norwich"],
    "southampton": ["Southampton", "SOUTHAMPTON"],
    "tottenham": ["Tottenham", "TOTTENHAM", "Tottenham Hotspur"],
    "watford": ["Watford", "WATFORD"],
    "westham": ["West Ham", "WEST HAM", "West Ham United"],
    "wolves": ["Wolverhampton", "Wolves", "Wolverhampton Wanderers"],
}


bl_teams = {  # bundesliga teams
    "bayern": ["Bayern Munchen", "BAYERN", "Bayern Munich"],
    "dortmund": ["Borussia Dortmund", "DORTMUND"],
    "freiburg": ["SC Freiburg", "FREIBURG", "Freiburg"],
    "vflwolfsburg": ["VfL Wolfsburg", "WOLFSBURG"],
    "leipzig": ["RB Leipzig", "LEIPZIG", "RasenBallsport Leipzig"],
    "leverkusen": ["Bayer Leverkusen", "LEVERKUSEN", "Bayer 04 Leverkusen"],
    "mainz": ["Mainz", "MAINZ", "1. FSV Mainz 05"],
    "unionberlin": ["Union Berlin", "UNION BERLIN"],
    "borussiagladbach": ["Borussia Monchengladbach", "BORUSSIA (MG)"],
    "hoffenheim": ["Hoffenheim", "HOFFENHEIM", "TSG 1899 Hoffenheim"],
    "koln": ["FC Koln", "KOLN", "1. Koln"],
    "bochum": ["VfL Bochum", "Bochum"],
    "herthaberlin": ["Hertha BSC", "HERTHA"],
    "eintrachfrankfurt": ["Eintracht Frankfurt", "EINTRACHT"],
    "stuttgart": ["Stuttgart", "STUTTGART", "VfB Stuttgart"],
    "augsburg": ["Augsburg", "AUGSBURG"],
    "arminiabielefeld": ["Arminia Bielefeld", "BIELEFELD"],
    "greutherfurth": ["Greuther Furth"],
}


def returnKey(str, teams):
    key = [key for key, val in teams.items() if str in val]
    if key:
        return key[0]
    return 0



# start django


#


def save_premierleague_arb():
    X1betPremierLeague.objects.all().delete()
    Bet22PremierLeague.objects.all().delete()
    BetikaPremierLeague.objects.all().delete()
    MelBetPremierLeague.objects.all().delete()
    SportpesaPremierLeague.objects.all().delete()
    # get data from json files

    # 1x bet premier league data
    f_1 = open("json/PLJson/1xbet_premierleague.json")
    data = json.load(f_1)    
    for i in data["Value"]:
        stat = X1betPremierLeague(
            team_a = returnKey(i["O1"], pl_teams),
            team_b = returnKey(i["O2"], pl_teams),
            odd_a = i["E"][0]["C"],
            odd_b = i["E"][1]["C"],
            odd_c = i["E"][2]["C"],
        )
        stat.save()
    f_1.close()
    print("saved 1xbet premier league!!")

    # # bet22 premier league data
    # f_2 = open("./json/PLJson/bet22_premierleague.json")
    # data = json.load(f_2)
    # for i in data["data"]:
    #     site_2 = Bet22PremierLeague(
    #         returnKey(i["home_team"]),
    #         returnKey(i["away_team"]),
    #         i["home_odd"],
    #         i["neutral_odd"],
    #         i["away_odd"],
    #     )
    # site_2.save()
    # f_2.close()
    # print("saved 22 bet premier league!!")

    # # betika premier league data
    # f_3 = open("./json/PLJson/betika_premierleague.json")
    # data = json.load(f_3)
    # for i in data["data"]:
    #     site_3 = BetikaPremierLeague(
    #         returnKey(i["home_team"]),
    #         returnKey(i["away_team"]),
    #         i["home_odd"],
    #         i["neutral_odd"],
    #         i["away_odd"],
    #     )
    # site_3.save()
    # f_3.close()
    # print("saved betika premier league!!")

    # # melbet premier league data
    # f_4 = open("./json/PLJson/melbet_premierleague.json")
    # data = json.load(f_4)
    # for i in data["data"]:
    #     site_4 = MelBetPremierLeague(
    #         returnKey(i["home_team"]),
    #         returnKey(i["away_team"]),
    #         i["home_odd"],
    #         i["neutral_odd"],
    #         i["away_odd"],
    #     )
    # site_4.save()
    # f_4.close()
    # print("saved betika premier league!!")

    # # sport pesa premier league data
    # f_5 = open("./json/PLJson/sportPesa_premierleague.json")
    # data = json.load(f_5)
    # for i in data:
    #     site_5 = SportpesaPremierLeague(
    #     team_a = returnKey(i["competitors"][0]["name"]),
    #     teab_b = returnKey(i["competitors"][1]["name"]),
    #     odd_a = i["markets"][0]["selections"][0]["odds"],
    #     odd_b = i["markets"][0]["selections"][1]["odds"],
    #     odd_c = i["markets"][0]["selections"][2]["odds"],
    #     time = formatDate(i["date"])
    # )
    # site_5.save()
    # f_5.close()
    # print("saved sportpesa premier league!!")


def run():
    save_premierleague_arb()

if __name__ == "__main__":
    run()

# save records to database
# def saveSportPesaBL():
#     db = "../database/bundesliga.db"
#     conn = database.createConnection(db)
#     f = open("../json/BLJson/sportPesaBundesLiga.json")
#     data = json.load(f)
#     with conn:
#         for i in data:
#             record = (
#                 returnKey(i["competitors"][0]["name"]),
#                 returnKey(i["competitors"][1]["name"]),
#                 i["markets"][0]["selections"][0]["odds"],
#                 i["markets"][0]["selections"][1]["odds"],
#                 i["markets"][0]["selections"][2]["odds"],
#                 formatDate(i["date"]),
#             )
#             createSPBLRecord(conn, record)
#     f.close()
#     print("saved sportpesa bundesliga!!")

    # for i in range(len(uefa_fixtures)):
    #     print(f"## saving uefa champions league ##")

    #     league = UefaChampsResult(
    #         team_a = uefa_fixtures[i]["Team_A"],
    #         team_b = uefa_fixtures[i]["Team_B"],
    #         score_a = uefa_fixtures[i]["Score_A"],
    #         score_b = uefa_fixtures[i]["Score_B"],
    #         league = uefa_fixtures[i]["League"],
    #     )
    #     league.save()


#


# end django

# create records
# def createSPBLRecord(conn, record):
#     sportpesasql = """INSERT OR IGNORE INTO sportpesaBundesliga(home_team, away_team, home_odd, neutral_odd, away_odd, start_time) VALUES(?, ?, ?, ?, ?, ?)"""
#     cur = conn.cursor()
#     cur.execute(sportpesasql, record)
#     conn.commit()
#     return cur.lastrowid


# def createBBLRecord(conn, record):
#     betikasql = """INSERT OR IGNORE INTO betikaBundesliga(home_team, away_team, home_odd, neutral_odd, away_odd) VALUES(?, ?, ?, ?, ?)"""
#     cur = conn.cursor()
#     cur.execute(betikasql, record)
#     conn.commit()
#     return cur.lastrowid


# def createB22BLRecord(conn, record):
#     bet22sql = """INSERT OR IGNORE INTO bet22Bundesliga(home_team, away_team, home_odd, neutral_odd, away_odd) VALUES(?, ?, ?, ?, ?)"""
#     cur = conn.cursor()
#     cur.execute(bet22sql, record)
#     conn.commit()
#     return cur.lastrowid


# def createMLBLRecord(conn, record):
#     mlsql = """INSERT OR IGNORE INTO melBundesliga(home_team, away_team, home_odd, neutral_odd, away_odd) VALUES(?, ?, ?, ?, ?)"""
#     cur = conn.cursor()
#     cur.execute(mlsql, record)
#     conn.commit()
#     return cur.lastrowid


# def create1XBBLRecord(conn, record):
#     x1sql = """INSERT OR IGNORE INTO x1betBundesliga(home_team, away_team, home_odd, neutral_odd, away_odd) VALUES(?, ?, ?, ?, ?)"""
#     cur = conn.cursor()
#     cur.execute(x1sql, record)
#     conn.commit()
#     return cur.lastrowid


# # save records to database
# def saveSportPesaBL():
#     db = "../database/bundesliga.db"
#     conn = database.createConnection(db)
#     f = open("../json/BLJson/sportPesaBundesLiga.json")
#     data = json.load(f)
#     with conn:
#         for i in data:
#             record = (
#                 returnKey(i["competitors"][0]["name"]),
#                 returnKey(i["competitors"][1]["name"]),
#                 i["markets"][0]["selections"][0]["odds"],
#                 i["markets"][0]["selections"][1]["odds"],
#                 i["markets"][0]["selections"][2]["odds"],
#                 formatDate(i["date"]),
#             )
#             createSPBLRecord(conn, record)
#     f.close()
#     print("saved sportpesa bundesliga!!")


# def saveBetikaBL():
#     db = "../database/bundesliga.db"
#     conn = database.createConnection(db)
#     f = open("../json/BLJson/betikaBundesLiga.json")
#     data = json.load(f)
#     with conn:
#         for i in data["data"]:
#             record = (
#                 returnKey(i["home_team"]),
#                 returnKey(i["away_team"]),
#                 i["home_odd"],
#                 i["neutral_odd"],
#                 i["away_odd"],
#             )
#             createBBLRecord(conn, record)
#     f.close()
#     print("saved betika bundesliga!!")


# def saveBet22BL():
#     db = "../database/bundesliga.db"
#     conn = database.createConnection(db)
#     f = open("../json/BLJson/22betBundesLiga.json")
#     data = json.load(f)
#     with conn:
#         for i in data["Value"]:
#             record = (
#                 returnKey(i["O1"]),
#                 returnKey(i["O2"]),
#                 i["E"][0]["C"],
#                 i["E"][1]["C"],
#                 i["E"][2]["C"],
#             )
#             createB22BLRecord(conn, record)
#     f.close()
#     print("saved 22 bet bundesliga!!")


# def saveMelBL():
#     db = "../database/bundesliga.db"
#     conn = database.createConnection(db)
#     f = open("../json/BLJson/melbetBundesLiga.json")
#     data = json.load(f)
#     with conn:
#         for i in data["Value"]:
#             record = (
#                 returnKey(i["O1"]),
#                 returnKey(i["O2"]),
#                 i["E"][0]["C"],
#                 i["E"][1]["C"],
#                 i["E"][2]["C"],
#             )
#             createMLBLRecord(conn, record)
#     f.close()
#     print("saved melbet bundesliga!!")


# def save1XBL():
#     db = "../database/bundesliga.db"
#     conn = database.createConnection(db)
#     f = open("../json/BLJson/1xbetBundesLiga.json")
#     data = json.load(f)
#     with conn:
#         for i in data["Value"]:
#             record = (
#                 returnKey(i["O1"]),
#                 returnKey(i["O2"]),
#                 i["E"][0]["C"],
#                 i["E"][1]["C"],
#                 i["E"][2]["C"],
#             )
#             create1XBBLRecord(conn, record)
#     f.close()
#     print("saved 1xbet bundesliga!!")


# def combineRecords():  # combine table columns
#     db = "../database/bundesliga.db"
#     conn = database.createConnection(db)
#     combineBundesligaSql = f"""INSERT INTO bLCombinations (home_team, away_team, sph, spx, spa, btkh, btkx, btka, bt22h, bt22x, bt22a, mlh, mlx, mla, x1h, x1x, x1a, time) 
# SELECT sp.home_team, sp.away_team, sp.home_odd, sp.neutral_odd, sp.away_odd, btk.home_odd, btk.neutral_odd, btk.away_odd, btt.home_odd, btt.neutral_odd, btt.away_odd, ml.home_odd, ml.neutral_odd, ml.away_odd, x1.home_odd, x1.neutral_odd, x1.away_odd, sp.start_time 
# FROM sportpesaBundesliga sp, betikaBundesliga as btk, bet22Bundesliga as btt, melBundesliga as ml, x1betBundesliga as x1
# WHERE sp.home_team=btk.home_team
# AND sp.home_team=btt.home_team
# AND sp.home_team=ml.home_team
# AND sp.home_team=x1.home_team"""
#     cur = conn.cursor()
#     cur.execute(combineBundesligaSql)
#     conn.commit()
#     print("Records combined!")
#     return cur.lastrowid


# if __name__ == "__main__":  # entry
#     saveSportPesaBL()
#     saveBetikaBL()
#     saveBet22BL()
#     saveMelBL()
#     save1XBL()
#     time.sleep(3)
#     combineRecords()
