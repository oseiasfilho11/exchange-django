from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Wallet)
admin.site.register(Coin)
admin.site.register(Active)