from django.urls import path
from atlasgrid.views import view
from atlasgrid.views import AtlasGridInfo

app_name = 'atlasgrid'

urlpatterns = [
    path('', view),
]
