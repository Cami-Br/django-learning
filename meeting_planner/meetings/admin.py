from django.contrib import admin
from meetings.models import Meeting, Room
from django.contrib.admin import ModelAdmin


admin.site.register(Room)


@admin.register(Meeting)
class MeetingAdmin(ModelAdmin):
    model = Meeting
    list_display = ("id", "title", "date", "start_time", "room")
    ordering = ("date", "start_time")
    search_fields = ("title",)
