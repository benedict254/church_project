from django.forms import ModelForm
from .models import Login,Prayer
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(ModelForm):

    class Meta:
        model = Login
        fields = ['username','email', 'password',]
        
def clean_data(self, *args, **kwargs):
        
    password = self.cleaned_data.get("password")
    if "$" not in password:
        raise forms.ValidationError("This is not a valid password!Must have '$")
    return password

class PrayerForm(ModelForm):

    class Meta:
        model = Prayer
        fields = ['name','email', 'subject','message',]

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']