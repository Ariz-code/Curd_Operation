
from django.urls import path
from curdapp import views

urlpatterns = [
    
    path('',views.home,name='default'),
    path('about/',views.myfun,name='about'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('delete/<int:key>',views.delete,name='delete'),
    path('edit/<int:key>',views.edit,name='edit'),
    path('doedit/<int:key>',views.doedit,name='doedit'),
    
    
]