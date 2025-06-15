# en tu_app/models.py
from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    identificador_unico = models.CharField(max_length=50, unique=True)
    # Otros campos que necesites: email, fecha de nacimiento, etc.

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class DatoBiometrico(models.Model):
    TIPO_CHOICES = [
        ('rostro', 'Rostro'),
        ('huella', 'Huella Dactilar'),
    ]
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='datos_biometricos')
    tipo_biometrico = models.CharField(max_length=10, choices=TIPO_CHOICES)
    # En un escenario real, aquí guardarías una plantilla o hash del dato biométrico.
    # Para el MVP, simularemos guardando la ruta a una imagen de ejemplo.
    ruta_simulada = models.ImageField(upload_to='biometric_data/')

    def __str__(self):
        return f"Dato biométrico de {self.persona.nombre} ({self.tipo_biometrico})"

class RegistroAcceso(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    fecha_hora_ingreso = models.DateTimeField(auto_now_add=True)
    fecha_hora_salida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Registro de {self.persona.nombre} - Ingreso: {self.fecha_hora_ingreso}"