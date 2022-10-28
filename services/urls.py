from django.urls import path 
from . import views

urlpatterns = [
    path('tender/', views.TenderCreateListView.as_view(), name='tenders'),
    path('tender/<int:tender_id>/', views.TenderDetailView.as_view(), name='tender_detail'),
    path('input/', views.InputCreateListView.as_view(), name='inputs'),
    path('input/<int:input_id>/', views.InputDetailView.as_view(), name='input_detail'),
    path('invest/', views.InvestmentCreateListView.as_view(), name='invest'),
    path('invest/<int:investor_id>/', views.InvestmentDetailView.as_view(), name='invest_detail')
]