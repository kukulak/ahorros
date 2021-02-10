from django import forms

from django.forms import ModelForm, CharField, TextInput
from django.core.exceptions import ValidationError

from django.core.validators import RegexValidator

from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

from django.forms import modelform_factory

from .models import Ahorro, Sistema, Profile, Plazo

class SistemaSelect(forms.Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if value:
            if value == id:
                option['attrs']['selected']
                print('value:', value)
        return option

class CantidadForm(ModelForm):
    class Meta:
        model = Ahorro
        fields = ['cantidad', 'sistema']
        widgets = {'sistema': SistemaSelect}

# class DeleteCantidadForm(ModelForm):
#     class Meta:
#         model = Sistema
#         fields = ['cantidad', 'sistema']
#         # widgets = {'sistema': SistemaSelect}
        

# LOGINFORM P
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         fields = UserCreationForm.Meta.fields + ("email",)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
 
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')



class UserSelected(forms.Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if value:
            print("atributo")
            if value == id:
                option['attrs']['selected']
                print('value:', value)
        return option


# class CreateNewSystem(forms.ModelForm):
#     class Meta:
#         model = Sistema
#         fields = ('nombre', 'user',)
  


# def adjust_username_field(form):
#     help_text = ("Usa únicamente números")
#     form.fields['username'].error_messages['invalid'] = ("Invalid username")
#     form.fields['username'].help_text = help_text
#     form.fields['username'].validators += [RegexValidator('\D')]

# def adjust_username_field(form):
#     validate_number = RegexValidator(regex="\D", message="Usa únicamente números")
#     validate_number(form)
#     return form

class CreateNewSystem(forms.ModelForm):
    class Meta:
        model = Sistema
        fields = ['nombre', 'user', 'frecuencia', 'tiempo', 'meta']
        # fields = '__all__'
    def validate(self):
        super(CreateNewSystem, self).clean()
        meta = self.cleaned_data.get('meta')
        validate_number = RegexValidator(regex="\D")
        print("@@@@@@#####@@@@@@@")
        # if validate_number(meta):
        if len(meta) < 5:
            self._errors['meta'] = self.error_class(['Usa únicamente números'])
        return self.cleaned_data


# class ArchiveSystem(forms.ModelForm):
#     class Meta:
#         model = Sistema
#         fields = ['not_archived',]
#         # fields = '__all__'


ArchiveSystem = modelform_factory(Sistema, fields=("not_archived",))

class CreatePlazoSystem(forms.ModelForm):
    class Meta:
        model = Plazo
        fields = ['frecuencia', 'tiempo', 'meta',]
   

# to SHARE

class EmailShareForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()