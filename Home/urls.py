from django.contrib import admin
from django.urls import path,include
from Home import views
from Home.views import index
from django.conf.urls import url 

urlpatterns = [
    path('', views.index, name="Home"),
    path('grants/', views.grants, name="Grants"),
    path('case_studies/', views.case_studies, name="Case-Studies"),
    path("view_grant", views.view_grant, name="view-grant"),
    path("view_case_study", views.view_case_study, name="view-case-study"),
    url(r'^$', index, name="home")
]

handler404 = 'Home.views.handler404'