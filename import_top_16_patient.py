'''
只匯入16位名人的資料
'''
import pandas as pd


def main():
    df = pd.read_csv("jiahong.csv")
    min = 120
    patients_list = []
    for index, row in df.iterrows():
        if row.isnull().sum() < min:
            # min = row.isnull().sum()
            # print(row.isnull().sum())
            print("id: ", row[1], " NAN: ", row.isnull().sum())
            patients_list.append(row[1])

        # print(type(row))
    print(patients_list)

    # [145867, 189335, 210238, 227101, 168850, 163555, 222024, 564545, 541134, 565598, 542502, 549524, 573071, 539939, 548034, 562261]
PATIENTS_LIST = [
    145867, 189335, 210238, 227101, 168850, 163555, 222024, 564545, 541134, 565598, 542502, 549524, 573071, 539939, 548034, 562261
]
# 14存活 2死亡


def filter_patient_id(df, filename):

    df_new = None
    for i in PATIENTS_LIST:

        tmp = df[df['patientunitstayid'] == i]

        if type(df_new) == type(None):
            df_new = tmp
        else:
            df_new = pd.concat([df_new, tmp], join='inner')
            # print(pd.concat([df_new, tmp], join='inner'))
    print(df_new)
    df_new.to_csv(f"result_{filename}.csv", index=False)


if __name__ == "__main__":
    # main()
    df = pd.read_csv("jiahong.csv")
    filter_patient_id(df, '')

    df = pd.read_csv("finish_intakeoutput.csv")
    filter_patient_id(df, 'intakeoutput')

    df = pd.read_csv("finish_lab.csv")
    filter_patient_id(df, 'lab')

    df = pd.read_csv("finish_respiratoryCharting.csv")
    filter_patient_id(df, 'respiratoryCharting')

    df = pd.read_csv("finish_vitalperiodic.csv")
    filter_patient_id(df, 'vitalperiodic')
