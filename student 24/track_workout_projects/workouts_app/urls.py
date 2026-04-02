from .views import ExerciseAPIView, WorkoutViewSet, WorkoutLogAPIView, ExerciseSearchViewSet

from rest_framework.routers import DefaultRouter

from django.urls import path

router = DefaultRouter()
router.register(r'workouts', WorkoutViewSet, basename='workout')
router.register(r'exercises/results',
                ExerciseSearchViewSet,
                basename='exercise-search')

urlpatterns = [
    path('workout-logs/', WorkoutLogAPIView.as_view(), name='workout-log-api'),
    path('workout-logs/<int:id>/', WorkoutLogAPIView.as_view(), name='workout-log-detail'),
    path('exercises/', ExerciseAPIView.as_view(), name='exercise-api'),
    path('exercises/<int:id>/', ExerciseAPIView.as_view(), name='exercise-detail'),
] + router.urls
