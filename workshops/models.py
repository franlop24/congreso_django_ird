from django.db import models

# Un modelo es una representación de una tabla

# Tabla Laboratorios/aulas
class Classroom(models.Model):
    FLOORS = [("Planta Baja", "Planta Baja"), ("Planta Alta", "Planta Alta")]
    name = models.CharField(verbose_name="Aula/Laboratorio", max_length=100)
    building = models.CharField(verbose_name="Edificio", max_length=100)
    floor = models.CharField(verbose_name="Planta", max_length=100, choices=FLOORS)

    def __str__(self):
        return self.name + " - " + self.building + " - " + self.floor

    class Meta:
        verbose_name = "Aula/Laboratorio"
        verbose_name_plural = "Aulas/Laboratorios"
    
# tabla taller (workshop)
class Workshop(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=200)
    description = models.TextField(verbose_name="Descripción")
    capacity = models.IntegerField(verbose_name="Capacidad")
    classroom = models.ForeignKey(
            Classroom, 
            related_name="classroom", 
            on_delete=models.SET_NULL,
            null=True)
    image = models.ImageField("Imagen o portada del Taller", 
                              upload_to="images", null=True, blank=True)
    date = models.DateField(verbose_name="Fecha", blank=True, null=True)
    start = models.TimeField(verbose_name="Hora de inicio",blank=True, null=True)
    end = models.TimeField(verbose_name="Hora de término", blank=True, null=True)
    
    
    def __str__(self):
        return self.name + " " + self.classroom.name

    class Meta:
        verbose_name = 'Taller'
        verbose_name_plural = "Talleres"
        ordering = ["name"]