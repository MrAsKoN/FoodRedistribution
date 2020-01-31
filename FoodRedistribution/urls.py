from django.contrib import admin
from django.urls import path
from users import views as usersviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', usersviews.base, name='home'),
    path('/', usersviews.base, name='home'),
    path('addHungerSpot/', usersviews.addHungerSpot, name='addHungerSpot')
]
