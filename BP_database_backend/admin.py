from django.contrib import admin

# Register your models here.
from .models import User, Project


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    search_fields = ('name',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'submitter', 'FA', 'summary', 'file_BP', 'file_datapack', )
    readonly_fields = ('last_update_time', )
    search_fields = ('name', 'submitter', 'category', 'FA')


admin.site.register(User, UserAdmin)
admin.site.register(Project, ProjectAdmin)
