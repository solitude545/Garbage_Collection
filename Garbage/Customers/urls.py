from django.urls import path
from.import views



urlpatterns=[
    path('',views.home, name='home'),
    path('login/',views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('base/', views.base_view, name='base_view'),
    path('bio/',views.bio_view,name='bio_view'),
    path('nonbio/',views.nonbio_view,name='nonbio_view'),
    path('haz/',views.haz_view,name='haz_view'),
    path('order/',views.order_view,name='order_view'),
    path('map/',views.map_view,name='map_view'),
    path('submit_location',views.submit_location,name='submit_location'),
    

    
]