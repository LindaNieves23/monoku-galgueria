from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'monoku'
urlpatterns = [
    path('', views.index, name='index'),
    path('Galguerias/', views.galgueria, name='galgueria'),
    path('personas/', views.personas, name='personas'),
    path('Preferecias_galguerias/', views.preferencias_galguerias, name='preferencias'),
    path('crear_personas/', views.crear_personas, name='crear_personas'),
    path('crear_galguerias/', views.crear_galguerias, name='crear_galguerias'),
    path('crear_preferencias/', views.crear_preferencias, name='crear_preferencias'),
    url(r'^login/$', views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    ]