from .views import ExerciseAPIView
from django.urls import path

urlpatterns = [
    path('exercises/', ExerciseAPIView.as_view(), name='exercise-list'),
    # note we're still adding the same ExerciseAPIView but we're passing in an id parameter to the URL pattern
    path('exercises/<int:id>/', ExerciseAPIView.as_view(), name='exercise-detail'),
]