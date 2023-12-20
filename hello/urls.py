from django.urls import path
from .views import HomeTemplateView, About

urlpatterns=[
    path('', HomeTemplateView.as_view(), name='index'),
    path('about/', About.as_view(), name='about')

]