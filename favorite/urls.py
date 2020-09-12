from django.urls import path
from .views import favorite


#http://localhost:8000/favorite/
urlpatterns = [
    path('', favorite, name='favorite'),

]