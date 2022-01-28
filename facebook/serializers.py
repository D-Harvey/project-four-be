from rest_framework import serializers
from .models import FacebookAccountNumber

class FacebookAccountNumberSerializer(serializers.ModelSerializer):
    '''Model for serializing the Facebook account numbers'''

    class Meta:
        model = FacebookAccountNumber
        fields = '__all__'
