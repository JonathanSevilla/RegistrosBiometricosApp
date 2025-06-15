from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from .models import Persona, DatoBiometrico, RegistroAcceso
from .forms import PersonaForm, DatoBiometricoForm # Debes crear estos formularios

def enrolar_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            persona = form.save()
            # Redirige para "capturar" datos biométricos
            return redirect('app:capturar_biometria', persona_id=persona.id)
    else:
        form = PersonaForm()
    return render(request, 'app/enrolar_persona.html', {'form': form})

def detalle_persona(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)
    return render(request, 'app/detalle_persona.html', {'persona': persona})


def capturar_biometria(request, persona_id):
    persona = Persona.objects.get(id=persona_id)
    print(persona)
    if request.method == 'POST':
        print("---------------------------------")
        form = DatoBiometricoForm(request.POST, request.FILES)
        if form.is_valid():
            dato_biometrico = form.save(commit=False)
            dato_biometrico.persona = persona
            dato_biometrico.save()
            # Puedes añadir más datos o finalizar el enrolamiento
            return redirect('app:detalle_persona', persona_id=persona.id)
    else:
        print("++++++++++++++++++++++++++++++++")
        form = DatoBiometricoForm()
    return render(request, 'app/capturar_biometria.html', {'persona': persona, 'form': form})




def pagina_seguimiento(request):
    personas = Persona.objects.all()
    registros_activos = RegistroAcceso.objects.filter(fecha_hora_salida__isnull=True)
    historial = RegistroAcceso.objects.select_related('persona').order_by('-fecha_hora_ingreso')
    
    return render(request, 'app/seguimiento.html', {
        'personas': personas,
        'registros_activos': registros_activos,
        'historial': historial,
    })


def registrar_ingreso(request, persona_id):
    persona = Persona.objects.get(id=persona_id)
    # Opcional: Verificar si ya tiene un ingreso sin salida
    if not RegistroAcceso.objects.filter(persona=persona, fecha_hora_salida__isnull=True).exists():
        RegistroAcceso.objects.create(persona=persona)
    return redirect('app:pagina_seguimiento')

def registrar_salida(request, persona_id):
    persona = Persona.objects.get(id=persona_id)
    # Busca el último registro de ingreso sin salida para cerrarlo
    registro = RegistroAcceso.objects.filter(persona=persona, fecha_hora_salida__isnull=True).last()
    if registro:
        registro.fecha_hora_salida = timezone.now()
        registro.save()
    return redirect('app:pagina_seguimiento')


from django.shortcuts import render, get_object_or_404
from .models import Persona

def lista_personas(request):
    personas = Persona.objects.all()
    return render(request, 'app/lista_personas.html', {'personas': personas})


def persona_detalle(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)
    registros = persona.registroacceso_set.all().order_by('-fecha_hora_ingreso')
    return render(request, 'app/persona_detalle.html', {
        'persona': persona,
        'registros': registros,
    })
