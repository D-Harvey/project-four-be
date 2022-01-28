from rest_framework.generics import ListCreateAPIView

from .serializers import FacebookAccountNumberSerializer

from .models import FacebookAccountNumber

class FacebookAccountNumberView(ListCreateAPIView):
    '''View for saving Facebook account numbers'''
    queryset = FacebookAccountNumber.objects.all()
    serializer_class = FacebookAccountNumberSerializer
