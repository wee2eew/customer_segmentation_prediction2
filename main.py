# import libraries ต่างๆ ที่จำเป็น
import pandas as pd
from sklearn.cluster import KMeans

def train_model(df):
    # เลือกเฉพาะ feature 'Age'  และ  'Spending Score (1-100)' ดูก่อน
    X1 = df[['Age' , 'Annual Income (k$)' , 'Spending Score (1-100)']].copy()

    Model1 = (KMeans(n_clusters = 3 ,max_iter=300,  random_state= 111))

    # ใช้คำสั่ง .fit() เพื่อเทรนโมเดล
    Model1.fit(X1)
    return Model1

def predict_model(age, annual, spending):
    # read mall customer data
    df = pd.read_csv("mall_200customers.csv", sep=",")
    # print(df)

    # เรียกใช้เมธอด
    Model1 = train_model(df)

    # สร้างข้อมูล testuser
    X_test = [age, annual, spending]
    X_test_new = pd.DataFrame([X_test], columns=['Age' , 'Annual Income (k$)' , 'Spending Score (1-100)'])

    # ทำนายโมเดล
    result = Model1.predict(X_test_new)

    if result==0:
        # print("คุณเป็นกลุ่มลูกค้าอายุน้อย แต่มีกำลังซื้อเยอะ")
        return "คุณเป็นกลุ่มลูกค้าอายุน้อย แต่มีกำลังซื้อเยอะ"
    elif result==1:
        # print("คุณเป็นกลุ่มลูกค้าที่อายุหลากหลาย แต่กำลังซื้อไม่มาก")
        return "คุณเป็นกลุ่มลูกค้าที่อายุหลากหลาย แต่กำลังซื้อไม่มาก"
    else:
        # print("คุณเป็นกลุ่มลูกค้าที่อายุหลากหลาย แต่มีกำลังซื้อปานกลาง")
        return "คุณเป็นกลุ่มลูกค้าที่อายุหลากหลาย แต่มีกำลังซื้อปานกลาง"


predict_model(20, 50, 10)