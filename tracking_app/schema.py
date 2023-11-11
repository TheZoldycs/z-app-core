import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
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
from graphene_django.forms.mutation import DjangoModelFormMutation
from .forms import (
    UnitOfMeasurementForm,
    ExerciseTypeForm,
    MuscleGroupForm,
    ExerciseForm,
    RoutineForm,
    RoutineExerciseForm,
    RoutineSetForm,
    WorkoutForm,
    WorkoutExerciseForm,
    WorkoutSetForm,
    MealForm,
    CalorieConsumptionForm,
    CalorieGoalForm,
)

class UnitOfMeasurementType(DjangoObjectType):
    class Meta:
        model = UnitOfMeasurement
        fields = ("id", "name")
        filter_fields = ["id", "name"]
        interfaces = (relay.Node, )

class ExerciseTypeType(DjangoObjectType):
    class Meta:
        model = ExerciseType
        fields = ("id", "name")
        filter_fields = ["id", "name"]
        interfaces = (relay.Node, )

class MuscleGroupType(DjangoObjectType):
    class Meta:
        model = MuscleGroup
        fields = ("id", "name")
        filter_fields = ["id", "name"]
        interfaces = (relay.Node, )

class ExerciseType(DjangoObjectType):
    class Meta:
        model = Exercise
        fields = ("id", "name","description", "uom", "gif", "exercice_type" , "muscle_groups")
        filter_fields = ["id", "name","description", "uom", "gif", "exercice_type" , "muscle_groups"]
        interfaces = (relay.Node, )

class RoutineSetType(DjangoObjectType):
    class Meta:
        model = RoutineSet
        fields = ("id", "routine_exercise", "order", "principal_goal", "reps_goal")
        filter_fields = ["id", "routine_exercise", "order", "principal_goal", "reps_goal"]
        interfaces = (relay.Node, )

class RoutineExerciseType(DjangoObjectType):
    class Meta:
        model = RoutineExercise
        fields = ("id", "routine", "exercise", "order", "reps_goal")
        filter_fields = ["id", "routine", "exercise", "order", "reps_goal"]
        interfaces = (relay.Node, )
    sets = DjangoFilterConnectionField(RoutineSetType)

    def resolve_sets(self, info):
        return RoutineSetType.objects.filter(routine_exercise=self)

class RoutineType(DjangoObjectType):
    class Meta:
        model = Routine
        fields = ("id", "name", "description")
        filter_fields = ["id", "name", "description"]
        interfaces = (relay.Node, )
    exercises = DjangoFilterConnectionField(RoutineExerciseType)

    def resolve_exercises(self, info):
        return RoutineExercise.objects.filter(routine=self)

class WorkoutSetType(DjangoObjectType):
    class Meta:
        model = WorkoutSet
        fields = ("id", "workout_exercise", "order", "principal_goal", "reps_goal", "actual_achievement", "actual_reps")
        filter_fields = ["id", "workout_exercise", "order", "principal_goal", "reps_goal", "actual_achievement", "actual_reps"]
        interfaces = (relay.Node, )

class WorkoutExerciseType(DjangoObjectType):
    class Meta:
        model = WorkoutExercise
        fields = ("id", "rest_time", "workout", "exercise")
        filter_fields = ["id", "rest_time", "workout", "exercise"]
        interfaces = (relay.Node, )
    sets = DjangoFilterConnectionField(WorkoutSetType)

    def resolve_sets(self, info):
        return WorkoutSetType.objects.filter(workout_exercise=self)

class WorkoutType(DjangoObjectType):
    class Meta:
        model = Workout
        fields = ("id", "schedule", "name", "status", "duration", "routine", "is_freestyle")
        filter_fields = ["id", "schedule", "name", "status", "duration", "routine", "is_freestyle"]
        interfaces = (relay.Node, )
    exercises = DjangoFilterConnectionField(WorkoutExerciseType)

    def resolve_exercises(self, info):
        return WorkoutExerciseType.objects.filter(workout=self)

