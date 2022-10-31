from django.urls import path 
from . import views

urlpatterns = [
    path('', views.HelloAuthView.as_view(), name='hello_auth'),
    path('signup/farmer/', views.FarmerCreateView.as_view(), name='sign_up'),
    path('signup/tender/', views.TenderCreateView.as_view(), name='sign_up'),
    path('signup/input/', views.InputCreateView.as_view(), name='sign_up'),
    path('signup/investor/', views.InvestorCreateView.as_view(), name='sign_up'),
    path('signout/', views.UserLogoutView.as_view(), name='sign_out'),
]
