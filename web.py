import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreakss', layout='wide',page_icon="👩‍⚕")


model_dir = "training_models"

with open(os.path.join(model_dir, "diabetes_model.sav"), "rb") as file:
    diabetes_model = pickle.load(file)

with open(os.path.join(model_dir, "heart_model.sav"), "rb") as file:
    heart_model = pickle.load(file)

with open(os.path.join(model_dir, "parkinsons_model.sav"), "rb") as file:
    parkinsons_model = pickle.load(file)

                                   
with st.sidebar:
    selected= option_menu('prediction of disease outbreak system',['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using Ml')
    col1,col2,col3 = st.columns(3)
    with col1:
        pregnancies=st.text_input('Number of pregnancies')
    with col2:
        Glucose= st.text_input('Glucose level')
    with col3:
        Bloodpressure=st.text_input('Blood Pressure value')
    with col1:
        SkinThinkness = st.text_input('Skin Thinkness value')
    with col2:
        Insulin=st.text_input('Insulin level')
    with col3:
        BMI=st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age=st.text_input('Age of the person')

    diab_diagnosis=''
    if st.button('Diabetes Test Result'):
        user_input=[pregnancies , Glucose , Bloodpressure,SkinThinkness,Insulin,BMI,DiabetesPedigreeFunction,Age]
        user_input=[float(X) for X in user_input]
        diab_prediction=diabetes_model.predict([user_input])
        if diab_prediction[0]==1:
            diab_diagnosis='The person is diabetic'
        else:
            diab_diagnosis='The person is not diabetic'
    st.success(diab_diagnosis)





if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using Ml')
    col1,col2,col3 = st.columns(3)
    with col1:
        Age=st.text_input('Age')
    with col2:
        Sex= st.text_input('Sex')
    with col3:
        Chest_pain=st.text_input('Chest Pain Types')
    with col1:
        RestingBloodPressure = st.text_input('Resting Blood Pressure')
    with col2:
        Serum_Cholestoral=st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        FastingBloodPressure=st.text_input('Fasting Blood Sugar >120 mg/dl')
    with col1:
        RestingElectrocardiographic=st.text_input('Resting Electrocardiographic results')
    with col2:
        MaximumHeartRate=st.text_input('Maximum Heart Rate achieved')
    with col3:
        Exercise=st.text_input('Exercise Induced Angina')
    with col1:
        St_depression = st.text_input('ST depression induced by exercise')
    with col2:
        Slope=st.text_input('Slope of the peak exercise ST segment')
    with col3:
        Vessels_colour=st.text_input('Major vessels coloured by flouroscopy')
    with col1:
        Thal=st.text_input('thal:0 = normal; 1 = fixed defect; 2=reversable defect')

    heart_diagnosis=''
    if st.button('Heart Disease Test Result'):
        user_input=[Age,Sex,Chest_pain,RestingBloodPressure,Serum_Cholestoral,FastingBloodPressure,RestingElectrocardiographic,MaximumHeartRate,Exercise,St_depression,Slope,Vessels_colour,Thal]
        user_input=[float(X) for X in user_input]
        heart_prediction=heart_model.predict([user_input])
        if heart_prediction[0]==1:
            heart_diagnosis='The person is having heart disease'
        else:
            heart_diagnosis='The person is not having heart disease'
    st.success(heart_diagnosis)

        

if selected == 'Parkinsons Prediction':
    st.title("Parkinson's Disease Prediction using ML")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        MDVP1 = st.text_input('MDVP (Hz)', key="mdvp1")
    with col2:
        MDVP2 = st.text_input('MDVP  (Hz)', key="mdvp2")
    with col3:
        MDVP3 = st.text_input('MDVP   (Hz)', key="mdvp3")
    with col4:
        MDVP4 = st.text_input('MDVP  (%)', key="mdvp4")
    with col5:
        MDVP5 = st.text_input('MDVP  (Abs)', key="mdvp5")

    with col1:
        MDVP6 = st.text_input('MDVP', key="mdvp6")
    with col2:
        MDVP7 = st.text_input('MDVP', key="mdvp7")
    with col3:
        Jitter = st.text_input('Jitter', key="jitter")
    with col4:
        MDVP8 = st.text_input('MDVP', key="mdvp8")
    with col5:
        MDVP9 = st.text_input('MDVP (dB)', key="mdvp9")

    with col1:
        Shimmer1 = st.text_input('Shimmer', key="shimmer1")
    with col2:
        Shimmer2 = st.text_input('Shimmer', key="shimmer2")
    with col3:
        MDVP10 = st.text_input('MDVP', key="mdvp10")
    with col4:
        Shimmer3 = st.text_input('Shimmer', key="shimmer3")
    with col5:
        NHR = st.text_input('NHR', key="nhr")

    with col1:
        HNR = st.text_input('HNR', key="hnr")
    with col2:
        RPDE = st.text_input('RPDE', key="rpde")
    with col3:
        DFA = st.text_input('DFA', key="dfa")
    with col4:
        spread1 = st.text_input('Spread 1', key="spread1")
    with col5:
        spread2 = st.text_input('Spread 2', key="spread2")

    with col1:
        D2 = st.text_input('D2', key="d2")
    with col2:
        PPE = st.text_input('PPE', key="ppe")

    Parkinsons_diagnosis = ''
    if st.button("Parkinson's Disease Test Result"):
        user_input = [MDVP1, MDVP2, MDVP3, MDVP4, MDVP5, MDVP6, MDVP7, Jitter, MDVP8, MDVP9, 
                      Shimmer1, Shimmer2, MDVP10, Shimmer3, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        user_input = [float(X) for X in user_input]
        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            Parkinsons_diagnosis = "The person is having Parkinson's disease"
        else:
            Parkinsons_diagnosis = "The person is not having Parkinson's disease"

    st.success(Parkinsons_diagnosis)

        
# to run streamlit run web.py        