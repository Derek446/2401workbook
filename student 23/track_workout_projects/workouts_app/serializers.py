from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Exercise, Workout, WorkoutLog


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'title', 'date']

class ExerciseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    exercise_type = serializers.ChoiceField(choices=Exercise.EXERCISE_TYPES)

    def validate_name(self, value):
        INVALID_EXERCISE_NAMES = ["sitting", "lying down"]
        if value in INVALID_EXERCISE_NAMES:
            raise serializers.ValidationError("Exercise name cannot be 'sitting' or 'lying down'.")
        return value

    def create(self, validated_data):
        return Exercise.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.exercise_type = validated_data.get('exercise_type', instance.exercise_type)
        instance.save()
        return instance

class UserReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email']

class WorkoutLogReadOnlySerializer(serializers.ModelSerializer):
    # include the workout's information in the response
    workout = WorkoutSerializer(read_only=True)
    # include the exercises in the workout log
    exercise = ExerciseSerializer(read_only=True)
    user = UserReadOnlySerializer(read_only=True)

    class Meta:
        model = WorkoutLog
        fields = [
            'id',
            'sets',
            'reps',
            'weight_kg',
            'time',
            # override the default
            'workout',
            'exercise',
            'user'
        ]

class WorkoutLogCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutLog
        fields = [
            'id',
            'sets',
            'reps',
            'weight_kg',
            'time',
            # foreign key fields
            'workout',
            'exercise',
            'user'
        ]