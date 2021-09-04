from rest_framework import serializers
from django.contrib.auth import get_user_model
User=get_user_model()
from django.contrib.auth import authenticate

class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude=["password","last_login","is_active","is_admin","staff",
                    "is_superuser","owner","groups","user_permissions"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name","last_name", "email" ,"institution","faculty",
                     "department","set","password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data["email"],validated_data["institution"],
                                        validated_data["faculty"],validated_data["department"],
                                        validated_data["set"],validated_data["first_name"],
                                        validated_data["last_name"],validated_data["password"])
        user.save()
        return user         


class LoginSerializer(serializers.Serializer):
    email= serializers.EmailField()
    password= serializers.CharField()
    
    def validate(self,data):
        user= authenticate(**data)
        
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Credentials")  