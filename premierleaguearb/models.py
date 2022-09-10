from django.db import models


class SportpesaPremierLeague(models.Model):
    team_a = models.TextField(max_length=100, null=True, blank=True)
    team_b = models.TextField(max_length=100, null=True, blank=True)
    odd_a = models.IntegerField(null=True, blank=True)
    odd_b = models.IntegerField(null=True, blank=True)
    odd_c = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team_a


class X1betPremierLeague(models.Model):
    team_a = models.TextField(max_length=100, null=True, blank=True)
    team_b = models.TextField(max_length=100, null=True, blank=True)
    odd_a = models.IntegerField(null=True, blank=True)
    odd_b = models.IntegerField(null=True, blank=True)
    odd_c = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team_a


class MelBetPremierLeague(models.Model):
    team_a = models.TextField(max_length=100, null=True, blank=True)
    team_b = models.TextField(max_length=100, null=True, blank=True)
    odd_a = models.IntegerField(null=True, blank=True)
    odd_b = models.IntegerField(null=True, blank=True)
    odd_c = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team_a


class Bet22PremierLeague(models.Model):
    team_a = models.TextField(max_length=100, null=True, blank=True)
    team_b = models.TextField(max_length=100, null=True, blank=True)
    odd_a = models.IntegerField(null=True, blank=True)
    odd_b = models.IntegerField(null=True, blank=True)
    odd_c = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team_a

class BetikaPremierLeague(models.Model):
    team_a = models.TextField(max_length=100, null=True, blank=True)
    team_b = models.TextField(max_length=100, null=True, blank=True)
    odd_a = models.IntegerField(null=True, blank=True)
    odd_b = models.IntegerField(null=True, blank=True)
    odd_c = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team_a