from django.db import models

# Create your models here.
class FacebookAccountNumber(models.Model):
    facebook_account_id = models.CharField(max_length=300, unique=True)
    facebook_account_name = models.CharField(max_length=300)

    def __str__(self):
        return f'Client {self.facebook_account_name}'