from rest_framework.serializers import ModelSerializer
from .models import (
    UefaChampsResult,
    PremierLeagueResult,
    PrimeraDivisionResult,
    SerieAResult,
    BundesligaResult,
    Ligue1Result,
    UefaSuperResult,
    UefaEuropaResult,
    UefaConfResult,
    LeagueCupResult,
)


class UefaChampsResultSerializer(ModelSerializer):
    class Meta:
        model = UefaChampsResult
        # fields = ["team_a", "team_b", "score_a", "score_b", "league", "created"]
        fields = "__all__"


class PremierLeagueResultSerializer(ModelSerializer):
    class Meta:
        model = PremierLeagueResult
        fields = "__all__"


class PrimeraDivisionResultSerializer(ModelSerializer):
    class Meta:
        model = PrimeraDivisionResult
        fields = "__all__"


class SerieAResultSerializer(ModelSerializer):
    class Meta:
        model = SerieAResult
        fields = "__all__"


class BundesligaResultSerializer(ModelSerializer):
    class Meta:
        model = BundesligaResult
        fields = "__all__"


class Ligue1ResultSerializer(ModelSerializer):
    class Meta:
        model = Ligue1Result
        fields = "__all__"


class UefaSuperResultSerializer(ModelSerializer):
    class Meta:
        model = UefaSuperResult
        fields = "__all__"


class UefaEuropaResultSerializer(ModelSerializer):
    class Meta:
        model = UefaEuropaResult
        fields = "__all__"


class UefaConfResultSerializer(ModelSerializer):
    class Meta:
        model = UefaConfResult
        fields = "__all__"


class LeagueCupResultSerializer(ModelSerializer):
    class Meta:
        model = LeagueCupResult
        fields = "__all__"
