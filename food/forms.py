from django import forms
from .models import GetInTouch, GetEmail
class CustomerForm(forms.ModelForm):
    class Meta:
        model = GetInTouch
        fields = "__all__"

class CustomerMail(forms.ModelForm):
    class Meta:
        model = GetEmail
        fields = "__all__"