from django.urls import path
from . import views

urlpatterns = [
    # the empty string means the root of this app
    path('', views.post_list, name='post_list'),
    # post detail view
    # <datatype:variable_name>
    # variable name must match name in view
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]