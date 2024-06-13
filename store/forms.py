from django import forms

# Create your forms here
class LoginForm(forms.ModelForm):
      
      user = forms.CharField()
      password = forms.PasswordInput()