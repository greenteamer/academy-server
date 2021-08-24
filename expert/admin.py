from django.contrib import admin

from expert.models import Expert


class ExpertAdmin(admin.ModelAdmin):
    model = Expert


admin.site.register(Expert, ExpertAdmin)
