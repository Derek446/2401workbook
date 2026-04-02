from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ExerciseSerializer
from .models import Exercise

class ExerciseAPIView(APIView):
    def get(self, request, id=None):
        # detail view
        if id:
            exercise = get_object_or_404(Exercise, id=id)
            serializer = ExerciseSerializer(exercise)
            return Response(serializer.data)
        # list view
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ExerciseSerializer(data=request.data)
        if serializer.is_valid():
            exercise = serializer.save()
            return Response(ExerciseSerializer(exercise).data, status=201) # 201 Created indicates that the request was successful and a new resource was created as a result.
        return Response(serializer.errors, status=400)
        # let's add a function that will update the existing exercise instance when we receive valid data
    
    def update(self, request, id, partial=False):
        exercise = get_object_or_404(Exercise, id=id)
        serializer = ExerciseSerializer(exercise, data=request.data, partial=partial)
        if serializer.is_valid():
            exercise = serializer.save()
            return Response(ExerciseSerializer(exercise).data) # 200 OK indicates that the request was successful and the response contains the updated exercise data.
        return Response(serializer.errors, status=400) # 400 Bad Request indicates that the server cannot process the request due to a client error (e.g., validation errors).

    # we can use the same update function for both PUT and PATCH requests by passing in the partial argument
    def put(self, request, id):
        return self.update(request, id, partial=False)

    def patch(self, request, id):
        return self.update(request, id, partial=True)
    
    def delete(self, request, id):
        exercise = get_object_or_404(Exercise, id=id)
        exercise.delete()
        return Response(status=204) # 204 No Content indicates that the request was successful but there is no content to return in the response.