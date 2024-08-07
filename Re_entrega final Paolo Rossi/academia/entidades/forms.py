from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class ComprasForm(forms.Form):
    nombre= forms.CharField (max_length=50, required=True)
    stock= forms.IntegerField(required=True)
    size= forms.IntegerField(required=True)
    precio= forms.IntegerField(required=True)

class ProfesoresForm(forms.Form):
    nombre= forms.CharField (max_length=50, required=True)
    edad=forms.IntegerField(required=True)
    horarios=forms.IntegerField(required=True)
    profesion=forms.CharField(max_length=50, required=True)

class AlumnoForm(forms.Form):
    nombre= forms.CharField(max_length=50,required=True)
    edad=forms.IntegerField(required=True)
    email=forms.EmailField(required=True)
    direccion= forms.CharField(max_length=50,required=True)

class ProveedorForm(forms.Form):
    nombre= forms.CharField(max_length=50,required=True)    
    producto= forms.CharField(max_length=50,required=True)
    email=forms.EmailField(required=True)


class RegistroForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields  # Incluye los campos necesarios

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])  # Usa 'password1' para UserCreationForm
        if commit:
            user.save()
        return user
    

class UserEditForm(UserChangeForm):
    email= forms.EmailField(required=True)
    first_name= forms.CharField(label="Nombre",max_length=50, required=True)
    last_name= forms.CharField(label="Apellido",max_length=50, required=True)

    class Meta:
        model= User
        fields=["email", "first_name", "last_name"]



class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)