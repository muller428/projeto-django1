from recipes.views import contato, home, sobre
from django.urls import path

urlpatterns = [
    path('', home),     # home
    path('sobre/', sobre),  # /sobre/
    path('contato/', contato),  # /contato/
]
