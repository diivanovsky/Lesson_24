from django import forms
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class UserEditForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['email', 'first_name', 'last_name']
