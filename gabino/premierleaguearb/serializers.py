from rest_framework.serializers import ModelSerializer
from .models import SportpesaPremierLeague, X1betPremierLeague, MelBetPremierLeague, Bet22PremierLeague, BetikaPremierLeague

class SportpesaPremierLeagueSerializer(ModelSerializer):
    class Meta:
        model = SportpesaPremierLeague
        # fields = ["team_a", "team_b", "score_a", "score_b", "league", "created"]
        fields = "__all__"


class X1betPremierLeagueSerializer(ModelSerializer):
    class Meta:
        model = X1betPremierLeague
        fields = "__all__"


class MelBetPremierLeagueSerializer(ModelSerializer):
    class Meta:
        model = MelBetPremierLeague
        fields = "__all__"


class Bet22PremierLeagueSerializer(ModelSerializer):
    class Meta:
        model = Bet22PremierLeague
        fields = "__all__"

class BetikaPremierLeagueSerializer(ModelSerializer):
    class Meta:
        model = BetikaPremierLeague
        fields = "__all__"
