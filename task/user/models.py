from django.db import models

class Money(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.code

class Convertion(models.Model):
    currency = models.ForeignKey(Money, on_delete=models.CASCADE)
    to = models.ForeignKey(Money,related_name='%(class)s_to', on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return "%s to %s %s" %(self.currency, self.to, self.rate)