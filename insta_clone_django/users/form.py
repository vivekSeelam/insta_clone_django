from django import forms
from models import User


class UserSignUpForm(forms.ModelForm):

    name = forms.CharField(required=True)

    email = forms.EmailField(required=True)

    password = forms.PasswordInput()

    class Meta:
        model = User
        exclude = ('created_on', 'updated_on', 'is_active')

