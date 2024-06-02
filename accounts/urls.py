from django.urls import path
from . import views

urlpatterns=[
path('signupaccount/', views.signupaccount, name='signupaccount'),
path('logout/',views.logoutaccount, name='logoutaccount'),
path('login/',views.loginaccount, name='loginaccount'),
path('update-profile-image/', views.update_profile_image, name='update_profile_image'),

]
 