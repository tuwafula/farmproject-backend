from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers
from .models import Tender, Input, Investment
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema

User=get_user_model()


# Create your views here.
class HelloServicesView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={"message":"Hello Services"}, status=status.HTTP_200_OK)


class TenderCreateListView(generics.GenericAPIView):
    serializer_class=serializers.TenderViewSerializer
    queryset=Tender.objects.all()
    permission_classes=[IsAuthenticated]

    @swagger_auto_schema(operation_summary="list all tenders")
    def get(self, request):

        tenders = Tender.objects.all()

        serializer=self.serializer_class(instance=tenders, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
 
    @swagger_auto_schema(operation_summary="create a new tender")   
    def post (self, request):
        data=request.data

        serializer=self.serializer_class(data=data)

        user=request.user

        if serializer.is_valid():
            serializer.save(tender_holder=user)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TenderDetailView(generics.GenericAPIView):
    serializer_class=serializers.TenderDetailViewSerializer
    #permission_classes=[IsAuthenticated]

    @swagger_auto_schema(operation_summary="Retrieve a tender by id")
    def get(self, request, tender_id):
        
        tender=get_object_or_404(Tender, pk=tender_id)

        serializer=self.serializer_class(instance=tender)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Update a tender by id")
    def put(self, request, tender_id):
        data=request.data 

        tender=get_object_or_404(Tender, pk=tender_id)

        serializer=self.serializer_class(data=data, instance=tender)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @swagger_auto_schema(operation_summary="Delete a tender")
    def delete(self, request, tender_id):
        tender=get_object_or_404(Tender, pk=tender_id)

        tender.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class UserTendersView(generics.GenericAPIView):
    serializer_class=serializers.TenderDetailViewSerializer

    @swagger_auto_schema(operation_summary="Get all tenders for a user")
    def get(self, request, user_id): 
        user=User.objects.get(pk=user_id)

        tenders=Tender.objects.all().filter(tender_holder=user)

        serializer=self.serializer_class(instance=tenders, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserTenderDetail(generics.GenericAPIView):
    serializer_class=serializers.TenderDetailViewSerializer

    @swagger_auto_schema(operation_summary="Get a user's specific tender")
    def get(self, request, user_id, tender_id):
        user=User.objects.get(pk=user_id)

        tenders=Tender.objects.all().filter(tender_holder=user).get(pk=tender_id)

        serializer=self.serializer_class(instance=tenders)

        return Response(data=serializer.data, status=status.HTTP_200_OK)



class InputCreateListView(generics.GenericAPIView):
    serializer_class=serializers.InputViewSerializer
    queryset=Input.objects.all()
    permission_classes=[IsAuthenticated]

    @swagger_auto_schema(operation_summary="List all inputs")
    def get(self, request):

        inputs = Input.objects.all()

        serializer=self.serializer_class(instance=inputs, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Create a new input")
    def post (self, request):
        data=request.data

        serializer=self.serializer_class(data=data)

        user=request.user

        if serializer.is_valid():
            serializer.save(input_holder=user)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InputDetailView(generics.GenericAPIView):
    serializer_class=serializers.InputDetailViewSerializer
    #permission_classes=[IsAuthenticated]

    @swagger_auto_schema(operation_summary="Retrieve an input by id")
    def get(self, request, input_id):
        
        input=get_object_or_404(Input, pk=input_id)

        serializer=self.serializer_class(instance=input)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Update an input by id")
    def put(self, request, input_id):
        data=request.data 

        input=get_object_or_404(Input, pk=input_id)

        serializer=self.serializer_class(data=data, instance=input)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @swagger_auto_schema(operation_summary="Delete an input")
    def delete(self, request, input_id):
        input=get_object_or_404(Input, pk=input_id)

        input.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class UserInputView(generics.GenericAPIView):
    serializer_class=serializers.InputDetailViewSerializer

    @swagger_auto_schema(operation_summary="Get all inputs for a user")
    def get(self, request, user_id): 
        user=User.objects.get(pk=user_id)

        inputs=Input.objects.all().filter(input_holder=user)

        serializer=self.serializer_class(instance=inputs, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserInputDetail(generics.GenericAPIView):
    serializer_class=serializers.InputDetailViewSerializer

    @swagger_auto_schema(operation_summary="Get a user's specific input")
    def get(self, request, user_id, input_id):
        user=User.objects.get(pk=user_id)

        inputs=Input.objects.all().filter(input_holder=user).get(pk=input_id)

        serializer=self.serializer_class(instance=inputs)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class InvestmentCreateListView(generics.GenericAPIView):
    serializer_class=serializers.InvestViewSerializer
    queryset=Investment.objects.all()
    permission_classes=[IsAuthenticated]

    @swagger_auto_schema(operation_summary="List all investments")
    def get(self, request):

        investments = Investment.objects.all()

        serializer=self.serializer_class(instance=investments, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Create a new investment")
    def post (self, request):
        data=request.data

        serializer=self.serializer_class(data=data)

        user=request.user

        if serializer.is_valid():
            serializer.save(investor_holder=user)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InvestmentDetailView(generics.GenericAPIView):
    serializer_class=serializers.InvestDetailViewSerializer
    #permission_classes=[IsAuthenticated]

    @swagger_auto_schema(operation_summary="Retrieve an investment by id")
    def get(self, request, investor_id):
        
        investment=get_object_or_404(Investment, pk=investor_id)

        serializer=self.serializer_class(instance=investment)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Update an investmnent by id")
    def put(self, request, investor_id):
        data=request.data 

        investment=get_object_or_404(Investment, pk=investor_id)

        serializer=self.serializer_class(data=data, instance=investment)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @swagger_auto_schema(operation_summary="Delete an investment")
    def delete(self, request, investor_id):
        investment=get_object_or_404(Investment, pk=investor_id)

        investment.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class UserInvestmentView(generics.GenericAPIView):
    serializer_class=serializers.InvestDetailViewSerializer

    @swagger_auto_schema(operation_summary="Get all investments for a user")
    def get(self, request, user_id): 
        user=User.objects.get(pk=user_id)

        investments=Investment.objects.all().filter(investor_holder=user)

        serializer=self.serializer_class(instance=investments, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserInvestmentDetail(generics.GenericAPIView):
    serializer_class=serializers.InvestDetailViewSerializer

    @swagger_auto_schema(operation_summary="Get a user's specific investment")
    def get(self, request, user_id, investor_id):
        user=User.objects.get(pk=user_id)

        investments=Investment.objects.all().filter(investor_holder=user).get(pk=investor_id)

        serializer=self.serializer_class(instance=investments)

        return Response(data=serializer.data, status=status.HTTP_200_OK)



