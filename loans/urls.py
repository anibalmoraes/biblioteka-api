from django.urls import path
from .views import LoansView, LoansDetailView, LoansHistoricView


urlpatterns = [
    path("loans/<uuid:copy_id>/", LoansView.as_view()),
    path("loans/admin/<uuid:loan_id>/", LoansDetailView.as_view()),
    path("loans/<uuid:user_id>/", LoansHistoricView.as_view()),
]
