from django import forms

class MenuForm(forms.Form):

    nombre = forms.CharField()
    tipo_de_comida = forms.CharField()
    precio = forms.IntegerField()