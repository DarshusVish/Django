from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField(max_length=13)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

    @staticmethod
    def get_cutomer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False