from django.contrib import admin

from .models import Workshop, Classroom

# Register your models here.
# admin.site.register(Workshop)

@admin.register(Workshop)
class WorkShopAdmin(admin.ModelAdmin):
    list_display = ["name", "classroom", "date"]

admin.site.register(Classroom)