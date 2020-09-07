from django.contrib import admin
from .models import Team, Player

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_created')

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'team')

admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)