from django.db import models

# Create your models here.

class Telefono(models.Model):
    COMPANIA=[
        ("Tigo", "Tigo Guatemala"),
        ("Claro", "Claro Guatemala"),
        ("Twenty","Twenty America"),
        ("Movistar", "Movistar"),
    ]

    telefono = models.CharField(max_length=15)
    compania = models.CharField(max_length=8, choices=COMPANIA)
    
    class Meta:
        verbose_name = 'Telefono'
        verbose_name_plural = 'Telefonos'
        
    def __str__(self):
        return self.telefono + " ----- "+ self.compania
    
class Departamento(models.Model):
    nombre = models.CharField(max_length=15)
    descripcion = models.TextField()

    class Meta:
       
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return self.nombre + " ----- " + self.descripcion

class Inscrito(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    direccion = models.CharField(max_length=50)
    departamento_id = models.ForeignKey(Departamento,on_delete = models.PROTECT, null= False, blank=False)
    
    class Meta:
        verbose_name = 'Inscrito'
        verbose_name_plural = 'Inscritos'

    def __str__(self):
        return self.nombre +" "+ self.apellido + " " + self.direccion

class Responsable(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    direccion = models.CharField(max_length=50)
    telefono_id = models.ForeignKey(Telefono,on_delete = models.PROTECT, null= False, blank=False)
    class Meta:
        verbose_name = 'Responsable'
        verbose_name_plural = 'Responsables'

    def __str__(self):
        return self.nombre + " " + self.apellido + " " + self.direccion


class Contacto(models.Model):
    contacto_num = models.CharField(max_length=15, null=True, default="N/A")
    inscrito_id = models.ForeignKey(Inscrito, on_delete = models.PROTECT, null= False, blank=False)
    responsable_id = models.ForeignKey(Responsable, on_delete = models.PROTECT, null= False, blank=False)
   
    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.contacto_num +" " + self.inscrito_id
