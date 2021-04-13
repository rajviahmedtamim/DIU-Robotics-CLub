from django.urls import path
from TeamandEvent.views import EventView,PanelMember
urlpatterns = [
    path('',EventView, name='EventView'),
    path('team/',PanelMember, name='PanelMember')
]