from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['user_id','first_name','last_name','phone','email','role','is_active','created_at','updated_at']
        read_only_fields = ['user_id','created_at','updated_at']