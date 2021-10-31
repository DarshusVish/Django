from django.db import models
from django.contrib.auth.models import User

class NewCustomer(User):
    role = models.CharField(max_length=20, default='admin',blank=False)