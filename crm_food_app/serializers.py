from rest_framework import serializers
from .models import *


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']

    def create(self, validated_data):
        return Role.objects.create(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'surname', 'login',
                  'password', 'email', 'role','date','phone']

        def create(self, validated_data):
            return User.objects.create(**validated_data)


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'name']

    def create(self, validated_data):
        return Status.objects.create(**validated_data)


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'name']

    def create(self, validated_data):
        return Table.objects.create(**validated_data)


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']

    def create(self, validated_data):
        return Department.objects.create(**validated_data)


class MealCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MealCategory
        fields = ['id', 'name', 'department']

    def create(self, validated_data):
        return MealCategory.objects.create(**validated_data)


class MealSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meal
        fields = ['id', 'name', 'category',
                  'price', 'description']

    def create(self, validated_data):
        return Meal.objects.create(**validated_data)


class MealsToOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model= MealsToOrder
        fields = ['id', 'order']

    def create(self, validated_data):
        return MealsToOrder.objects.create(**validated_data)


class MealOrderSerializer(serializers.ModelSerializer):

    meal = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = MealOrder
        fields = ['id', 'order', 'meal', 'count']

    def create(self, validated_data):
        return MealOrder.objects.create(**validated_data)


class OrderSerializer(serializers.ModelSerializer):

    meals = MealOrderSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'isitopen', 'waiter','date', 'table', 'meals']

    def create(self, validated_data):
        return Order.objects.create(**validated_data)


class CheckOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckOrder
        fields = ['id', 'order', 'date', 'servicefree']

    def create(self, validated_data):
        return CheckOrder.objects.create(**validated_data)


class CheckedMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckedMeal
        fields = ['id', 'mealorder', 'check_fk', 'meal']

    def create(self, validated_data):
        return CheckedMeal.objects.create(**validated_data)
