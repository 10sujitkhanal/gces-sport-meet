from django.contrib import admin

from .models import Player, PlayerInfo
# Register your models here.

class PlayerInfoInline(admin.TabularInline):
    model = PlayerInfo
    extra = 0  # how many rows to show
    max_num = 1  # Only one price per item
    min_num = 1  # Only one item store price is allowed
    can_delete = False

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    inlines = [PlayerInfoInline]