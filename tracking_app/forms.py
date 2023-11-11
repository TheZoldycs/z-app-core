from django import forms
from .models import (
    UnitOfMeasurement,
    ExerciseType,
    MuscleGroup,
    Exercise,
    Routine,
    RoutineExercise,
    RoutineSet,
    Workout,
    WorkoutExercise,
    WorkoutSet,
    Meal,
    CalorieConsumption,
    CalorieGoal,
)

class UnitOfMeasurementForm(forms.ModelForm):
    class Meta:
        model = UnitOfMeasurement
        fields = ['name']

class ExerciseTypeForm(forms.ModelForm):
    class Meta:
        model = ExerciseType
        fields = ['name']

class MuscleGroupForm(forms.ModelForm):
    class Meta:
        model = MuscleGroup
        fields = ['name']

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'description', 'uom', 'gif', 'exercice_type', 'muscle_groups']

class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ['name', 'description']

class RoutineExerciseForm(forms.ModelForm):
    class Meta:
        model = RoutineExercise
        fields = ['routine', 'exercise', 'order', 'reps_goal']

class RoutineSetForm(forms.ModelForm):
    class Meta:
        model = RoutineSet
        fields = ['routine_exercise', 'order', 'principal_goal', 'reps_goal']

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['schedule', 'name', 'status', 'duration', 'routine', 'is_freestyle']

class WorkoutExerciseForm(forms.ModelForm):
    class Meta:
        model = WorkoutExercise
        fields = ['rest_time', 'workout', 'exercise']

class WorkoutSetForm(forms.ModelForm):
    class Meta:
        model = WorkoutSet
        fields = ['workout_exercise', 'order', 'principal_goal', 'reps_goal', 'actual_achievement', 'actual_reps']

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['meal_id', 'uom', 'qty', 'date_time', 'meal_type']

class CalorieConsumptionForm(forms.ModelForm):
    class Meta:
        model = CalorieConsumption
        fields = ['date_time', 'qty']

class CalorieGoalForm(forms.ModelForm):
    class Meta:
        model = CalorieGoal
        fields = ['goal']
