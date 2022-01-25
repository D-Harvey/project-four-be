from django.db import models

class Client(models.Model):
    client_name = models.CharField(max_length=300, unique=True)
    client_comm = models.DecimalField(max_digits=5, decimal_places=2)
    client_logo = models.CharField(max_length=300, unique=True)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.client_name}'

class Adset(models.Model):
    adset_name = models.CharField(max_length=300, unique=True)
    created_at = models.DateField(auto_now=True)
    client = models.ForeignKey(
        Client,
        # related name needs to match the key in the serializer
        related_name='adset_name',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.client} - {self.adset_name}'


class MediaCost(models.Model):
    media_cost = models.PositiveIntegerField()
    created_at = models.DateField(auto_now=True)
    adset_name = models.ForeignKey(
        Adset,
        related_name='media_cost',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Cost {self.media_cost} on Adset {self.adset_name}'

class DailyImpression(models.Model):
    daily_impressions = models.PositiveIntegerField()
    created_at = models.DateField(auto_now=True)
    adset_name = models.ForeignKey(
        Adset,
        related_name='daily_impressions',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Imps {self.daily_impressions} on Adset {self.adset_name}'

class DailyClick(models.Model):
    daily_clicks = models.PositiveIntegerField()
    created_at = models.DateField(auto_now=True)
    adset_name = models.ForeignKey(
        Adset,
        related_name='daily_clicks',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Clicks {self.daily_clicks} on Adset {self.adset_name}'

class DailyConversion(models.Model):
    daily_conversions = models.PositiveIntegerField()
    created_at = models.DateField(auto_now=True)
    adset_name = models.ForeignKey(
        Adset,
        related_name='daily_conversions',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Convs {self.daily_conversions} on Adset {self.adset_name}'

class DailyRevenue(models.Model):
    daily_revenue = models.PositiveIntegerField()
    created_at = models.DateField(auto_now=True)
    adset_name = models.ForeignKey(
        Adset,
        related_name='daily_revenue',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Revenue {self.daily_revenue} on Adset {self.adset_name}'
