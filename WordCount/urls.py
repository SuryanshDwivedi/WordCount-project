
from django.urls import path
from . import views
urlpatterns = [
    path('',views.hello,name='home'),
    path('count',views.count,name='count'),
    path('countwords',views.count,name='count'),
    path('about',views.about,name='about'),
]
