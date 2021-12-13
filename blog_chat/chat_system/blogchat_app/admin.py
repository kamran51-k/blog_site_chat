from django.contrib import admin

from blogchat_app.models import AboutModel, LogoModel, NavbarModel, PostModel

# Register your models here.
admin.site.register(NavbarModel)
admin.site.register(PostModel)
admin.site.register(LogoModel)
admin.site.register(AboutModel)