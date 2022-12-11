from import_export import resources
from .models import AgentDir
class AdentDirData(resources.ModelResource):
    class meta:
        model=AgentDir
        