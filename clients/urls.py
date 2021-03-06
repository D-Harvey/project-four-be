from django.urls import path
from .views import ClientListView, ClientDetailView, CampaignListView

urlpatterns = [
    path('', ClientListView.as_view()),
    path('<int:pk>/', ClientDetailView.as_view()),
    path('<int:pk>/plans/<int:asPk>', CampaignListView.as_view())
]
