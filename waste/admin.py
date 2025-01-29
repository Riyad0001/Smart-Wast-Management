from django.contrib.admin import AdminSite
from .models import WasteBin, CollectionSchedule, UserReport,WasteRequest
from django.contrib import admin

class WasteAdminSite(AdminSite):
    site_header = 'Waste Management Admin'

admin_site = WasteAdminSite(name='waste_admin')
admin_site.register(WasteBin)
admin_site.register(CollectionSchedule)
# admin_site.register(UserReport)
admin.site.register(WasteBin)
admin.site.register(CollectionSchedule)
admin.site.register(UserReport)
admin.site.register(WasteRequest)
