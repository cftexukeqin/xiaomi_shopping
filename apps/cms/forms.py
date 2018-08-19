from django import forms
from apps.forms import FormMixin
from apps.phone.models import Phone

class AddPhoneForm(forms.ModelForm,FormMixin):
    class Meta:
        model = Phone
        fields = "__all__"
