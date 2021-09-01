
from django.urls import path
from .views import*

app_name = 'private'

urlpatterns = [
    path('', home, name='home'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('data', data, name='data'),
    path('shop', shop, name='shop'),
    path('summary', summary, name='summary'),
    path('cards', cards, name='cards'),
    path("card-<int:pk>/", card, name="card"),
]