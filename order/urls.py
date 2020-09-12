from django.urls import path
from .views import order


#http://localhost:8000/order/
urlpatterns = [
    path('', order, name='order'),

]