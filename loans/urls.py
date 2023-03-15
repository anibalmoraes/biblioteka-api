from django.urls import path
from .views import LoansView, LoansDetailView, LoansHistoricView


urlpatterns = [
    path("loans/copies/<uuid:copy_id>/", LoansView.as_view()),
    path("loans/admin/<uuid:loan_id>/", LoansDetailView.as_view()),
    path("loans/students/<uuid:user_id>/", LoansHistoricView.as_view()),
]
