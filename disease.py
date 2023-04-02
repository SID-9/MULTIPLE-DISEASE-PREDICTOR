import pickle
import streamlit as st

heart_model = pickle.load(open("D:\streamlit\heart_disease\heart_disease_prediction.sav","rb"))
liver_model = pickle.load(open("D:\streamlit\heart_disease\liver_disease.sav","rb"))


# sidebar for navigation

nav = st.sidebar.radio("**NAVIGATION**",['WELCOME!!','HEART DISEASE PREDICTION','LIVER DISEASE PREDICTION'])

if(nav == 'WELCOME!!'):
    st.image("dpred.jpg")
    st.write("A disease predictor is used to predict the likelihood of an individual developing a particular disease or health condition based on their personal health data, medical history, and other relevant factors. ")
    st.write("The scope of a disease predictor is quite broad, and its application can have a significant impact on disease prevention and management, as well as overall public health.")

    
    


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ HEART DISEASE PREDICTION~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if(nav == "HEART DISEASE PREDICTION"):
    st.image("hpred.png")
    col1,col2,col3,col4 = st.columns(4)

    with col1:
        Age = st.text_input("Age : ")
    with col2:
        RestingBP = st.text_input("Resting BP : ")
    with col3:
        Cholestrol = st.text_input("Cholestrol : ")
    with col4:
        FastingBS = st.text_input("Fasting BS : ")
    with col1:
        MaxHR = st.text_input("Max HR : ")
    with col2:
        OldPeak = st.text_input("OldPeak : ")
    with col4:
        choice = st.radio("sex",['Male','Female'],index=1)
        if(choice == 'Male'):
            sex_f = 0
            sex_m = 1
        else:
            sex_f = 1
            sex_m = 0
    with col1:
        choice1 = st.radio("chest pain type ",['ASY','ATA','NAP','TA'],index=1)
        if(choice1 == "ASY"):
            cpt_ASY = 1
            cpt_NAP = 0
            cpt_ta = 0
            cpt_ATA = 0
        if(choice1 == "NAP"):
            cpt_ASY = 0
            cpt_NAP = 1
            cpt_ta = 0
            cpt_ATA = 0
        if(choice1 == "TA"):
            cpt_ASY = 0
            cpt_NAP = 0
            cpt_ta = 1
            cpt_ATA = 0
        if(choice1 == "ATA"):
            cpt_ASY = 0
            cpt_NAP = 0
            cpt_ta = 0
            cpt_ATA = 1
            
    with col2:
        choice3 = st.radio("Resting ECG",['LVH',"Normal","ST"],index=1)
        if(choice3 == "LVH"):
            recg_LVH = 1
            recg_N = 0
            recg_ST = 0
        if(choice3 == "Normal"):
            recg_LVH = 0
            recg_N = 1
            recg_ST = 0
        if(choice3 == "ST"):
            recg_LVH = 0
            recg_N = 0
            recg_ST = 1

    with col3:
        choice4 = st.radio("Exercise Angina",['NO','YES'],index=1)
        if(choice4 == "NO"):
            ea_NO = 1
            ea_YES = 0
        if(choice4 == "YES"):
            ea_NO = 0
            ea_YES = 1

    with col4:
        choice5 = st.radio("ST Slope ",['down','flat','up'],index=1)
        if(choice5 == "down"):
            st_d = 1
            st_f = 0
            st_up = 0
        if(choice5 == "flat"):
            st_d = 0
            st_f = 1
            st_up = 0
        if(choice5 == "up"):
            st_d = 0
            st_f = 0 
            st_up = 1

    diagnosis = ''
    if(st.button("heart disease test result")):
        heart_predict = heart_model.predict([[Age,RestingBP,Cholestrol,FastingBS,MaxHR,OldPeak,sex_f,sex_m,cpt_ASY,cpt_ATA,cpt_NAP,cpt_ta,recg_LVH,recg_N,recg_ST,ea_NO,ea_YES,st_d,st_f,st_up]])
        if(heart_predict[0] == 1):
            diagnosis = "heart disease found "
        else:
            diagnosis = "no heart disease"

    st.success(diagnosis)   


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ LIVER DISEASE PREDICTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if(nav == 'LIVER DISEASE PREDICTION'):
    st.image('liverpred.jpg')
    col1,col2,col3 = st.columns(3)

    with col1:
        Age = st.text_input("Age")
    with col2:
        g = st.radio("gender",["Male","Female"])
        if(g == "Male"):
            Gender = 0
        if(g == "Female"):
            Gender = 1

    with col3:
        Total_Bilirubin = st.text_input("Total_Bilirubin : ")
    with col1:
        Direct_Bilirubin = st.text_input("Direct_Bilirubin : ")
    with col2:
        Alkaline_Phosphotase = st.text_input("Alkaline_Phosphotase : ")
    with col3:
        Alamine_Aminotransferase = st.text_input("Alamine_Aminotransferase : ")
    with col1:
        Aspartate_Aminotransferase = st.text_input("Aspartate_Aminotransferase : ")
    with col2:
        Total_Protiens = st.text_input("Total_Protiens : ")
    with col3:
        Albumin = st.text_input("Albumin : ")
    with col1:
        Albumin_and_Globulin_Ratio = st.text_input("Albumin_and_Globulin_Ratio : ")

    diag = ' '
    if(st.button("test result")):
        liver_predict = liver_model.predict([[Age,Gender,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin,Albumin_and_Globulin_Ratio]])
        if(liver_predict[0]==2):
            diag = "liver disease found"
        else:
            diag = "no liver disease found"
    st.success(diag)

