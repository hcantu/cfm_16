# ano_escolar/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
	# ex /ano_escolar/
	url(r'^$', views.index, name='index'),

	# ex: /ano_escolar/2
	url(r'^(?P<ano_escolar_id>[0-9]+)/$',views.cursos, name='cursos'),

	# ex: /ano_escolar/2/1/
	url(r'^(?P<ano_escolar_id>[0-9]+)/(?P<salon_id>[0-9]+)/$', views.alumnos,  name='alumnos'),
]

