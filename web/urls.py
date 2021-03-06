from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('lists/', views.lists, name='lists'),
    path('lists/create/', views.createList, name='createList'),
    path('list/close/<int:id>/', views.closeList, name='closeList'),
    path('plays/<int:id>/', views.plays, name='plays'),
    path('players/', views.players, name='players'),
    path('players/<int:id>/', views.playerDetail, name='player-detail'),
    path('players/create/', views.createPlayer, name='createPlayer'),
    path('dealers/', views.dealers, name='dealers'),
    path('dealers/<int:id>/', views.dealerDetail, name='dealer-detail'),
    path('dealers/create/', views.createDealer, name='createDealer'),
]