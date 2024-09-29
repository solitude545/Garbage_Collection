from django.urls import path
from.import views



urlpatterns=[
    path('',views.home, name='home'),
    path('login/',views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('base/', views.base_view, name='base_view'),

    

    
]