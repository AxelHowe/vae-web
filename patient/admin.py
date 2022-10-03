from django.contrib import admin
from patient.models import Patient, IntakeOutput, Lab, RespiratoryCharting, VitalPeriodic
# Register your models here.
admin.site.register(Patient)
admin.site.register(IntakeOutput)
admin.site.register(Lab)
admin.site.register(RespiratoryCharting)
admin.site.register(VitalPeriodic)
