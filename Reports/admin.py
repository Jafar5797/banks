from django.contrib import admin
from .models import Report,Q_Report,QueryFiles,ResponseFiles
# Register your models here.

class reportAdmin(admin.ModelAdmin):
	readonly_fields = ('date',)
admin.site.register(Report,reportAdmin)

admin.site.register(Q_Report)

admin.site.register(QueryFiles)
admin.site.register(ResponseFiles)
