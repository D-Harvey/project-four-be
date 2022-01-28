from django.urls import path
from .views import FacebookAccountNumberView

urlpatterns = [
    path('', FacebookAccountNumberView.as_view()),
]
