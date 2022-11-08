from calendar import c
from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import User
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken, BlacklistedToken, OutstandingToken
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

class UserLogoutView(APIView):
    
    @staticmethod
    def delete(request, *args, **kwargs):
        # simply delete the token to force a login
        request.user.Authorization.delete()
        data =  {
            "message" : "You have successfully logged out.",
        }
        return Response(data, status=status.HTTP_200_OK)

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class LogoutAllView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)

        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)


class DeleteAccount(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def delete(self, request, *args, **kwargs):
        user = self.request.user
        user.delete()
        data =  {
            "message" : "User deleted successfully.",
        }
        return Response(data, status=status.HTTP_200_OK)