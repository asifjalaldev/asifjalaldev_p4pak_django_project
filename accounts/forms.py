from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

#new code to create userProfile
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        #self.error_class = BsErrorList

    def clean_email(self):
        email = self.cleaned_data["email"]

        try:
            User._default_manager.get(email__iexact=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(
            'A user with that email already exists',
            code='duplicate_email',
        )

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]

        # Create user_profile here
        
        if commit:
            user.save()

        return user

