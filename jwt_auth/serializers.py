from rest_framework import serializers
from django.contrib.auth import get_user_model
# import django.contrib.auth.password_validation as validation
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, attrs):
        password = attrs.pop('password')
        password_confirmation = attrs.pop('password_confirmation')

        # makes sure pass and pass conf are the same
        if password != password_confirmation:
            raise ValidationError({'detail': 'Password and Confirmation do not match'})

        # makes sure password is strong enough, long enough etc
        # try:
        #     validation.validate_password(password=password)
        # except ValidationError as err:
        #     raise ValidationError({'password': err})

        # putting password back as hashed
        attrs['password'] = make_password(password)

        return attrs

    class Meta:
        model = User
        fields = '__all__'
