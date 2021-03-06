from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.views import APIView
from . import serializers
from .models import *
from rest_framework.response import Response
from rest_framework import generics
# from user.models import Role,User
import django_filters.rest_framework


class TableView(APIView):

    serializer_class = serializers.TableSerializer

    def get(self, request):
        tables = Table.objects.all()
        serializer = serializers.TableSerializer(tables, many=True)
        return Response({"tables": serializer.data})

    def post(self,request):
        serializer = serializers.TableSerializer(data=request.data)
        if serializer.is_valid():
            saved_data = serializer.save()
            return Response({"success": "Table '{}' created successfully".format(saved_data.name)},
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TableDetail(APIView):

    serializer_class = serializers.TableSerializer

    def get(self, request, pk):
        table = Table.objects.get(pk=pk)
        serializer = serializers.TableSerializer(table)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        table = Table.objects.get(pk=pk)
        serializer = serializers.TableSerializer(table, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Resp = Table.objects.get(pk=pk)
        table = Table.objects.get(pk = pk)
        table.delete()
        return Response({"success": "Table '{}' was deleted".format(Resp.name)}, status=status.HTTP_204_NO_CONTENT)


class RoleView(APIView):

    serializer_class = serializers.RoleSerializer

    def get(self, request):
        roles = Role.objects.all()
        serializer = serializers.RoleSerializer(roles, many=True)
        return Response({"roles": serializer.data})

    def post(self, request):
        serializer = serializers.RoleSerializer(data=request.data)
        if serializer.is_valid():
            saved_data = serializer.save()
            return Response({"success": "Role '{}' created successfully".format(saved_data.name)})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class RoleDetail(APIView):

    serializer_class = serializers.RoleSerializer

    def get(self,request, pk):
        role = Role.objects.get(pk=pk)
        serializer = serializers.RoleSerializer(role)
        return Response(serializer.data)

    def put(self,request, pk):
        role = Role.objects.get(pk=pk)
        serializer = serializers.RoleSerializer(role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Resp = Role.objects.get(pk=pk)
        role = Role.objects.get(pk=pk)
        role.delete()
        return Response({"success": "Role '{}' was deleted".format(Resp.name)},
                        status=status.HTTP_400_BAD_REQUEST)


class DepartmentView(APIView):

    serializer_class = serializers.DepartmentSerializer

    def get(self,request):
        departments = Department.objects.all()
        serializer = serializers.DepartmentSerializer(departments, many=True)
        return Response({"departments":serializer.data})

    def post(self, request):
        serializer = serializers.DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            saved_data = serializer.save()
            return Response({"success": "Department '{}' created successfully".format(saved_data.name)})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class DepartmentDetail(APIView):

    serializer_class = serializers.DepartmentSerializer

    def get(self, request, pk):
        department = Department.objects.get(pk=pk)
        serializer = serializers.DepartmentSerializer(department)
        return Response(serializer.data)

    def put(self, request, pk):
        department = Department.objects.get(pk=pk)
        serializer = serializers.DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        department = Department.objects.get(pk=pk)
        Resp = Department.objects.get(pk=pk)
        department.delete()
        return Response({"success": "Department '{}' was deleted".format(Resp.name)},
                        status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):

    serializer_class = serializers.UserSerializer

    def get(self, request):
        users = User.objects.all()
        serializer = serializers.UserSerializer(users, many=True)
        return Response({"users": serializer.data})

    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            saved_data = serializer.save()
            return Response({"success":"User '{}' was created successfully".format(saved_data.name)})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):

    serializer_class = serializers.UserSerializer

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = serializers.UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        user = User.objects.get(pk=pk)
        Resp = User.objects.get(pk=pk)
        user.delete()
        return Response({"success": "User '{}' was deleted".format(Resp.name)},
                        status=status.HTTP_400_BAD_REQUEST)


class MealCategoryView(APIView):

    serializer_class = serializers.MealCategorySerializer

    def get(self, request):
        mealcategories = MealCategory.objects.all()
        serializer = serializers.MealCategorySerializer(mealcategories, many=True)
        return Response({"mealcategories": serializer.data})

    def post(self, request):
        serializer = serializers.MealCategorySerializer(data=request.data)
        if serializer.is_valid():
            saved_data = serializer.save()
            return Response({"success": "MealCategory '{}' was created successfully".format(saved_data.name)})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MealCategoryDetail(APIView):

    serializer_class = serializers.MealCategorySerializer

    def get(self, request, pk):
        mealcategory = MealCategory.objects.get(pk=pk)
        serializer = serializers.MealCategorySerializer(mealcategory)
        return Response(serializer.data)

    def put(self, request, pk):
        mealcategory = MealCategory.objects.get(pk=pk)
        serializer = serializers.MealCategorySerializer(mealcategory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = MealCategory.objects.get(pk=pk)
        Resp = MealCategory.objects.get(pk=pk)
        user.delete()
        return Response({"success": "MealCategory '{}' was deleted".format(Resp.name)},
                        status=status.HTTP_400_BAD_REQUEST)


class StatusView(APIView):

    serializer_class = serializers.StatusSerializer

    def get(self, request):
        statuses = Status.objects.all()
        serializer = serializers.StatusSerializer(statuses, many=True)
        return Response({"statuses": serializer.data})

    def post(self, request):
        serializer = serializers.StatusSerializer(data=request.data)
        if serializer.is_valid():
            saved_data = serializer.save()
            return Response({"success": "Status '{}' was created successfully".format(saved_data.name)})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StatusDetail(APIView):

    serializer_class = serializers.StatusSerializer

    def get(self, request, pk):
        status_ = Status.objects.get(pk=pk)
        serializer = serializers.StatusSerializer(status_)
        return Response(serializer.data)

    def put(self, request, pk):
        status_ = Status.objects.get(pk=pk)
        serializer = serializers.StatusSerializer(status_, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        Resp = Status.objects.get(pk=pk)
        status_ = Status.objects.get(pk=pk)
        status_.delete()
        return Response({"success": "Status '{}' was deleted".format(Resp.name)},
                        status=status.HTTP_400_BAD_REQUEST)


class MealView(APIView):

    serializer_class = serializers.MealSerializer

    def get(self, request):
        meals = Meal.objects.all()
        serializer = serializers.MealSerializer(meals, many=True)
        return Response({"meals": serializer.data})

    def post(self,request):
        serializer = serializers.MealSerializer(data=request.data)
        if serializer.is_valid():
            saved_data = serializer.save()
            return Response({"success": "Meal '{}' was created successfully".format(saved_data.name)})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MealDetail(APIView):
    """Meal Detail"""
    serializer_class = serializers.MealSerializer

    def get(self, request,pk):
        meal = Meal.objects.get(pk=pk)
        serializer = serializers.MealSerializer(meal)
        return Response(serializer.data)

    def put(self, request, pk):
        meal = Meal.objects.get(pk=pk)
        serializer = serializers.MealSerializer(meal,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        meal = Meal.objects.get(pk=pk)
        Resp = Meal.objects.get(pk=pk)
        meal.delete()
        return Response({"success": "Meal '{}' was deleted successfully".format(Resp.name)})


class MealsByCategory(generics.ListAPIView):

    queryset = Meal.objects.all()
    serializer_class = serializers.MealSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']


class OrderView(APIView):
    """OrderList"""

    serializer_class = serializers.OrderSerializer

    def get(self, request):
        orders = Order.objects.all()
        serializer = serializers.OrderSerializer(orders, many=True)
        return Response({"orders":serializer.data})

    def post(self, request):
        serializer = serializers.OrderSerializer(data=request.data)
        if serializer.is_valid():
            saved_data = serializer.save()
            return Response({'success': "Order '{}' was created successfully".format(saved_data.table)})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActiveOrders(generics.ListAPIView):

    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['isitopen']


class OrderDetail(APIView):

    serializer = serializers.OrderSerializer

    def get(self, request, pk):
        order = Order.objects.get(pk=pk)
        serializer = serializers.OrderSerializer(order)
        return Response(serializer.data)

    def delete(self, request, pk):
        order = Order.objects.get(pk=pk)
        Resp = Order.objects.get(pk=pk)
        order.delete()
        return Response({"success":"Order '{}' was deleted successfully".format(Resp.table.name)})


class CheckView(APIView):

    serializer_class = serializers.CheckOrderSerializer

    def get(self,request):
        checkmeals = CheckOrder.objects.all()
        serializer = serializers.CheckOrderSerializer(checkmeals, many=True)
        return Response({"checks": serializer.data})


class CheckDetail(APIView):

    serializer_class = serializers.CheckOrderSerializer

    def get(self,requests, pk):
        checkmeal = CheckOrder.objects.get(pk=pk)
        serializer = serializers.CheckOrderSerializer(checkmeal)
        return Response(serializer.data)