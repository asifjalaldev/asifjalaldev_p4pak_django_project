from django.contrib import admin
from .models import AgentCity, AgentDir, batch
from import_export.admin import ImportExportModelAdmin


#class AgentDirList(admin.ModelAdmin):
   # list_display=('name','city','phoneNo', 'img','address')

# Register your models here.
#admin.site.register(AgentDir,AgentDirList)
admin.site.register(batch)
admin.site.register(AgentCity)
@admin.register(AgentDir)#addiing agentDirList in orgin registery and uncomment the agentdirList func
class agentData(ImportExportModelAdmin):
   pass
# https://downloader.la/  website which allow you to download paid images