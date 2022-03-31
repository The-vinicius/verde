from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, UserProfile

class CustomUserCreationForm(UserCreationForm):
    
    username = forms.CharField(label='username', min_length=5, max_length=150)  
    email = forms.EmailField(label='email')  
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomClearableFileInput(forms.FileInput):
    template_name = 'widgets/customclearablefileinput.html'


class CustomTextArea(forms.TextInput):
    template_name = 'widgets/customtextarea.html'


class EditProfileForm(forms.ModelForm):
    image = forms.ImageField(label='Profile Photo',required=False, widget=CustomClearableFileInput)
    bio = forms.CharField(widget=CustomTextArea(attrs={'class':'form-control'}),  max_length=260, required=False)
    wallet = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Endereço bitcoin'}), required=False)
    class Meta:
        model = UserProfile
        fields = ('image', 'bio', 'gender', 'wallet')
        