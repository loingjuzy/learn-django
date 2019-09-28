from django.urls import path
from . import views as cm

urlpatterns = [
    path('', cm.login),
]