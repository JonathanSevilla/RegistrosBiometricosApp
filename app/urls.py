from django.contrib import admin
from django.urls import path
from .views import enrolar_persona, persona_detalle, capturar_biometria, pagina_seguimiento, registrar_ingreso, registrar_salida, detalle_persona, lista_personas

app_name = 'app'

urlpatterns = [
    # Página principal/terminal de seguimiento
    # Ejemplo: http://127.0.0.1:8000/
    path('', pagina_seguimiento, name='pagina_seguimiento'),

    # Ruta para iniciar el enrolamiento de una nueva persona
    # Ejemplo: http://127.0.0.1:8000/enrolar/
    path('enrolar/', enrolar_persona, name='enrolar_persona'),
    
    # Rutas que necesitan un ID de persona. El <int:persona_id> captura el número
    # de la URL y lo pasa como un argumento a la vista.
    path('personas/', lista_personas, name='lista_personas'),
    path('persona/<int:persona_id>/detalle/', persona_detalle, name='persona_detalle'),
    
    # Ruta para ver los detalles de una persona ya enrolada
    # Ejemplo: http://127.0.0.1:8000/persona/1/
    path('persona/<int:persona_id>/', detalle_persona, name='detalle_persona'),

    # Ruta para "capturar" datos biométricos de una persona específica
    # Ejemplo: http://127.0.0.1:8000/persona/1/capturar/
    path('persona/<int:persona_id>/captura', capturar_biometria, name='capturar_biometria'),

    # Rutas para simular el registro de ingreso y salida
    # Ejemplo: http://127.0.0.1:8000/persona/1/ingreso/
    path('persona/<int:persona_id>/ingreso/', registrar_ingreso, name='registrar_ingreso'),
    
    # Ejemplo: http://127.0.0.1:8000/persona/1/salida/
    path('persona/<int:persona_id>/salida/', registrar_salida, name='registrar_salida'),
]
