from django.contrib import admin
from .models import Session, Tournament, Organizer, Match, Category, Group, MatchDate, SingleMatch
# Register your models here.
class MatchInline(admin.TabularInline):
    model = Match

class SingleMatchInline(admin.TabularInline):
    model = SingleMatch

@admin.register(MatchDate)
class PlayerAdmin(admin.ModelAdmin):
    inlines = [SingleMatchInline, MatchInline]

admin.site.register(Session)
admin.site.register(Tournament)
admin.site.register(Organizer)
admin.site.register(Category)
admin.site.register(Group)
