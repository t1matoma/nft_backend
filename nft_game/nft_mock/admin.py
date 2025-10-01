from django.contrib import admin
from .models import User, QRCode, UserNFT
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')


@admin.register(QRCode)
class QRCodeAdmin(admin.ModelAdmin):
    list_display = ('code',)


@admin.register(UserNFT)
class UserNFTAdmin(admin.ModelAdmin):
    list_display = ('user', 'qr_code', 'minted_at')

