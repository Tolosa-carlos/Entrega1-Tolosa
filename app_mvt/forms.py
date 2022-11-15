from django import forms

class MenuForm(forms.Form):

    nombre = forms.CharField()
    precio = forms.IntegerField()


class EmpleadosForm(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()