class MealType(DjangoObjectType):
    class Meta:
        model = Meal
        fields = ("id", "meal_id", "uom", "qty", "date_time", "meal_type")
        filter_fields = ["id", "meal_id", "uom", "qty", "date_time", "meal_type"]
        interfaces = (relay.Node, )

class CalorieConsumptionType(DjangoObjectType):
    class Meta:
        model = CalorieConsumption
        fields = ("id", "date_time", "qty")
        filter_fields = ["id", "date_time", "qty"]
        interfaces = (relay.Node, )

class CalorieGoalType(DjangoObjectType):
    class Meta:
        model = CalorieGoal
        fields = ("id", "goal")
        filter_fields = ["id", "goal"]
        interfaces = (relay.Node, )

class UnitOfMeasurementMutation(DjangoModelFormMutation):
    class Meta:
        form_class = UnitOfMeasurementForm

class ExerciseTypeMutation(DjangoModelFormMutation):
    class Meta:
        form_class = ExerciseTypeForm

class MuscleGroupMutation(DjangoModelFormMutation):
    class Meta:
        form_class = MuscleGroupForm

class ExerciseMutation(DjangoModelFormMutation):
    class Meta:
        form_class = ExerciseForm

class RoutineMutation(DjangoModelFormMutation):
    class Meta:
        form_class = RoutineForm

class RoutineExerciseMutation(DjangoModelFormMutation):
    class Meta:
        form_class = RoutineExerciseForm

class RoutineSetMutation(DjangoModelFormMutation):
    class Meta:
        form_class = RoutineSetForm

class WorkoutMutation(DjangoModelFormMutation):
    class Meta:
        form_class = WorkoutForm

class WorkoutExerciseMutation(DjangoModelFormMutation):
    class Meta:
        form_class = WorkoutExerciseForm

class WorkoutSetMutation(DjangoModelFormMutation):
    class Meta:
        form_class = WorkoutSetForm

class MealMutation(DjangoModelFormMutation):
    class Meta:
        form_class = MealForm

class CalorieConsumptionMutation(DjangoModelFormMutation):
    class Meta:
        form_class = CalorieConsumptionForm

class CalorieGoalMutation(DjangoModelFormMutation):
    class Meta:
        form_class = CalorieGoalForm

class Query(graphene.ObjectType):
    units_of_measurement = DjangoFilterConnectionField(UnitOfMeasurementType)
    exercise_types = DjangoFilterConnectionField(ExerciseTypeType)
    muscle_groups = DjangoFilterConnectionField(MuscleGroupType)
    exercises = DjangoFilterConnectionField(ExerciseType)
    routines = DjangoFilterConnectionField(RoutineType)
    routine_exercises = DjangoFilterConnectionField(RoutineExerciseType)
    routine_sets = DjangoFilterConnectionField(RoutineSetType)
    workouts = DjangoFilterConnectionField(WorkoutType)
    workout_exercises = DjangoFilterConnectionField(WorkoutExerciseType)
    workout_sets = DjangoFilterConnectionField(WorkoutSetType)
    meals = DjangoFilterConnectionField(MealType)
    calorie_consumptions = DjangoFilterConnectionField(CalorieConsumptionType)
    calorie_goals = DjangoFilterConnectionField(CalorieGoalType)

class Mutation(graphene.ObjectType):
    create_unit_of_measurement = UnitOfMeasurementMutation.Field()
    create_exercise_type = ExerciseTypeMutation.Field()
    create_muscle_group = MuscleGroupMutation.Field()
    create_exercise = ExerciseMutation.Field()
    create_routine = RoutineMutation.Field()
    create_routine_exercise = RoutineExerciseMutation.Field()
    create_routine_set = RoutineSetMutation.Field()
    create_workout = WorkoutMutation.Field()
    create_workout_exercise = WorkoutExerciseMutation.Field()
    create_workout_set = WorkoutSetMutation.Field()
    create_meal = MealMutation.Field()
    create_calorie_consumption = CalorieConsumptionMutation.Field()
    create_calorie_goal = CalorieGoalMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

