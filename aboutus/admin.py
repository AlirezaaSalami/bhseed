from django.contrib import admin
from .models import AboutUs


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'content',)


admin.site.register(AboutUs, AboutUsAdmin)
