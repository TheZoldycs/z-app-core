from django.db import models

class UnitOfMeasurement(models.Model):
    """
    Model to represent units of measurement.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Unit of Measurement"
        verbose_name_plural = "Units of Measurement"

class ExerciseType(models.Model):
    """
    Model to represent exercise types.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Exercise Type"
        verbose_name_plural = "Exercise Types"

class MuscleGroup(models.Model):
    """
    Model to represent muscle groups.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Muscle Group"
        verbose_name_plural = "Muscle Groups"

class Exercise(models.Model):
    """
    Model to represent exercises.
    """
    name = models.CharField(max_length=255, verbose_name="Exercise Name")
    description = models.TextField(verbose_name="Exercise Description")
    uom = models.ForeignKey(UnitOfMeasurement, on_delete=models.CASCADE, verbose_name="Unit of Measurement")
    gif = models.URLField(verbose_name="GIF URL")
    exercice_type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE, verbose_name="Exercise Type")
    muscle_groups = models.ManyToManyField(MuscleGroup, verbose_name="Muscle Groups")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Exercises"

class Routine(models.Model):
    """
    Model to represent workout routines.
    """
    name = models.CharField(max_length=255, verbose_name="Routine Name")
    description = models.TextField(verbose_name="Routine Description")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Routines"

class RoutineExercise(models.Model):
    """
    Model to represent exercises within a routine.
    """
    rest_time = models.PositiveIntegerField(verbose_name="Rest Time")
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE, verbose_name="Routine")
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, verbose_name="Exercise")
    order = models.PositiveIntegerField(verbose_name="Order")
    reps_goal = models.PositiveIntegerField(verbose_name="Reps Goal")

class RoutineSet(models.Model):
    """
    Model to represent sets within a routine exercise.
    """
    routine_exercise = models.ForeignKey(RoutineExercise, on_delete=models.CASCADE, verbose_name="Routine Exercise")
    order = models.PositiveIntegerField(verbose_name="Order")
    principal_goal = models.CharField(max_length=50, verbose_name="Principal Goal")
    reps_goal = models.PositiveIntegerField(verbose_name="Reps Goal")

class Workout(models.Model):
    """
    Model to represent workouts.
    """
    schedule = models.DateTimeField(verbose_name="Schedule")
    name = models.CharField(max_length=255, verbose_name="Workout Name")
    status = models.CharField(max_length=20, verbose_name="Status")
    duration = models.PositiveIntegerField(verbose_name="Duration")
    routine = models.ForeignKey(Routine, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Routine")
    is_freestyle = models.BooleanField(default=False, verbose_name="Is Freestyle")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Workouts"

class WorkoutExercise(models.Model):
    """
    Model to represent exercises within a workout.
    """
    rest_time = models.PositiveIntegerField(verbose_name="Rest Time")
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, verbose_name="Workout")
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, verbose_name="Exercise")
    order = models.PositiveIntegerField(verbose_name="Order")
    reps_goal = models.PositiveIntegerField(verbose_name="Reps Goal")
    def __str__(self):
        return self.exercise

    class Meta:
        verbose_name_plural = "Workout Exercices"

class WorkoutSet(models.Model):
    """
    Model to represent sets within a workout exercise.
    """
    workout_exercise = models.ForeignKey(WorkoutExercise, on_delete=models.CASCADE, verbose_name="Workout Exercise")
    order = models.PositiveIntegerField(verbose_name="Order")
    principal_goal = models.CharField(max_length=50, verbose_name="Principal Goal")
    reps_goal = models.PositiveIntegerField(verbose_name="Reps Goal")
    actual_achievement = models.PositiveIntegerField(verbose_name="Actual Achievement")
    actual_reps = models.PositiveIntegerField(verbose_name="Actual Reps")
    def __str__(self):
        return f"{self.workout_exercise}-{self.order}-{self.principal_goal}"

    class Meta:
        verbose_name_plural = "Workout Sets"

class Meal(models.Model):
    """
    Model to represent meals.
    """
    meal_id = models.PositiveIntegerField(verbose_name="Meal ID")
    uom = models.ForeignKey(UnitOfMeasurement, on_delete=models.CASCADE, verbose_name="Unit of Measurement")
    qty = models.FloatField(verbose_name="Quantity")
    date_time = models.DateTimeField(verbose_name="Date and Time")
    meal_type = models.CharField(max_length=255, verbose_name="Meal Type")
    def __str__(self):
        return f"{self.meal_id}-{self.uom}-{self.qty}"

    class Meta:
        verbose_name_plural = "Meals"

class CalorieConsumption(models.Model):
    """
    Model to represent calorie consumption.
    """
    date_time = models.DateTimeField(verbose_name="Date and Time")
    qty = models.FloatField(verbose_name="Quantity")
    def __str__(self):
        return f"{self.date_time}-{self.qty}"

    class Meta:
        verbose_name_plural = "Calories Consumptions"

class CalorieGoal(models.Model):
    """
    Model to represent calorie goals.
    """
    goal = models.PositiveIntegerField(verbose_name="Goal")
    def __str__(self):
        return f"{self.id}-{self.goal}"
