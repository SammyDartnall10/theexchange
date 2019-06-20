#make the forms in here and then send them to views.py.

from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from accounts.models import CustomUser

class UserLoginForm(forms.Form):
    """Forms to be used by users to login"""
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class UserRegistrationForm(ModelForm):
    
    password1 = forms.CharField(
                label="Password", 
                widget=forms.PasswordInput)
    password2 = forms.CharField(
                label="Password Confirmation", 
                widget=forms.PasswordInput)
            
    class Meta: 
        model = CustomUser
        fields = ['email', 'username', 'password1', 'password2']
        
            
    def add_error(self, message):
        self._errors[NON_FIELD_ERRORS] = self.error_class([message])
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError('Email must be unique')
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if not password1 or not password2:
            raise ValidationError("Please conf your password")
            
        if password1 != password2:
            raise ValidationError("Passwords do not match")

            
        return password2
        

class MakePaymentForm(forms.Form):
    
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2017, 2036)]
    
    credit_card_number = forms.CharField(label="Credit card number", required=False)
    cvv = forms.CharField(label="Security Code (CVV)", required=False)
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
#--------------------------------------------------------------------------------------------------------------------------------
"""    
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("full_name", "phone_number", "country", "postcode", "town_or_city", "street_address1", "street_address2", "county")

"""