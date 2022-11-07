from django.contrib import admin
from blog.models import ConfigIndex, ConfigAbout, ConfigContact

admin.site.register(ConfigIndex)
admin.site.register(ConfigAbout)
admin.site.register(ConfigContact)