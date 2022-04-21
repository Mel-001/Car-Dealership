
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import CharField, EmailField, TextInput, EmailInput

class UserRegistrationForm(UserCreationForm):
    first_name = CharField(max_length=50, widget=TextInput(attrs={'class':'new-user-firstname'}))
    last_name = CharField(max_length=50, widget=TextInput(attrs={'class':'new-user-lastname'}))
    email = EmailField(widget=EmailInput(attrs={'class':'new-user-email'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs={'class' : 'new-user-username'}
        self.fields['password1'].widget.attrs={'class' : 'new-user-password'}
        self.fields['password2'].widget.attrs={'class': 'new-user-confirm-password'}
