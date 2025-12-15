import pickle
import streamlit as st

# baca model
diabetes_model = pickle.load( open ('diabetes_model.sav', 'rb'))

# judul web
st.title('Data mining prediksi diabetes')
# membagi kolom
col1, col2 = st.columns(2)
with col1:
    Pregnancies = st.text_input('input niilai Pregnancies')
    
with col2:
    Glucose = st.text_input('input niilai Glucose')
    
with col1:
    BloodPressure = st.text_input('input niilai BloodPressure')
    
with col2:
    SkinThickness = st.text_input('input niilai SkinThickness')
    
with col1:
    Insulin = st.text_input('input niilai Insulin')
    
with col2:
    BMI = st.text_input('input niilai BMI')
    
with col1:
    DiabetesPedigreeFunction = st.text_input('input niilai DiabetesPedigreeFunction')
    
with col2:
    Age = st.text_input('input niilai Age')

# Outcome = st.text_input('input niilai Outcome')

# code prediksi
diab_diagnostik = ''

# membuat tombol untuk prediksi'
if(st.button('Test prediksi diabetes')):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
    if(diab_prediction[0] == 1):
        diab_diagnostik = 'pasien terkena diabetes'
    else:
        diab_diagnostik = 'pasien tidak terkena diabetes'
    st.success(diab_diagnostik)