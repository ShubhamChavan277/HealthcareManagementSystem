from django.contrib import admin

from .models import Doctor, VidApp, VidDoc, VAppointment, PhyDoc,PhyApp, PAppointment
# Register your models here.

admin.site.register(Doctor)
admin.site.register(VidDoc)
admin.site.register(VidApp)
admin.site.register(VAppointment)
admin.site.register(PhyDoc)
admin.site.register(PhyApp)
admin.site.register(PAppointment)
