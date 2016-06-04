from django.contrib import admin

from .models import Anuario, Salones_curso, Alumno

class Salones_cursoInline(admin.TabularInline):
   model = Salones_curso
   extra = 3

class AnuarioAdmin(admin.ModelAdmin):
   fieldsets = [
         (None,      {'fields': ['anuario_text']}),
         #('Anuario', {'fields': ['anuario']}),
   ]
   inlines = [Salones_cursoInline]

class AlumnoInline(admin.TabularInline):
   model = Alumno
   extra = 3

class Salones_cursoAdmin(admin.ModelAdmin):
   fieldsets = [
      (None, {'fields':['anuario', 'salon', 'curso']}),
   ]
   inlines=[AlumnoInline]

   
admin.site.register(Anuario, AnuarioAdmin)
admin.site.register(Salones_curso, Salones_cursoAdmin)
#admin.site.register(Alumno, AlumnoAdmin)


