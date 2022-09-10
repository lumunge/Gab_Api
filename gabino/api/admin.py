from django.contrib import admin
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

admin.site.register(UefaChampsResult)
admin.site.register(PremierLeagueResult)
admin.site.register(PrimeraDivisionResult)
admin.site.register(SerieAResult)
admin.site.register(BundesligaResult)
admin.site.register(Ligue1Result)
admin.site.register(UefaSuperResult)
admin.site.register(UefaEuropaResult)
admin.site.register(UefaConfResult)
admin.site.register(LeagueCupResult)
