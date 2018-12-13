from django.contrib import admin
from .models import Galguerias
from .models import Personas
from .models import Preferecias_galguerias
from .models import Tipo_producto


admin.site.register(Galguerias)
admin.site.register(Personas)
admin.site.register(Preferecias_galguerias)
admin.site.register(Tipo_producto)
# Register your models here.
