from django.contrib import admin
from people.models import Person, Pet


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'owner')


admin.site.register(Person, PersonAdmin)
admin.site.register(Pet, PetAdmin)