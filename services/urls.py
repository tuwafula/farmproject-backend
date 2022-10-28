from django.urls import path 
from . import views

urlpatterns = [
    path('tender/', views.TenderCreateListView.as_view(), name='tenders'),
    path('tender/<int:tender_id>/', views.TenderDetailView.as_view(), name='tender_detail'),
    path('tender/user/<int:user_id>/tenders/', views.UserTendersView.as_view(), name="user-tenders"),
    path('tender/user/<int:user_id>/tenders/<int:tender_id>/', views.UserTenderDetail.as_view(), name='tender_specific_detail'),
    path('input/', views.InputCreateListView.as_view(), name='inputs'),
    path('input/<int:input_id>/', views.InputDetailView.as_view(), name='input_detail'),
    path('input/user/<int:user_id>/inputs/', views.UserInputView.as_view(), name="user-inputs"),
    path('input/user/<int:user_id>/inputs/<int:input_id>/', views.UserInputDetail.as_view(), name='input_specific_detail'),
    path('invest/', views.InvestmentCreateListView.as_view(), name='invest'),
    path('invest/<int:investor_id>/', views.InvestmentDetailView.as_view(), name='invest_detail'),
    path('invest/user/<int:user_id>/investments/', views.UserInvestmentView.as_view(), name="user-investments"),
    path('invest/user/<int:user_id>/investments/<int:investor_id>/', views.UserInvestmentDetail.as_view(), name='investment_specific_detail'),
]