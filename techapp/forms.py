from django import forms

class SignupForm(forms.Form):
    first_name = forms.CharField(label="Name", max_length=200)
    email = forms.EmailField(label="Email", max_length=200)
    password = forms.CharField(widget=forms.PasswordInput, label="Password", max_length=200)



from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=254, required=True, label="Email")
    password = forms.CharField(widget=forms.PasswordInput, required=True, label="Password")
    
    
from .models import ContactDetail
    
class ContactForm(forms.ModelForm):
    class Meta:
        model=ContactDetail 
        fields=['name','email','subject','message']
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        #     'message': forms.Textarea(attrs={'class': 'form-control'}),
        # }


# # forms.py
# from django import forms
# from .models import UserProfile
# from django.contrib.auth.models import User

# class UserUpdateForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email']

# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['address', 'phone_number']
