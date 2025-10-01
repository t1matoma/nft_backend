# app/serializers.py
from rest_framework import serializers
from .models import User, QRCode, UserNFT

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class QRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRCode
        fields = ['id', 'code', 'created_at']


class UserNFTSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNFT
        fields = ['id', 'user', 'qr_code', 'minted_at']
