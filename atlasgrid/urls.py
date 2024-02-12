from django.urls import path, include
from atlasgrid.views import view
from atlasgrid.views import AtlasGridInfo

app_name = 'atlasgrid'

urlpatterns = [
    path('', view),
    path('monitor/', view, name='monitor')
]
