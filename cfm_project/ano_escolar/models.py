from __future__ import unicode_literals

from django.db import models

class Anuario(models.Model):
   anuario      = models.IntegerField(unique=True)
   anuario_text = models.CharField(max_length = 15, unique=True)
   
   def __unicode__(self):
      return self.anuario_text
      
class Salones_curso(models.Model):
   anuario = models.ForeignKey(Anuario)
   salon   = models.IntegerField(unique=True)
   curso   = models.CharField(max_length = 40, unique=True)
   
   def __unicode__(self):
      return u'%s %s' %(self.curso, self.salon)
   
class Alumno(models.Model):
   anuario   = models.ForeignKey(Anuario)
   salon     = models.ForeignKey(Salones_curso)
   nombre    = models.CharField(max_length = 20)
   apellidos = models.CharField(max_length = 20)
   exe       = models.BooleanField(default=False)
   prim10    = models.BooleanField(default=False)
   foto_gde  = models.ImageField(upload_to='media/', null=True, blank=True)
   foto_med  = models.ImageField(upload_to='media/', null=True, blank=True)
   foto_peq  = models.ImageField(upload_to='media/', null=True, blank=True)
   
   def __unicode__(self):
      return u'%s %s' %(self.apellidos, self.nombre)

