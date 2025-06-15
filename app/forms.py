from django import forms
from .models import Persona, DatoBiometrico

class PersonaForm(forms.ModelForm):
    """
    Formulario para crear y editar una instancia del modelo Persona.
    ModelForm crea automáticamente los campos del formulario basados en el modelo.
    """
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'identificador_unico']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Juan'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Pérez'}),
            'identificador_unico': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Cédula o ID de empleado'}),
        }

class DatoBiometricoForm(forms.ModelForm):
    """
    Formulario para "capturar" los datos biométricos simulados.
    """
    class Meta:
        model = DatoBiometrico
        # Excluimos el campo 'persona' porque lo asignaremos automáticamente
        # en la vista después de saber a quién pertenece el dato biométrico.
        fields = ['tipo_biometrico', 'ruta_simulada']
        widgets = {
            'tipo_biometrico': forms.Select(attrs={'class': 'form-select'}),
            'ruta_simulada': forms.FileInput(attrs={'class': 'form-control'}),
        }