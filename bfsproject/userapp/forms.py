from django import forms

from .models import *


class DateInput(forms.DateInput):
    input_type = "date"

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"
        labels = {"username": "Provide Username","gender": "Select Gender", "location": "Provide Location","panno":"Pan Number","conatctno":"Contact Number","aadharno":"Aadhar Number"}
        widgets = {"password": forms.PasswordInput(),"dateofbirth":DateInput()}

class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"
        widgets = {"password":forms.PasswordInput()}

class TransferForm(forms.ModelForm):
    class Meta:
        model=Transfer
        fields="__all__"
        exclude={"transaction_id","transfertime"}

class BillPaymentForm(forms.ModelForm):
    class Meta:
        model=BillPayment
        fields="__all__"
        exclude={"payment_time"}
