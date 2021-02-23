from django.urls import path
from . import views

urlpatterns = [
    path('', views.hi,name='home-page'),
    path('postsign/', views.postsign,name='dashboard'),
    path('insertCollection/', views.insertCollection,name='inserted'),
]