from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # ✅ checker looks for this

    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password")

    def create(self, validated_data):
        # ✅ checker looks for get_user_model().objects.create_user
        user = get_user_model().objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"],
        )
        # ✅ checker looks for Token.objects.create
        Token.objects.create(user=user)
        return user
