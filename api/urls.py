from django.urls import path, include
from . import views

# from .views import UefaChampsResultView

urlpatterns = [
    path("get_uefa_champ/", views.get_uefa_champ, name="get_uefa_champ"),
    path("get_premier_league/", views.get_premier_league, name="get_premier_league"),
    path(
        "get_primera_division/", views.get_primera_division, name="get_primera_division"
    ),
    path("get_serie_a/", views.get_serie_a, name="get_serie_a"),
    path("get_bundesliga/", views.get_bundesliga, name="get_bundesliga"),
    path("get_ligue_1/", views.get_ligue_1, name="get_ligue_1"),
    path("get_uefa_super/", views.get_uefa_super, name="get_uefa_super"),
    path("get_uefa_europa/", views.get_uefa_europa, name="get_uefa_europa"),
    path("get_uefa_conference/", views.get_uefa_conference, name="get_uefa_conference"),
    path("get_league_cup/", views.get_league_cup, name="get_league_cup"),
    # create
    path("create_uefa_matches/", views.create_uefa_matches, name="create_uefa_matches"),
]
