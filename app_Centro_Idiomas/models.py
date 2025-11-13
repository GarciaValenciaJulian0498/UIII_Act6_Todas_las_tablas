from django.db import models

class Idioma(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    nivel = models.CharField(max_length=50)
    region = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    codigo = models.CharField(max_length=10, unique=True)
    bandera_img = models.ImageField(upload_to='banderas/', blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    ap_paterno = models.CharField(max_length=100)
    ap_materno = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    correo = models.EmailField(unique=True)
    id_idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE, related_name="profesores")

    def __str__(self):
        return f"{self.nombre} {self.ap_paterno}"
    
class Aulas(models.Model):
    numero_aula = models.CharField(max_length=10, unique=True)
    capacidad = models.IntegerField()
    ubicacion = models.CharField(max_length=100, blank=True, null=True)
    tipo_aula = models.CharField(max_length=50, blank=True, null=True) # Ej: "Laboratorio", "Teoría", "Seminario"

    def __str__(self):
        return f"Aula {self.numero_aula}"
    
class Clase(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    capacidad = models.PositiveIntegerField()
    nivel = models.CharField(max_length=50, choices=[
        ('Básico A1', 'Básico A1'),
        ('Básico A2', 'Básico A2'),
        ('Intermedio B1', 'Intermedio B1'),
        ('Intermedio B2', 'Intermedio B2'),
        ('Avanzado C1', 'Avanzado C1'),
        ('Avanzado C2', 'Avanzado C2')
    ])
    id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name="clases")
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE, related_name="clases_idioma")
    aula = models.ForeignKey('Aulas', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.idioma.nombre})"
    

class Alumnos(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    clase = models.ForeignKey(Clase, on_delete=models.SET_NULL, null=True, blank=True, related_name='alumnos')

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno}"