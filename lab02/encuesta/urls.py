from django.urls import path

from . import views

app_name = 'encuesta'

urlpatterns = [
    # ex: /encuesta/
    path('', views.index, name='index'),
    path('enviar', views.enviar, name='enviar'),
    path('calculadora', views.calculadora, name='index'),
    path('cilindro', views.cilindro, name='index'),
    path('enviarcilindro', views.enviarcilindro, name='enviarcilindro'),
    path('enviarcalculadora', views.enviarcalculadora, name='enviarcalculadora')
]