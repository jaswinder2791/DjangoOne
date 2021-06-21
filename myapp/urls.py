from django.urls import path
from . import views

urlpatterns = [
    path('', views.myappfunc),
    path('addtocart', views.addtocart),
    path('payment', views.payment),
    path('checkout', views.checkout)
]
