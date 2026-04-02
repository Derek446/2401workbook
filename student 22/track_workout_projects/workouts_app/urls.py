from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExerciseAPIView, WorkoutViewSet

router = DefaultRouter()

router.register(r'workouts', WorkoutViewSet)

urlpatterns = [

    path('exercises/', ExerciseAPIView.as_view(), name='exercise-api'),
    path('exercises/<int:id>/', ExerciseAPIView.as_view(), name='exercise-detail'),
] + router.urls