from django.urls import path

from .views import update_profile, profile_list

urlpatterns = [
    path('', profile_list, name='profile_list'),
    path('edit/', update_profile, name='profile_edit'),
]