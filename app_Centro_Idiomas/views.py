from django.shortcuts import render, redirect, get_object_or_404
from .models import Idioma, Profesor, Clase, Aulas, Alumnos # Importa todos los modelos

def inicio_centro_idiomas(request):
    return render(request, 'inicio.html')

def agregar_idioma(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        nivel = request.POST.get('nivel')
        region = request.POST.get('region')
        descripcion = request.POST.get('descripcion')
        codigo = request.POST.get('codigo')
        # bandera_img = request.FILES.get('bandera_img') # Para manejar imágenes, se necesita configurar MEDIA_ROOT y MEDIA_URL en settings.py

        idioma = Idioma(
            nombre=nombre,
            nivel=nivel,
            region=region,
            descripcion=descripcion,
            codigo=codigo,
            # bandera_img=bandera_img
        )
        idioma.save()
        return redirect('ver_idiomas')
    return render(request, 'idioma/agregar_idioma.html')

def ver_idiomas(request):
    idiomas = Idioma.objects.all()
    return render(request, 'idioma/ver_idiomas.html', {'idiomas': idiomas})

def actualizar_idioma(request, id_idioma):
    idioma = get_object_or_404(Idioma, pk=id_idioma)
    if request.method == 'POST':
        idioma.nombre = request.POST.get('nombre')
        idioma.nivel = request.POST.get('nivel')
        idioma.region = request.POST.get('region')
        idioma.descripcion = request.POST.get('descripcion')
        idioma.codigo = request.POST.get('codigo')
        # if 'bandera_img' in request.FILES:
        #    idioma.bandera_img = request.FILES['bandera_img']
        idioma.save()
        return redirect('ver_idiomas')
    return render(request, 'idioma/actualizar_idioma.html', {'idioma': idioma})

def borrar_idioma(request, id_idioma):
    idioma = get_object_or_404(Idioma, pk=id_idioma)
    if request.method == 'POST':
        idioma.delete()
        return redirect('ver_idiomas')
    return render(request, 'idioma/borrar_idioma.html', {'idioma': idioma})

def agregar_profesor(request):
    idiomas = Idioma.objects.all() # Obtener todos los idiomas para el select
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        ap_paterno = request.POST.get('ap_paterno')
        ap_materno = request.POST.get('ap_materno')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        id_idioma_id = request.POST.get('id_idioma') # Obtener el ID del idioma seleccionado

        idioma_obj = get_object_or_404(Idioma, pk=id_idioma_id) # Obtener el objeto Idioma
        
        Profesor.objects.create(
            nombre=nombre,
            ap_paterno=ap_paterno,
            ap_materno=ap_materno,
            telefono=telefono,
            correo=correo,
            id_idioma=idioma_obj
        )
        return redirect('ver_profesores') # Redirigir a la lista de profesores
    return render(request, 'profesores/agregar_profesor.html', {'idiomas': idiomas})

# Función para ver todos los profesores
def ver_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesores/ver_profesores.html', {'profesores': profesores})

# Función para editar un profesor (muestra el formulario con datos actuales)
def actualizar_profesor(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    idiomas = Idioma.objects.all()
    return render(request, 'profesores/actualizar_profesor.html', {'profesor': profesor, 'idiomas': idiomas})

# Función para realizar la actualización del profesor
def realizar_actualizacion_profesor(request, pk):
    if request.method == 'POST':
        profesor = get_object_or_404(Profesor, pk=pk)
        profesor.nombre = request.POST.get('nombre')
        profesor.ap_paterno = request.POST.get('ap_paterno')
        profesor.ap_materno = request.POST.get('ap_materno')
        profesor.telefono = request.POST.get('telefono')
        profesor.correo = request.POST.get('correo')
        
        id_idioma_id = request.POST.get('id_idioma')
        idioma_obj = get_object_or_404(Idioma, pk=id_idioma_id)
        profesor.id_idioma = idioma_obj
        
        profesor.save()
        return redirect('ver_profesores')
    return redirect('ver_profesores') # En caso de que se acceda por GET, redirigir

# Función para borrar un profesor
def borrar_profesor(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    if request.method == 'POST':
        profesor.delete()
        return redirect('ver_profesores')
    return render(request, 'profesores/borrar_profesor.html', {'profesor': profesor})

def agregar_clase(request):
    profesores = Profesor.objects.all()
    idiomas = Idioma.objects.all()
    aulas= Aulas.objects.all()

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        capacidad = request.POST.get('capacidad')
        nivel = request.POST.get('nivel')
        id_profesor_id = request.POST.get('id_profesor')
        idioma_id = request.POST.get('idioma')
        aula=request.POST.get('aula')

        # Convertir id_profesor e idioma a sus objetos correspondientes
        profesor_obj = get_object_or_404(Profesor, pk=id_profesor_id)
        idioma_obj = get_object_or_404(Idioma, pk=idioma_id)
        aula_obj = get_object_or_404(Aulas, pk=aula)

        Clase.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            capacidad=capacidad,
            nivel=nivel,
            id_profesor=profesor_obj,
            idioma=idioma_obj,
            aula=aula_obj
        )
        return redirect('ver_clases')
    return render(request, 'clases/agregar_clase.html', {'profesores': profesores, 'idiomas': idiomas})

# Función para ver todas las clases
def ver_clases(request):
    clases = Clase.objects.all()
    return render(request, 'clases/ver_clases.html', {'clases': clases})

# Función para actualizar una clase (muestra el formulario con datos actuales)
def actualizar_clase(request, pk):
    clase = get_object_or_404(Clase, pk=pk)
    profesores = Profesor.objects.all()
    idiomas = Idioma.objects.all()
    aulas= Aulas.objects.all()
    return render(request, 'clases/actualizar_clase.html', {'clase': clase, 'profesores': profesores, 'idiomas': idiomas, 'aulas':aulas})

# Función para realizar la actualización (maneja el POST del formulario)
def realizar_actualizacion_clase(request, pk):
    clase = get_object_or_404(Clase, pk=pk)
    if request.method == 'POST':
        clase.nombre = request.POST.get('nombre')
        clase.descripcion = request.POST.get('descripcion')
        clase.capacidad = request.POST.get('capacidad')
        clase.nivel = request.POST.get('nivel')

        id_profesor_id = request.POST.get('id_profesor')
        idioma_id = request.POST.get('idioma')
        aula=request.POST.get('aula')

        clase.id_profesor = get_object_or_404(Profesor, pk=id_profesor_id)
        clase.idioma = get_object_or_404(Idioma, pk=idioma_id)
        clase.aula = get_object_or_404(Aulas, pk=aula)
        clase.save()
        return redirect('ver_clases')
    return redirect('actualizar_clase', pk=pk) # Redirige al formulario si no es POST

# Función para borrar una clase
def borrar_clase(request, pk):
    clase = get_object_or_404(Clase, pk=pk)
    if request.method == 'POST':
        clase.delete()
        return redirect('ver_clases')
    return render(request, 'clases/borrar_clase.html', {'clase': clase})

def agregar_alumno(request):
    clases = Clase.objects.all() # Obtiene todas las clases para el combobox
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido_paterno = request.POST.get('apellido_paterno')
        apellido_materno = request.POST.get('apellido_materno')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        clase_id = request.POST.get('clase') # Captura el ID de la clase seleccionada

        clase_obj = None
        if clase_id:
            clase_obj = get_object_or_404(Clase, pk=clase_id)

        alumno = Alumnos(
            nombre=nombre,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            correo=correo,
            telefono=telefono,
            clase=clase_obj
        )
        alumno.save()
        return redirect('ver_alumnos') # Redirige a la lista de alumnos
    return render(request, 'alumnos/agregar_alumno.html', {'clases': clases})

def ver_alumnos(request):
    alumnos = Alumnos.objects.all()
    return render(request, 'alumnos/ver_alumnos.html', {'alumnos': alumnos})

def actualizar_alumno(request, pk):
    alumno = get_object_or_404(Alumnos, pk=pk)
    clases = Clase.objects.all() # Para el combobox de clases
    return render(request, 'alumnos/actualizar_alumno.html', {'alumno': alumno, 'clases': clases})

def realizar_actualizacion_alumno(request, pk):
    alumno = get_object_or_404(Alumnos, pk=pk)
    if request.method == 'POST':
        alumno.nombre = request.POST.get('nombre')
        alumno.apellido_paterno = request.POST.get('apellido_paterno')
        alumno.apellido_materno = request.POST.get('apellido_materno')
        alumno.correo = request.POST.get('correo')
        alumno.telefono = request.POST.get('telefono')
        clase_id = request.POST.get('clase')

        clase_obj = None
        if clase_id:
            clase_obj = get_object_or_404(Clase, pk=clase_id)
        alumno.clase = clase_obj

        alumno.save()
        return redirect('ver_alumnos')
    return redirect('ver_alumnos') # En caso de que se acceda directamente sin POST

def borrar_alumno(request, pk):
    alumno = get_object_or_404(Alumnos, pk=pk)
    if request.method == 'POST':
        alumno.delete()
        return redirect('ver_alumnos')
    return render(request, 'alumnos/borrar_alumno.html', {'alumno': alumno})


# ==========================================
# FUNCIONES CRUD PARA AULAS
# ==========================================

def agregar_aula(request):
    if request.method == 'POST':
        numero_aula = request.POST.get('numero_aula')
        capacidad = request.POST.get('capacidad')
        ubicacion = request.POST.get('ubicacion')
        tipo_aula = request.POST.get('tipo_aula')

        aula = Aulas(
            numero_aula=numero_aula,
            capacidad=capacidad,
            ubicacion=ubicacion,
            tipo_aula=tipo_aula
        )
        aula.save()
        return redirect('ver_aulas')
    return render(request, 'aulas/agregar_aula.html')

def ver_aulas(request):
    aulas = Aulas.objects.all()
    return render(request, 'aulas/ver_aulas.html', {'aulas': aulas})

def actualizar_aula(request, pk):
    aula = get_object_or_404(Aulas, pk=pk)
    return render(request, 'aulas/actualizar_aula.html', {'aula': aula})

def realizar_actualizacion_aula(request, pk):
    aula = get_object_or_404(Aulas, pk=pk)
    if request.method == 'POST':
        aula.numero_aula = request.POST.get('numero_aula')
        aula.capacidad = request.POST.get('capacidad')
        aula.ubicacion = request.POST.get('ubicacion')
        aula.tipo_aula = request.POST.get('tipo_aula')
        aula.save()
        return redirect('ver_aulas')
    return redirect('ver_aulas')

def borrar_aula(request, pk):
    aula = get_object_or_404(Aulas, pk=pk)
    if request.method == 'POST':
        aula.delete()
        return redirect('ver_aulas')
    return render(request, 'aulas/borrar_aula.html', {'aula': aula})