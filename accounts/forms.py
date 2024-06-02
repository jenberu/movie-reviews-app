from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserCreateForm(UserCreationForm):
    profile = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'custom-input'}))

    class Meta:
        model = User  #make This form is associated with the User model.
        fields = ['username', 'password1', 'password2'] #Specifies the fields from the User model to include 
                                                         # in the form, in this case, username, password1, and password2.

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class': 'custom-input'})

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        if commit:
            user.save()
            profile = UserProfile(user=user)
            if self.cleaned_data['profile']:
                profile.image = self.cleaned_data['profile']
            profile.save()
        return user



class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['image']
