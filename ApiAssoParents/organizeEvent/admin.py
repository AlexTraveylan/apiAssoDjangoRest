from django.contrib import admin

from organizeEvent.models import ToDo, Organisation

# Register your models here.

class ToDoAdmin(admin.ModelAdmin):

    list_display = ('description', 'isChecked')

class OrganisationAdmin(admin.ModelAdmin):

    list_display = ("typeEvent", "description", "lieu", "date", "toDo", "horaire", "tarifs")

    @admin.display(description='toDo')
    def toDo(self, obj):
        return len(obj)
        


admin.site.register(ToDo, ToDoAdmin)
admin.site.register(Organisation, OrganisationAdmin)