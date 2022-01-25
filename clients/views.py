from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)


# from rest_framework.permissions import IsAuthenticated

from .models import Client, Adset
from .serializers import ClientSerializer, AdsetDetailSerializer

class ClientListView(ListCreateAPIView):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    # permission_classes = (IsAuthenticated, )

class ClientDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    # permission_classes = (IsAuthenticated, )

class CampaignListView(ListCreateAPIView):

    queryset = Adset.objects.all()
    serializer_class = AdsetDetailSerializer
    # permission_classes = (IsAuthenticated, )
