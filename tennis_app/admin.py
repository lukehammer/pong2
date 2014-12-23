from django.contrib import admin
from tennis_app.models import gamePlayer, gameRecord, gameLobby

admin.site.register(gamePlayer)
admin.site.register(gameRecord)
admin.site.register(gameLobby)