from django.urls import path
from . import views 
urlpatterns = [
    path('', views.home),
    path('response/', views.response),
    path('getuser/<name>/<id>', views.pathview, name='pathview'), 
    path('getuser/', views.qryview, name='qryview'),
    path("showform/", views.showform, name="showform"), 
    path("myapp/getform/", views.getform, name='getform'),
    path('dishes/<str:dish>', views.menuitems), #dish=pasta
    path('drinks/<str:drink_name>', views.drinks, name="drink_name"), 
    path('aboutus/', views.about, name="about"),
    path('menu/', views.menu, name= "menu"),
    path('book/', views.book, name="book"),
]