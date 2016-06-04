# ano_escolar/views.py

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from . models import Anuario
from . models import Salones_curso

def index(request):
	anuarios = Anuario.objects.order_by('anuario')
	context = {'anuarios': anuarios}
	return render(request, 'ano_escolar/index.html', context)

def cursos(request, ano_escolar_id):
	cursos = get_object_or_404(Salones, pk= ano_escolar_id)
	return render(request, 'ano_escolar/cursos.html')

	#return HttpResponse("You are looking at the courses for ano_escolar %s." % ano_escolar_id)

def alumnos(request, ano_escolar_id, salon_id):
	return HttpResponse("You are looking at ano_escolar %s and salon %s." % ( ano_escolar_id, salon_id))
