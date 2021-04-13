from django.contrib import admin
from Club_Project_App.models import ProjectCategory, ClubProjects


class AdminProjectCategory(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at','updated_at']
    list_filter = ['status', 'created_at']
    prepopulated_fields = {'slug':('title',)}


class AdminClubProjects(admin.ModelAdmin):
    list_display = ['title','image_tag','status','created_at','updated_at']
    list_filter = ['status','created_at']
    prepopulated_fields = {'slug':('title',)}

    class Media:
        js= ('tinyInject.js',)


admin.site.register(ProjectCategory, AdminProjectCategory)
admin.site.register(ClubProjects, AdminClubProjects)


