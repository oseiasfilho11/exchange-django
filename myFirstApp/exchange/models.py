from django.db import models

class User(models.Model):
    userName = models.CharField(max_length=45)
    passWord = models.CharField(max_length=30)
    userEmail = models.EmailField(max_length=30)

    def __str__(self):
        return f'User name = {self.userName}, User Email = {self.userEmail}'

    def getId(self):
        return self.id

class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    totalBalance = models.FloatField()     

    def __str__(self):
        return f"User = {self.user.userName}, Total Balance = {self.totalBalance}" 

class Coin(models.Model):
    coinName = models.CharField(max_length=10)
    value = models.FloatField()

    def __str__(self):
        return f"Coin Name = {self.coinName}, value = {self.value}"

class Active(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f"Wallet = {self.wallet.id}, Coin = {self.coin}, Quantity = {self.quantity}"

