from django.contrib import admin
from .models import CustomUser, Games, PurchasedGame


admin.site.register(CustomUser)
admin.site.register(Games)
admin.site.register(PurchasedGame)
