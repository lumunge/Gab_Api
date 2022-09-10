import os
import requests
from bs4 import BeautifulSoup


from api.models import UefaChampsResult, PremierLeagueResult, PrimeraDivisionResult, SerieAResult, BundesligaResult, Ligue1Result, UefaSuperResult, UefaEuropaResult, UefaConfResult, LeagueCupResult


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")


league_mappings = {
    "4oogyu6o156iphvdvphwpck10": "uefa champoins league",
    "2kwbbcootiqqgmrzs6o5inle5": "premier league",
    "34pl8szyvrbwcmfkuocjm3r6t": "primera división",
    "1r097lpxe0xn03ihb7wi98kao": "serie a",
    "6by3h89i2eykc341oz7lv1ddd": "bundesliga",
    "dm5ka0os1e3dxcp3vh05kmp33": "ligue 1",
    "a0f4gtru0oyxmpvty4thc5qkc": "uefa super cup",
    "4c1nfi2j1m731hcay25fcgndq": "uefa europa league",
    "c7b8o53flg36wbuevfzy3lb10": "uefa europa conference league",
    "725gd73msyt08xm76v7gkxj7u": "league cup",
}

uefa_url = "https://www.goal.com/en/uefa-champions-league/fixtures-results/4oogyu6o156iphvdvphwpck10"
premier_league_url = (
    "https://www.goal.com/en/premier-league/fixtures-results/2kwbbcootiqqgmrzs6o5inle5"
)
primera_division_url = "https://www.goal.com/en/primera-divisi%C3%B3n/fixtures-results/34pl8szyvrbwcmfkuocjm3r6t"
serie_a_url = (
    "https://www.goal.com/en/serie-a/fixtures-results/1r097lpxe0xn03ihb7wi98kao"
)
bundesliga_url = (
    "https://www.goal.com/en/bundesliga/fixtures-results/6by3h89i2eykc341oz7lv1ddd"
)
ligue_1_url = (
    "https://www.goal.com/en/ligue-1/fixtures-results/dm5ka0os1e3dxcp3vh05kmp33"
)
uefa_super_cup_url = (
    "https://www.goal.com/en/uefa-super-cup/fixtures-results/a0f4gtru0oyxmpvty4thc5qkc"
)
uefa_europa_league_url = "https://www.goal.com/en/uefa-europa-league/fixtures-results/4c1nfi2j1m731hcay25fcgndq"
uefa_europa_conference_league_url = "https://www.goal.com/en/uefa-europa-conference-league/fixtures-results/c7b8o53flg36wbuevfzy3lb10"
league_cup_url = (
    "https://www.goal.com/en/league-cup/fixtures-results/725gd73msyt08xm76v7gkxj7u"
)


# 4oogyu6o156iphvdvphwpck10,
# a0f4gtru0oyxmpvty4thc5qkc,
# 4c1nfi2j1m731hcay25fcgndq,
# c7b8o53flg36wbuevfzy3lb10,
# 725gd73msyt08xm76v7gkxj7u,
# 2hj3286pqov1g1g59k2t2qcgm,
# apdwh753fupxheygs8seahh7x,
# 6694fff47wqxl10lrd9tb91f8,
# 486rhdgz7yc0sygziht7hje65,
# 70excpe1synn9kadnbppahdn7,
# 595nsvo7ykvoe690b1e4u5n56,
# 55hcphd1ccc6eai1ms77460on,
# 6vq8j5p3av14nr3iuyi4okhjt,
# 8x62utr2uti3i7kk14isbnip6,
# 43029a6fvhou87zehkd5u8fyt


def combine_objects(lst):
    new_lst = []
    for i in range(len(lst)):
        new_lst.append(lst[i].text)
    return new_lst


def fetch_data(league, tables):
    objects = []
    objects_1 = []

    for i in range(1, len(tables)):
        teams = tables[i].find_all("span", class_="match-row__team-name")
        goals = tables[i].find_all("b", class_="match-row__goals")
        objects.append(combine_objects(teams + goals))

    for i in range(len(objects)):
        objects_1.append(
            {
                "Team_A": objects[i][0],
                "Team_B": objects[i][1],
                "Score_A": objects[i][2],
                "Score_B": objects[i][3],
                "League": league_mappings.get(league),
            }
        )

    return objects_1

