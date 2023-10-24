from django import forms


class UserForm(forms.Form):
    age = forms.IntegerField(required=False, max_value=150, min_value=18)
    email = forms.CharField(required=True)

