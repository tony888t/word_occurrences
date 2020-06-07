from django.urls import path

from . import views


urlpatterns = [
    path('', views.Words.as_view(), name='word')
]
