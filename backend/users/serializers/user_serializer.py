from rest_framework import serializers
from users.models import User
from users.serializers import UserIdentitySerializer

class UserSerializer(serializers.ModelSerializer):
    identity = serializers.SerializerMethodField()
    
    def get_identity (self, obj):
        identity = obj.identity
        
        if identity:
            return UserIdentitySerializer(identity).data
        return None
    
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'is_superuser',
            'role',
            'identity'
        ]