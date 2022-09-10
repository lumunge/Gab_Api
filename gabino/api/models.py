from django.db import models


class UefaChampsResult(models.Model):
    team_a = models.TextField(max_length=100)
    team_b = models.TextField(max_length=100)
    score_a = models.IntegerField(null=False)
    score_b = models.IntegerField(null=False)
    league = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team_a


class PremierLeagueResult(models.Model):
    team_a = models.TextField(max_length=100)
    team_b = models.TextField(max_length=100)
    score_a = models.IntegerField(null=False)
    score_b = models.IntegerField(null=False)
    league = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team_a


class PrimeraDivisionResult(models.Model):
    team_a = models.TextField(max_length=100)
    team_b = models.TextField(max_length=100)
    score_a = models.IntegerField(null=False)
    score_b = models.IntegerField(null=False)
    league = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team_a


class SerieAResult(models.Model):
    team_a = models.TextField(max_length=100)
    team_b = models.TextField(max_length=100)
    score_a = models.IntegerField(null=False)
    score_b = models.IntegerField(null=False)
    league = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team_a


class BundesligaResult(models.Model):
    team_a = models.TextField(max_length=100)
    team_b = models.TextField(max_length=100)
    score_a = models.IntegerField(null=False)
    score_b = models.IntegerField(null=False)
    league = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team_a


class Ligue1Result(models.Model):
    team_a = models.TextField(max_length=100)
    team_b = models.TextField(max_length=100)
    score_a = models.IntegerField(null=False)
    score_b = models.IntegerField(null=False)
    league = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team_a


class UefaSuperResult(models.Model):
    team_a = models.TextField(max_length=100)
    team_b = models.TextField(max_length=100)
    score_a = models.IntegerField(null=False)
    score_b = models.IntegerField(null=False)
    league = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team_a


class UefaEuropaResult(models.Model):
    team_a = models.TextField(max_length=100)
    team_b = models.TextField(max_length=100)
    score_a = models.IntegerField(null=False)
    score_b = models.IntegerField(null=False)
    league = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team_a


class UefaConfResult(models.Model):
    team_a = models.TextField(max_length=100)
    team_b = models.TextField(max_length=100)
    score_a = models.IntegerField(null=False)
    score_b = models.IntegerField(null=False)
    league = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team_a


class LeagueCupResult(models.Model):
    team_a = models.TextField(max_length=100)
    team_b = models.TextField(max_length=100)
    score_a = models.IntegerField(null=False)
    score_b = models.IntegerField(null=False)
    league = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team_a
