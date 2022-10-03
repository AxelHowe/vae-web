import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vae_patient_web.settings")
django.setup()

import numpy as np
import pandas as pd
from patient.models import Patient, VitalPeriodic, RespiratoryCharting, IntakeOutput, Lab




'''
先匯入大table result.csv 建立Patient之後
再匯入每個table 看有沒有 patient 在建立資料
'''
import_num = 10000


def clean_all_models():
    Patient.objects.all().delete()
    VitalPeriodic.objects.all().delete()
    RespiratoryCharting.objects.all().delete()
    IntakeOutput.objects.all().delete()
    Lab.objects.all().delete()


def import_patient():
    df = pd.read_csv("result.csv")
    # df.fillna(None)
    df = df.fillna(np.nan).replace([np.nan], [None])
    # print(df.head)
    for index, row in df.iterrows():
        if index == import_num:
            break
        Patient.objects.create(
            patientunitstayid=df.loc[index, "patientunitstayid"],
            gender=df.loc[index, "gender"],
            age=df.loc[index, "age"],
            admissionheight=df.loc[index, "admissionheight"],
            admissionweight=df.loc[index, "admissionweight"],
            dischargeweight=df.loc[index, "dischargeweight"],
            apachescore=df.loc[index, "apachescore"],
            unitdischargestatus=df.loc[index, "unitdischargestatus"],
        )
        # 建立藥物、疾病等靜態資料


def main():

    # import_patient()

    df = pd.read_csv("result_lab.csv")
    df = df.fillna(np.nan).replace([np.nan], [None])
    for index, row in df.iterrows():
        if index == import_num:
            break
        id = df.loc[index, "patientunitstayid"]
        try:
            patient = Patient.objects.get(patientunitstayid=id)
        except:
            continue
        create_lab_model(df, index, patient)

    df = pd.read_csv("result_intakeOutput.csv")
    for index, row in df.iterrows():
        if index == import_num:
            break
        id = df.loc[index, "patientunitstayid"]
        try:
            patient = Patient.objects.get(patientunitstayid=id)
        except:
            continue
        create_intakeOutput_model(df, index, patient)

    df = pd.read_csv("result_respiratoryCharting.csv")
    for index, row in df.iterrows():
        if index == import_num:
            break
        id = df.loc[index, "patientunitstayid"]
        try:
            patient = Patient.objects.get(patientunitstayid=id)
        except:
            continue
        create_respiratoryCharting_model(df, index, patient)

    df = pd.read_csv("result_vitalPeriodic.csv")
    for index, row in df.iterrows():
        if index == import_num:
            break
        id = df.loc[index, "patientunitstayid"]
        try:
            patient = Patient.objects.get(patientunitstayid=id)
        except:
            continue
        create_vitalPeriodic_model(df, index, patient)


def create_lab_model(df, index, patient):

    Lab.objects.create(
        patient=patient,
        labName=df.loc[index, "labname"],
        labResult=df.loc[index, "labresult"],
        labResultOffset=df.loc[index, "labresultoffset"],
    )


def create_respiratoryCharting_model(df, index, patient):
    RespiratoryCharting.objects.create(
        patient=patient,
        respChartValueLabel=df.loc[index, "respchartvaluelabel"],
        respChartValue=df.loc[index, "respchartvalue"],
        respChartOffset=df.loc[index, "respchartoffset"],
    )


def create_intakeOutput_model(df, index, patient):
    IntakeOutput.objects.create(
        patient=patient,
        intakeTotal=df.loc[index, "intaketotal"],
        outputTotal=df.loc[index, "outputtotal"],
        dialysisTotal=df.loc[index, "dialysistotal"],
        netTotal=df.loc[index, "nettotal"],
        intakeOutputOffset=df.loc[index, "intakeoutputoffset"],
    )


def create_vitalPeriodic_model(df, index, patient):
    VitalPeriodic.objects.create(
        patient=patient,
        # saO2=df.loc[index, "saO2"],
        heartRate=df.loc[index, "heartrate"],
        respiration=df.loc[index, "respiration"],
        systemicSystolic=df.loc[index, "systemicsystolic"],
        systemicDiastolic=df.loc[index, "systemicdiastolic"],
        systemicMean=df.loc[index, "systemicmean"],
        observationOffset=df.loc[index, "observationoffset"]
    )


if __name__ == "__main__":

    clean_all_models()
    import_patient()
    main()
