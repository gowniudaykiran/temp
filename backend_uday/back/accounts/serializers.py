from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import User

class CustomRegisterSerializer(RegisterSerializer):

    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    name = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()

        return {
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'name': self.validated_data.get('name', ''),
            'phone_number': self.validated_data.get('phone_number', ''),
        }

class CustomUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email','name','phone_number')
        read_only_fields = ('email',)