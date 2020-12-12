from django.forms import widgets
from django.utils.translation import gettext_lazy,gettext as _
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserModel, UsernameField,SetPasswordForm
from django.contrib.auth.models import User
from .views import UserCreationForm
from .models import *
class SignUpForm(UserCreationForm):
    password2=forms.CharField(label="Confirm password again",widget=forms.PasswordInput(attrs={"class":'form-control'}),)
    password1 =forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    #To change the lable here
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'Email',"first_name":'firstname','last_name':'lastname'}
        #passwords are not part of model here so we can not change here
        #password is the part of the Usercreationform here
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
                'first_name':forms.TextInput(attrs={'class':'form-control'}),
                'last_name':forms.TextInput(attrs={'class':'form-control'}),
                'password':forms.PasswordInput(attrs={'class':'form-control'}),
                'email':forms.EmailInput(attrs={'class':'form-control'})}
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs=
                {'autocomplete':'current-password','class':'form-control'}))
class PasswordChangeForm(SetPasswordForm):
    class Meta:
        model = User
        fields=['New password','New password confirmation']
        labels={'New password':"change password","New password confirmation":"password confirmation"}
        widgets={"New password":forms.TextInput(attrs={'class':'form-control'}),
                 "New password confirmation":forms.TextInput(attrs={'class':'form-control'})}
        
