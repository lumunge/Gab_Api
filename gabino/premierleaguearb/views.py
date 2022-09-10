# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import SportpesaPremierLeague, X1betPremierLeague, MelBetPremierLeague, Bet22PremierLeague, BetikaPremierLeague
# from .serializers import SportpesaPremierLeagueSerializer, X1betPremierLeagueSerializer, MelBetPremierLeagueSerializer, Bet22PremierLeagueSerializer, BetikaPremierLeagueSerializer
# from rest_framework.decorators import api_view



# @api_view(["GET"])
# def get_sp_premier_league(request):
#     matches = SportpesaPremierLeague.objects.all().order_by("-created")
#     serializer = SportpesaPremierLeagueSerializer(matches, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


