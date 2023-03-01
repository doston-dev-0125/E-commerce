from django.urls import path
from.views import signup,contact_us



urlpatterns = [
 path('signup/',signup,name='signup'),
 path('contact/',contact_us,name='contact_us'),

]