from typing import Any
from django.contrib.auth.forms import UserCreationForm
class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super (UserCreateForm,self).__init__(*args,**kwargs)
        for fieldname in['username', 'password1','password2']:
            #set help_text of the form's fields to None to remove them
            self.fields[fieldname].help_text=None
            #set for each form field a class attribute to use a Bootstrap class.

            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})