from django.db import models
from django.contrib.auth.models import User


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
class Games(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    url = models.CharField(max_length=200)
    developer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image_path = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    salesCount = models.IntegerField(default=0)
class PurchasedGame(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    player = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    highScore = models.IntegerField(default=0)
    gameState = models.CharField(max_length=1000, default = "")
    time_of_purchase = models.DateTimeField()
    
