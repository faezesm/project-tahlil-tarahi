
from django.urls import path
from . import views

app_name='website'

urlpatterns = [
    
    path('first/',views.first,name='first'), 
    path('about/',views.about,name='about'),
    path('bofe/',views.bofe,name='bofe'), 
    path('entazamat/',views.entazamat,name='entazamat'),
    path('tasisat1/',views.tasisat1,name='tasisat1'),
    path('',views.login,name='login'), 
    path('registery/',views.registery,name='registery'), 
    
]
