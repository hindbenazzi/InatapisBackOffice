from django.urls import path
from . import views

urlpatterns = [
    path('', views.hi,name='home-page'),
    path('postsign/', views.postsign,name='dashboard'),
    path('insertCollection/', views.insertCollection,name='inserted'),
    path('showCollection/', views.showCollection,name='show'),
    path('home/', views.gethome,name='home'),
    path('signout/', views.signout,name='signout'),
    path('editItem/', views.editItem,name='edit'),
    path('deleteItem/', views.deleteItem,name='delete'),
    path('updateCollection/', views.updateCollection,name='updateCollection'),

]