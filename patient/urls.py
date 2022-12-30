from django.contrib import admin
from django.urls import path, include
from patient.views import patient_data, patient_vitalPeriodic_data, patient_respiratoryCharting_data, patient_intakeOutput_data, patient_lab_data


urlpatterns = [
    path('', patient_data),
    path('vitalPeriodic/', patient_vitalPeriodic_data),
    path('respiratoryCharting/', patient_respiratoryCharting_data),
    path('intakeOutput/', patient_intakeOutput_data),
    path('lab/', patient_lab_data)

]
