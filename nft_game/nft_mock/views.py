from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, QRCode, UserNFT
from .serializers import UserSerializer, QRCodeSerializer, UserNFTSerializer
import uuid

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class QRCodeViewSet(viewsets.ModelViewSet):
    queryset = QRCode.objects.all()
    serializer_class = QRCodeSerializer

    @action(detail=False, methods=['post'])
    def generate(self, request):
        code = str(uuid.uuid4())  # генерируем уникальный код
        qr = QRCode.objects.create(code=code)
        return Response(QRCodeSerializer(qr).data, status=status.HTTP_201_CREATED)


class UserNFTViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def scan(self, request):
        user_id = request.data.get('user_id')
        qr_code = request.data.get('qr_code')

        try:
            user = User.objects.get(id=user_id)
            qr = QRCode.objects.get(code=qr_code)
        except (User.DoesNotExist, QRCode.DoesNotExist):
            return Response({'error': 'User or QR code not found'}, status=status.HTTP_404_NOT_FOUND)

        # проверка, что NFT уже не выдан
        if UserNFT.objects.filter(user=user, qr_code=qr).exists():
            return Response({'detail': 'NFT already claimed'}, status=status.HTTP_400_BAD_REQUEST)

        nft = UserNFT.objects.create(user=user, qr_code=qr)
        return Response(UserNFTSerializer(nft).data, status=status.HTTP_201_CREATED)
