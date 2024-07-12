from django import forms
from django.contrib.auth import authenticate
#from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User



from django.contrib.auth.forms import UserCreationForm
from .models import Clientes, CondicionIva

class ClienteCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    telefono = forms.CharField(max_length=15, required=True)
    direccion = forms.CharField(max_length=255, required=True)
    id_condicion_iva = forms.ModelChoiceField(queryset=CondicionIva.objects.all(), required=False)
    foto_cliente = forms.ImageField(required=False)

    class Meta:
        model = Clientes
        fields = ('username', 'email', 'first_name', 'last_name', 'telefono', 'direccion', 'id_condicion_iva', 'foto_cliente', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.telefono = self.cleaned_data['telefono']
        user.direccion = self.cleaned_data['direccion']
        user.id_condicion_iva = self.cleaned_data['id_condicion_iva']
        
        if 'foto_cliente' in self.cleaned_data and self.cleaned_data['foto_cliente']:
            user.foto_cliente = self.cleaned_data['foto_cliente']
        else:
            user.foto_cliente = 'static/img/imagenes_clientes/default.jpg' 
        
        if commit:
            user.save()
        return user




# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Repite la contraseña', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ('username', 'email')

#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password'] != cd['password2']:
#             raise forms.ValidationError('Las contraseñas no coinciden.')
#         return cd['password2']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data['password'])
#         if commit:
#             user.save()
#         return user

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de Usuario'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Nombre de usuario o contraseña incorrectos.")
        return self.cleaned_data