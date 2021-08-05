from django.urls import path 
from studentadd import views

urlpatterns = [
    path('home/',views.home,name="home"),
    path('display/',views.display,name="display"),
    path('delete/<sid>', views.delete,name="delete"),
    path('update/<sid>',views.update,name='update'),
        
]
