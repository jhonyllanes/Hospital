from django.contrib import admin
from .models.Usuario import Usuario
from .models.familiar import Familiar
from .models.his_clinica import Historia_Clinica
from .models.paciente import Paciente
from .models.sig_vitales import Signos_Vitales
from .models.Psalud import Personal_Salud

admin.site.register(Usuario)
admin.site.register(Familiar)
admin.site.register(Historia_Clinica)
admin.site.register(Signos_Vitales)
admin.site.register(Paciente)
admin.site.register(Personal_Salud)





# Register your models here.
