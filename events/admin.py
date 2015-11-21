from django.contrib import admin
from events.models import Event, Assistant


# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'organizer', 'place')

@admin.register(Assistant)
class AssistantAdmin(admin.ModelAdmin):
    list_display = ('assistant', 'has_paid')