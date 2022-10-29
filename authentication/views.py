from calendar import c
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import User
from . import serializers


# Create your views here.
class HelloAuthView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={"message":"Hello Auth"}, status=status.HTTP_200_OK)


class FarmerCreateView(generics.GenericAPIView):

    serializer_class=serializers.FarmerUserCreationSerializer

    @swagger_auto_schema(operation_summary="Create a farmer's user account")
    def post(self, request):
        data=request.data 

        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message' : 'Farmer registered successfully',
            }
            status_code =  status.HTTP_200_OK
            return Response(response, status_code)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TenderCreateView(generics.GenericAPIView):

    serializer_class=serializers.TenderUserCreationSerializer

    @swagger_auto_schema(operation_summary="Create a tender's user account")
    def post(self, request):
        data=request.data 

        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message' : 'Tender user registered successfully',
            }
            status_code =  status.HTTP_200_OK
            return Response(response, status_code)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InputCreateView(generics.GenericAPIView):

    serializer_class=serializers.InputUserCreationSerializer

    @swagger_auto_schema(operation_summary="Create a input's user account")
    def post(self, request):
        data=request.data 

        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message' : 'Input user registered successfully',
            }
            status_code =  status.HTTP_200_OK
            return Response(response, status_code)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InvestorCreateView(generics.GenericAPIView):

    serializer_class=serializers.InvestorUserCreationSerializer

    @swagger_auto_schema(operation_summary="Create a investor's user account")
    def post(self, request):
        data=request.data 

        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message' : 'Investor registered successfully',
            }
            status_code =  status.HTTP_200_OK
            return Response(response, status_code)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    