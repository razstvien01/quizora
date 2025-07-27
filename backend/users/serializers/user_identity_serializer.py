from rest_framework import serializers
from users.models import UserIdentity

class UserIdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserIdentity
        fields = ['provider', 'auth_id']