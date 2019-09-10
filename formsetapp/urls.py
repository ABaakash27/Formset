from django.urls import path, include
from .import views
from formsetapp.views import *
urlpatterns = [


path('',CustomerCreateView.as_view(),name="CustomerCreateView"),
]