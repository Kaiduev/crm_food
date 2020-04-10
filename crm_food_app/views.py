from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from . import serializers
from .models import *
from rest_framework.response import Response


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
            return Response({"success": "Table '{}' created successfully".format(saved_data.name)})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TableDetail(APIView):

    serializer_class = serializers.TableSerializer

    def get(self, request, pk):
        table = Table.objects.get(pk=pk)
        serializer = serializers.TableSerializer(table)
        return Response(serializer.data)

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
        return Response({"tables": serializer.data})

    def post(self,request):
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
        return Response({"success":"Role '{}' was deleted".format(Resp.name)},
                        status=status.HTTP_400_BAD_REQUEST)
