from django.forms import ModelForm
from .models import UserLogin

class UserForm(ModelForm) :
    class Meta :
        model = UserLogin
        fields = ['username', 'password']

