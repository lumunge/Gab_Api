from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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

from .serializers import (
    UefaChampsResultSerializer,
    PremierLeagueResultSerializer,
    PrimeraDivisionResultSerializer,
    SerieAResultSerializer,
    BundesligaResultSerializer,
    Ligue1ResultSerializer,
    UefaSuperResultSerializer,
    UefaEuropaResultSerializer,
    UefaConfResultSerializer,
    LeagueCupResultSerializer,
)

from rest_framework.decorators import api_view


# class UefaChampsResultView(APIView):

# add permissions


@api_view(["GET"])
def get_uefa_champ(request):
    matches = UefaChampsResult.objects.all().order_by("-created")
    serializer = UefaChampsResultSerializer(matches, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_premier_league(request):
    matches = PremierLeagueResult.objects.all().order_by("-created")
    serializer = PremierLeagueResultSerializer(matches, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_primera_division(request):
    matches = PrimeraDivisionResult.objects.all().order_by("-created")
    serializer = PrimeraDivisionResultSerializer(matches, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_serie_a(request):
    matches = SerieAResult.objects.all().order_by("-created")
    serializer = SerieAResultSerializer(matches, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_bundesliga(request):
    matches = BundesligaResult.objects.all().order_by("-created")
    serializer = BundesligaResultSerializer(matches, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_ligue_1(request):
    matches = Ligue1Result.objects.all().order_by("-created")
    serializer = Ligue1ResultSerializer(matches, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_uefa_super(request):
    matches = UefaSuperResult.objects.all().order_by("-created")
    serializer = UefaSuperResultSerializer(matches, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_uefa_europa(request):
    matches = UefaEuropaResult.objects.all().order_by("-created")
    serializer = UefaEuropaResultSerializer(matches, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_uefa_conference(request):
    matches = UefaConfResult.objects.all().order_by("-created")
    serializer = UefaConfResultSerializer(matches, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_league_cup(request):
    matches = LeagueCupResult.objects.all().order_by("-created")
    serializer = LeagueCupResultSerializer(matches, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(["POST"])
# def create_matches(request):
#     data = request.data
#     result = UefaChampsResult.objects.create(data)
#     serializer = UefaChampsResultSerializer(result, many=True)
#     # if serializer.is_valid():
#     #     serializer.save()
#     return Response(serializer.data)
#     # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def create_uefa_matches(request):
    data = request.data
    serializer = UefaChampsResultSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    response = Response()
    response.data = {"message": "Match created successfully", "data": serializer.data}
    return response


# def create_matches(request):
#     data = {
#         "team_a": request.data.get("team_a"),
#         "team_b": request.data.get("team_b"),
#         "score_a": request.data.get("score_a"),
#         "score_b": request.data.get("score_b"),
#         "league": request.data.get("league"),
#     }

#     serializer = UefaChampsResultSerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
