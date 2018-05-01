from django.contrib import admin
from django.conf.urls import url,include
from . import views
from myport.views import LangProc

urlpatterns = [
    url(r'^$', views.home,name = 'home'),
    url(r'^LanguageHome/$', views.LHome,name = 'LHome'),
    url(r'^AWSHome/$', views.AWSHome,name = 'AWSHome'),
    url(r'^StudyTree/$', views.Stree,name = 'Stree'),
    url(r'^Lpython3/$',LangProc.as_view(),name = 'LPython3'),
]
