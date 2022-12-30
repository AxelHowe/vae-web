# VAE API 文件
[TOC]

## 使用的病人ID(不是PID)
> 前 16 位 nan 值 最少的病人

145867, 189335, 210238, 227101, 168850, 163555, 222024, 564545, 541134, 565598, 542502, 549524, 573071, 539939, 548034, 562261
> 死亡病人為：227101、565598
> 其餘病人皆存活
## 生存率
145867：99%
189335：98%
210238：97%
227101：6%
168850：100%
163555：51%
222024：99%
564545：98%
541134：97%
565598：4%
542502：99%
549524：99%
573071：96%
539939：100%
548034：100%
562261：72%

## URL

- patient/
- patient/all/
- patient/vitalPeriodic/
- patient/respiratoryCharting/
- patient/intakeOutput/
- patient/lab/
- patient/lab/static/

## 前端要帶的參數

- 靜態資料
    - patient/
    - patient/lab/static/
    ```json=
    {
        "id": 病人ID
    }
    ```
    - patient/all/
        - 不用帶任何參數
- 動態資料
    - patient/vitalPeriodic/
    - patient/respiratoryCharting/
    - patient/intakeOutput/
```json=
{
    "id": 病人ID,
    "field_name": "欄位名稱",
    "hour": true // true 代表回傳的 offset 單位為小時
}
```

## 回傳資料

- 靜態資料
    - patient/
    ```json=
    {
        "success": true,
        "data": {
            "patientunitstayid": 145867,
            "gender": "Female",
            "age": "52",
            "admissionheight": 162.6,
            "admissionweight": 59.0,
            "dischargeweight": 62.3,
            "apachescore": 97,
            "unitdischargestatus": "Alive"
        }
    }
    ```
    - patient/lab/static/
        - 靜態資料有多筆資料時，取第一筆當量測值
        - 無資料時回傳 NULL
    ```json=
    {
        "success": true,
        "patientunitstayid": 145867,
        "data": [
            {
                "name": "troponin - I",
                "value": "0.4000",
                "offset": 680
            },
            {
                "name": "direct bilirubin",
                "value": "0.8000",
                "offset": -265
            },
            {
                "name": "lactate",
                "value": "0.7000",
                "offset": 680
            },
            {
                "name": "fibrinogen",
                "value": null
            },
            {
                "name": "CPK-MB INDEX",
                "value": null
            },
            {
                "name": "CPK",
                "value": "494.0000",
                "offset": -265
            },
            {
                "name": "CPK-MB",
                "value": null
            },
            {
                "name": "HDL",
                "value": null
            },
            {
                "name": "LDL",
                "value": null
            },
            {
                "name": "total cholesterol",
                "value": null
            },
            {
                "name": "PTT",
                "value": "30.0000",
                "offset": -265
            },
            {
                "name": "PTT ratio",
                "value": null
            },
            {
                "name": "TSH",
                "value": null
            },
            {
                "name": "ammonia",
                "value": null
            },
            {
                "name": "amylase",
                "value": "567.0000",
                "offset": 60
            },
            {
                "name": "lipase",
                "value": "455.0000",
                "offset": 9445
            },
            {
                "name": "T4",
                "value": null
            },
            {
                "name": "Vitamin B12",
                "value": null
            },
            {
                "name": "Fe",
                "value": null
            },
            {
                "name": "TIBC",
                "value": null
            },
            {
                "name": "ionized calcium",
                "value": "4.7200",
                "offset": 1975
            },
            {
                "name": "Ferritincortisol",
                "value": null
            },
            {
                "name": "free T4",
                "value": null
            },
            {
                "name": "T3",
                "value": null
            },
            {
                "name": "uric acid",
                "value": null
            },
            {
                "name": "serum osmolality",
                "value": null
            },
            {
                "name": "BNP",
                "value": "38.0000",
                "offset": 160
            },
            {
                "name": "troponin - T",
                "value": null
            },
            {
                "name": "CRP",
                "value": null
            },
            {
                "name": "Fe/TIBC Ratio",
                "value": null
            },
            {
                "name": "LDH",
                "value": null
            },
            {
                "name": "transferrin",
                "value": null
            },
            {
                "name": "prealbumin",
                "value": null
            }
        ]
    }
    ```
- 動態資料
    - patient/vitalPeriodic/
    - patient/respiratoryCharting/
    - patient/intakeOutput/
```json=
{
    "success": true,
    "patientunitstayid": 145867,
    "field_name": "heartRate",
    "data": [
        {
            "value": 115,
            "offset": 3273
        },
        {
            "value": 130,
            "offset": 313
        },
        // 以下資料略
    ]
}
```