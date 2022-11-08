from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HelloAuthView.as_view(), name='hello_auth'),
    path('signup/farmer/', views.FarmerCreateView.as_view(), name='sign_up'),
    path('signup/tender/', views.TenderCreateView.as_view(), name='sign_up'),
    path('signup/input/', views.InputCreateView.as_view(), name='sign_up'),
    path('signup/investor/', views.InvestorCreateView.as_view(), name='sign_up'),
    #path('signout/', views.UserLogoutView.as_view(), name='sign_out'),
    #path('logout/', views.LogoutView.as_view(), name='auth_logout'),
    path('logout_all/', views.LogoutAllView.as_view(), name='auth_logout_all'),
    path('delete-user/', views.DeleteAccount.as_view(), name='delete_user'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
