from django.db.models import QuerySet
from django.shortcuts import render
from django.http import JsonResponse
from patient.models import Patient, VitalPeriodic, RespiratoryCharting, IntakeOutput, Lab
import json


def get_patient(request):
    try:
        json_data = json.loads(request.body)
    except:
        data = {
            'success': False,
            'detail': 'data format must be JSON.'
        }
        return JsonResponse(data, status=400)

    id = json_data['id']
    try:
        patient = Patient.objects.get(patientunitstayid=id)
    except:
        data = {
            'success': False,
            'detail': 'patient not found.'
        }
        return JsonResponse(data, status=400)
    return patient


def serializers_patient_data(patient: Patient):
    result = {
        "patientunitstayid": patient.patientunitstayid,
        "gender": patient.gender,
        "age": patient.age,
        "admissionheight": float(patient.admissionheight),
        "admissionweight": float(patient.admissionweight),
        "dischargeweight": float(patient.dischargeweight),
        "apachescore": patient.apachescore,
        "unitdischargestatus": patient.unitdischargestatus,
    }

    return result


def serializers_vitalPeriodic_data(vitalPeriodic_QS: QuerySet(VitalPeriodic)):
    result_list = []
    for vitalPeriodic in vitalPeriodic_QS:
        result = {
            "patientunitstayid": vitalPeriodic.patient.patientunitstayid,
            "saO2": vitalPeriodic.saO2,
            "heartRate": vitalPeriodic.heartRate,
            "respiration": vitalPeriodic.respiration,
            "systemicSystolic": vitalPeriodic.saO2,
            "systemicDiastolic": vitalPeriodic.systemicDiastolic,
            "systemicMean": vitalPeriodic.systemicMean,
            "observationOffset": vitalPeriodic.observationOffset,
        }
        result_list.append(result)

    return result_list


def serializers_RespiratoryCharting_data(respiratoryCharting_QS: QuerySet(RespiratoryCharting)):

    result_list = []
    for respiratoryCharting in respiratoryCharting_QS:
        result = {
            "patientunitstayid": respiratoryCharting.patient.patientunitstayid,
            "respChartValueLabel": respiratoryCharting.respChartValueLabel,
            "respChartValue": respiratoryCharting.respChartValue,
            "respChartOffset": respiratoryCharting.respChartOffset,
        }
        result_list.append(result)

    return result_list


def serializers_IntakeOutput_data(intakeOutput_QS: QuerySet(IntakeOutput)):
    result_list = []
    for intakeOutput in intakeOutput_QS:
        result = {
            "patientunitstayid": intakeOutput.patient.patientunitstayid,
            "intakeTotal": intakeOutput.intakeTotal,
            "outputTotal": intakeOutput.outputTotal,
            "dialysisTotal": intakeOutput.dialysisTotal,
            "netTotal": intakeOutput.netTotal,
            "intakeOutputOffset": intakeOutput.intakeOutputOffset,
        }
        result_list.append(result)

    return result_list


def serializers_Lab_data(lab_QS: QuerySet(Lab)):
    result_list = []
    for lab in lab_QS:
        result = {
            "patientunitstayid": lab.patient.patientunitstayid,
            "labName": lab.labName,
            "labResult": lab.labResult,
            "labResultOffset": lab.labResultOffset,
        }
        result_list.append(result)

    return result_list


def patient_data(request):

    try:
        json_data = json.loads(request.body)
    except:
        data = {
            'success': False,
            'detail': 'data format must be JSON.'
        }
        return JsonResponse(data, status=400)

    id = json_data['id']
    try:
        patient = Patient.objects.get(patientunitstayid=id)
    except:
        data = {
            'success': False,
            'detail': 'patient not found.'
        }
        return JsonResponse(data, status=400)

    serialized_patient = serializers_patient_data(patient)
    data = {
        'success': True,
        "data": serialized_patient
    }
    return JsonResponse(data, status=200)


def patient_vitalPeriodic_data(request):
    res = get_patient(request)
    if type(res) != type(Patient()):
        return res

    vitalPeriodic_QS = VitalPeriodic.objects.filter(patient=res)
    serialized_data = serializers_vitalPeriodic_data(vitalPeriodic_QS)
    data = {
        'success': True,
        "data": serialized_data
    }
    return JsonResponse(data, status=200)


def patient_respiratoryCharting_data(request):
    res = get_patient(request)
    if type(res) != type(Patient()):
        return res

    respiratoryCharting_QS = RespiratoryCharting.objects.filter(patient=res)
    serialized_data = serializers_RespiratoryCharting_data(
        respiratoryCharting_QS)
    data = {
        'success': True,
        "data": serialized_data
    }
    return JsonResponse(data, status=200)


def patient_intakeOutput_data(request):
    res = get_patient(request)
    if type(res) != type(Patient()):
        return res

    intakeOutput_QS = IntakeOutput.objects.filter(patient=res)
    serialized_data = serializers_IntakeOutput_data(intakeOutput_QS)
    data = {
        'success': True,
        "data": serialized_data
    }
    return JsonResponse(data, status=200)


def patient_lab_data(request):
    res = get_patient(request)
    if type(res) != type(Patient()):
        return res

    lab_QS = Lab.objects.filter(patient=res)
    serialized_data = serializers_Lab_data(lab_QS)
    data = {
        'success': True,
        "data": serialized_data
    }
    return JsonResponse(data, status=200)


def predict_model(request):
    pass
    """
    從csv抓病人已整理完的資料
    再丟到模型做預測
    """
    import pickle

    data = []
    # 讀取Model
    with open('./model/xgboost-iris.pickle', 'rb') as f:
        xgboostModel = pickle.load(f)
        pred = xgboostModel.predict(data)
        print(pred)


"""
1. 圖表 折線圖
2. 把預測模型的程式碼搬過來
3. 把 flask 那邊讀 csv 的程式碼搬過來
4. 看 lime 程式碼
5. 欄位翻譯成中文
"""
