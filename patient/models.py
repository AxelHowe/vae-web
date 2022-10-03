from django.db import models

# Create your models here.

choices = [
    ("Alive", "Alive"),
    ("Expired", "Expired")
]


class Patient(models.Model):
    # id = models.BigAutoField(primary_key=True)
    patientunitstayid = models.IntegerField(null=False)
    # patientunitstayid
    gender = models.CharField(max_length=25, null=True, default=None)
    age = models.CharField(max_length=10, null=True, default=None)
    admissionheight = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, default=None)
    admissionweight = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, default=None)
    dischargeweight = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, default=None)
    apachescore = models.IntegerField(null=True, default=None)
    unitdischargestatus = models.CharField(
        choices=choices, max_length=7)  # Alive, Expired

    # def create(self, *args, **kwargs):
    #     for i in kwargs:
    #         print(i)


class VitalPeriodic(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    saO2 = models.IntegerField(null=True, default=None)
    heartRate = models.IntegerField(null=True, default=None)
    respiration = models.IntegerField(null=True, default=None)
    systemicSystolic = models.IntegerField(null=True, default=None)
    systemicDiastolic = models.IntegerField(null=True, default=None)
    systemicMean = models.IntegerField(null=True, default=None)
    observationOffset = models.IntegerField(null=False)


class RespiratoryCharting(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    respChartValueLabel = models.CharField(
        max_length=255, null=False)
    respChartValue = models.CharField(max_length=1000, null=True, default=None)
    respChartOffset = models.IntegerField(null=False)


class IntakeOutput(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    intakeTotal = models.DecimalField(
        max_digits=12, decimal_places=4, null=True, default=None)
    outputTotal = models.DecimalField(
        max_digits=12, decimal_places=4, null=True, default=None)
    dialysisTotal = models.DecimalField(
        max_digits=12, decimal_places=4, null=True, default=None)
    netTotal = models.DecimalField(
        max_digits=12, decimal_places=4, null=True, default=None)
    intakeOutputOffset = models.IntegerField(null=False)


class Lab(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    labName = models.CharField(max_length=255, null=True, default=None)
    labResult = models.DecimalField(
        max_digits=11, decimal_places=4, null=True, default=None)
    labResultOffset = models.IntegerField(null=True, default=None)
