from rest_framework import serializers
from .models import (
Client, Adset, MediaCost,
DailyImpression, DailyClick,
DailyConversion, DailyRevenue
)

class MediaCostSerializer(serializers.ModelSerializer):
    '''Serializer for outgoing media cost reponse'''

    class Meta:
        model = MediaCost
        fields = '__all__'

class DailyImpressionsSerializer(serializers.ModelSerializer):
    '''Serializer for outgoing daily impressions reponse'''

    class Meta:
        model = DailyImpression
        fields = '__all__'

class DailyClicksSerializer(serializers.ModelSerializer):
    '''Serializer for outgoing daily clicks reponse'''

    class Meta:
        model = DailyClick
        fields = '__all__'

class DailyConversionsSerializer(serializers.ModelSerializer):
    '''Serializer for outgoing daily conversions reponse'''

    class Meta:
        model = DailyConversion
        fields = '__all__'

class DailyRevenueSerializer(serializers.ModelSerializer):
    '''Serializer for outgoing daily revenue reponse'''

    class Meta:
        model = DailyRevenue
        fields = '__all__'

class AdsetDetailSerializer(serializers.ModelSerializer):
    # keys below need to match the related name in the model
    media_cost = MediaCostSerializer(many=True)
    daily_impressions = DailyImpressionsSerializer(many=True)
    daily_clicks = DailyClicksSerializer(many=True)
    daily_conversions = DailyConversionsSerializer(many=True)
    daily_revenue = DailyRevenueSerializer(many=True)

    class Meta:
        model = Adset
        fields = '__all__'

class ClientDetailSerializer(serializers.ModelSerializer):
    '''Serializer for outgoing client detailed response'''
    adset_name = AdsetDetailSerializer(many=True)

    class Meta:
        model = Client
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    '''Serializer for outgoing client response'''

    class Meta:
        model = Client
        fields = '__all__'