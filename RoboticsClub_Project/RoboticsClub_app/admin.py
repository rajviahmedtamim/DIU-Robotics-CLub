from django.contrib import admin
from RoboticsClub_app.models import Setting, ContactMessage, AboutCateory, DURCGallery

# , ClubCategory
admin.site.register(Setting)
admin.site.register(ContactMessage)
admin.site.register(AboutCateory)
# admin.site.register(ClubCategory)
admin.site.register(DURCGallery)
