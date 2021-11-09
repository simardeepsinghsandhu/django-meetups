from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='all-meetups'),  #ourDomain.com/meetups
    path('<slug:meetup_slug>/success/', views.confirmation_registration, name = 'confirm-registration'),
    path('<slug:meetup_slug>/', views.meetup_details, name='meetup-detail')    #our-domain.com/meetups/dynamic-path   
]