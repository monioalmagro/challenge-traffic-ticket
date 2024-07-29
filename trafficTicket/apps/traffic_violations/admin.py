from django.contrib import admin

from .models import Officer, Person, Vehicle, Violation


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    search_fields = ("name", "email")


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ("license_plate", "brand", "color", "owner")
    search_fields = ("license_plate", "brand", "color")
    list_filter = ("brand", "color")


@admin.register(Officer)
class OfficerAdmin(admin.ModelAdmin):
    list_display = ("name", "badge_number")
    search_fields = ("name", "badge_number")


@admin.register(Violation)
class ViolationAdmin(admin.ModelAdmin):
    list_display = ("vehicle", "timestamp", "comments")