def get_fixtures(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    # uefa_title = uefa_soup.title
    league_id = url.split("/")[-1]
    # print(uefa_title)
    tables = soup.select("table")
    objects = fetch_data(league_id, tables)
    return objects

def save_db():
    UefaChampsResult.objects.all().delete()
    PremierLeagueResult.objects.all().delete()
    PrimeraDivisionResult.objects.all().delete()
    SerieAResult.objects.all().delete()
    BundesligaResult.objects.all().delete()
    Ligue1Result.objects.all().delete()
    UefaSuperResult.objects.all().delete()
    UefaEuropaResult.objects.all().delete()
    UefaConfResult.objects.all().delete()
    LeagueCupResult.objects.all().delete()

    uefa_fixtures = get_fixtures(uefa_url)
    premier_league_fixtures = get_fixtures(premier_league_url)
    primera_division_fixtures = get_fixtures(primera_division_url)
    serie_a_fixtures = get_fixtures(serie_a_url)
    bundesliga_fixtures = get_fixtures(bundesliga_url)
    ligue_1_fixtures = get_fixtures(ligue_1_url)
    uefa_super_cup_fixtures = get_fixtures(uefa_super_cup_url)
    uefa_europa_league_fixtures = get_fixtures(uefa_europa_league_url)
    uefa_europa_conference_fixtures = get_fixtures(uefa_europa_conference_league_url)
    league_cup_fixtures = get_fixtures(league_cup_url)


    for i in range(len(uefa_fixtures)):
        print(f"## saving uefa champions league ##")

        league = UefaChampsResult(
            team_a = uefa_fixtures[i]["Team_A"],
            team_b = uefa_fixtures[i]["Team_B"],
            score_a = uefa_fixtures[i]["Score_A"],
            score_b = uefa_fixtures[i]["Score_B"],
            league = uefa_fixtures[i]["League"],
        )
        league.save()

    for i in range(len(premier_league_fixtures)):
        # print(row)

        # print("###RESULT: ", premier_league_results[i][0])
        # print("###RESULT: ", premier_league_results[i][1])
        # print("###RESULT: ", premier_league_results[i][2])
        # print("###RESULT: ", premier_league_results[i][3])

        print(f"## saving premier league ##")

        league = PremierLeagueResult(
            team_a = premier_league_fixtures[i]["Team_A"],
            team_b = premier_league_fixtures[i]["Team_B"],
            score_a = premier_league_fixtures[i]["Score_A"],
            score_b = premier_league_fixtures[i]["Score_B"],
            league = premier_league_fixtures[i]["League"],
        )
        # print(result)

        league.save()

    for i in range(len(primera_division_fixtures)):
        print(f"## saving primera champions league ##")

        league = PrimeraDivisionResult(
            team_a = primera_division_fixtures[i]["Team_A"],
            team_b = primera_division_fixtures[i]["Team_B"],
            score_a = primera_division_fixtures[i]["Score_A"],
            score_b = primera_division_fixtures[i]["Score_B"],
            league = primera_division_fixtures[i]["League"],
        )
        league.save()
    
    for i in range(len(serie_a_fixtures)):
        print(f"## saving serie a league ##")

        league = SerieAResult(
            team_a = serie_a_fixtures[i]["Team_A"],
            team_b = serie_a_fixtures[i]["Team_B"],
            score_a = serie_a_fixtures[i]["Score_A"],
            score_b = serie_a_fixtures[i]["Score_B"],
            league = serie_a_fixtures[i]["League"],
        )
        league.save()
    
    for i in range(len(bundesliga_fixtures)):
        print(f"## saving primera champions league ##")

        league = BundesligaResult(
            team_a = bundesliga_fixtures[i]["Team_A"],
            team_b = bundesliga_fixtures[i]["Team_B"],
            score_a = bundesliga_fixtures[i]["Score_A"],
            score_b = bundesliga_fixtures[i]["Score_B"],
            league = bundesliga_fixtures[i]["League"],
        )
        league.save()
    
    for i in range(len(ligue_1_fixtures)):
        print(f"## saving ligue 1 league ##")

        league = Ligue1Result(
            team_a = ligue_1_fixtures[i]["Team_A"],
            team_b = ligue_1_fixtures[i]["Team_B"],
            score_a = ligue_1_fixtures[i]["Score_A"],
            score_b = ligue_1_fixtures[i]["Score_B"],
            league = ligue_1_fixtures[i]["League"],
        )
        league.save()
    
    for i in range(len(uefa_super_cup_fixtures)):
        print(f"## saving uefa super cup league ##")

        league = UefaSuperResult(
            team_a = uefa_super_cup_fixtures[i]["Team_A"],
            team_b = uefa_super_cup_fixtures[i]["Team_B"],
            score_a = uefa_super_cup_fixtures[i]["Score_A"],
            score_b = uefa_super_cup_fixtures[i]["Score_B"],
            league = uefa_super_cup_fixtures[i]["League"],
        )
        league.save()
    
    for i in range(len(uefa_europa_league_fixtures)):
        print(f"## saving uefa europa league ##")

        league = UefaEuropaResult(
            team_a = uefa_europa_league_fixtures[i]["Team_A"],
            team_b = uefa_europa_league_fixtures[i]["Team_B"],
            score_a = uefa_europa_league_fixtures[i]["Score_A"],
            score_b = uefa_europa_league_fixtures[i]["Score_B"],
            league = uefa_europa_league_fixtures[i]["League"],
        )
        league.save()
    
    for i in range(len(uefa_europa_conference_fixtures)):
        print(f"## saving uefa europa conference league ##")

        league = UefaConfResult(
            team_a = uefa_europa_conference_fixtures[i]["Team_A"],
            team_b = uefa_europa_conference_fixtures[i]["Team_B"],
            score_a = uefa_europa_conference_fixtures[i]["Score_A"],
            score_b = uefa_europa_conference_fixtures[i]["Score_B"],
            league = uefa_europa_conference_fixtures[i]["League"],
        )
        league.save()
    
    for i in range(len(league_cup_fixtures)):
        print(f"## saving league cup league ##")

        league = LeagueCupResult(
            team_a = league_cup_fixtures[i]["Team_A"],
            team_b = league_cup_fixtures[i]["Team_B"],
            score_a = league_cup_fixtures[i]["Score_A"],
            score_b = league_cup_fixtures[i]["Score_B"],
            league = league_cup_fixtures[i]["League"],
        )
        league.save()

    
def run():
    uefa_fixtures = get_fixtures(uefa_url)
    premier_league_fixtures = get_fixtures(premier_league_url)
    primera_division_fixtures = get_fixtures(primera_division_url)
    serie_a_fixtures = get_fixtures(serie_a_url)
    bundesliga_fixtures = get_fixtures(bundesliga_url)
    ligue_1_fixtures = get_fixtures(ligue_1_url)
    uefa_super_cup_fixtures = get_fixtures(uefa_super_cup_url)
    uefa_europa_league_fixtures = get_fixtures(uefa_europa_league_url)
    uefa_europa_conference_fixtures = get_fixtures(uefa_europa_conference_league_url)
    league_cup_fixtures = get_fixtures(league_cup_url)

    print("### UEFA ###")
    print(uefa_fixtures)

    print("### Premier League ###")
    print(premier_league_fixtures)

    print("### Primera Division ###")
    print(primera_division_fixtures)

    print("### Series A ###")
    print(serie_a_fixtures)

    print("### Bundesliga ###")
    print(bundesliga_fixtures)

    print("### Ligue 1 ###")
    print(ligue_1_fixtures)

    print("### UEFA Super Cup ###")
    print(uefa_super_cup_fixtures)

    print("### UEFA Europa ###")
    print(uefa_europa_league_fixtures)

    print("### UEFA Conference ###")
    print(uefa_europa_conference_fixtures)

    print("### League Cup ###")
    print(league_cup_fixtures)

    save_db()

if __name__ == "__main__":
    run()
