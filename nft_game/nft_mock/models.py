from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class QRCode(models.Model):
    code = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code


class UserNFT(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qr_code = models.ForeignKey(QRCode, on_delete=models.CASCADE)
    minted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} owns NFT from {self.qr_code}"
