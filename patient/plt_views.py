from django.http import JsonResponse, HttpResponse
from patient.models import Patient, VitalPeriodic, RespiratoryCharting, IntakeOutput, Lab
from patient.views import get_patient
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('SVG')


def vitalPeriodic_picture(request):
    res = get_patient(request)
    if type(res) != type(Patient()):
        return res
    vitalPeriodic_QS = VitalPeriodic.objects.filter(patient=res)
    sao2 = []
    heartRate = []
    respiration = []
    systemicSystolic = []
    systemicDiastolic = []
    systemicMean = []
    for v in vitalPeriodic_QS:
        if v.saO2:
            sao2.append((v.saO2, v.observationOffset))
        if v.heartRate:
            heartRate.append((v.heartRate, v.observationOffset))
        if v.respiration:
            respiration.append((v.respiration, v.observationOffset))
        if v.systemicSystolic:
            systemicSystolic.append((
                v.systemicSystolic, v.observationOffset))
        if v.systemicDiastolic:
            systemicDiastolic.append((
                v.systemicDiastolic, v.observationOffset))
        if v.systemicMean:
            systemicMean.append((v.systemicMean, v.observationOffset))

        pass
    draw_list = [sao2, heartRate, respiration,
                 systemicSystolic, systemicDiastolic, systemicMean]
    x_label = [
        "sao2", "heartRate", "respiration", "systemicSystolic", "systemicDiastolic", "systemicMean"
    ]
    for i in draw_list:
        x = []
        y = []
        for data in i:

            x.append(data[0])
            y.append(data[1])
        # print(i, x, y)
        draw_picture(x, y)

    data = {
        "success": True,
        "label": "a"
    }
    return JsonResponse(data)


def draw_picture(x, y):
    # x = [1, 5, 9, 13, 17]
    # y = [5, 30, 15, 35, 5]
    plt.plot(x, y, color='red')
    plt.xlabel('x label')  # 設定 x 軸標題
    plt.ylabel('Offset')  # 設定 y 軸標題
    plt.xlim(0, 30)  # 設定 x 軸座標範圍
    plt.ylim(0, 50)  # 設定 y 軸座標範圍
    # return plt.show()


def test_picture(request):
    image_data = open("日落.jpeg", "rb").read()
    # 注意舊版的資料使用mimetype,現在已經改為content_type
    return HttpResponse(image_data, content_type="image/png")
