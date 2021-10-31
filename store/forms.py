from django.contrib.auth.forms import UserCreationForm
from store.models.NewCustomer import NewCustomer

class OurUserForm(UserCreationForm):
    class Meta:
        model = NewCustomer
        fields = ['username','first_name','last_name','email','password1','password2','role']
