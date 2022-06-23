#!/usr/bin/env python
# coding: utf-8
from pycaret.regression import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np


model= load_model('Final Lightgbm Model 22June2022')

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions

def run():

    st.write("""

    # Explainable Ensemble ML-based Practical Bond Strength Prediction App For SRC Structures

    
    """)
    #st.write("""

    ## ML-based Practical Bond Strength Prediction App For SRC Structures

    #This app predicts the **Bond strength** between H-steel section and concrete!
 
    #""")
    st.write('This app predicts the **Bond strength** between H-steel section and concrete!')
    
    from PIL import Image
    image = Image.open('LightGBM.png')

    st.image(image, width=1050)#,use_column_width=False)
    
    st.sidebar.header('User Input Parameters')
    
    cover_thickness	= st.sidebar.slider('Concrete cover, cs (mm) ', 20, 200, 90)

    side_cover= st.sidebar.slider('Side cover, cv (mm) ', 35, 230, 85)

    steel_section_height= st.sidebar.slider('Height of steel section, hs (mm) ', 100, 900, 320)

    steel_section_width= st.sidebar.slider('Width of steel section, tf(mm) ', 70, 300, 130)

    bonded_length= st.sidebar.slider('Bonded length, lb (mm) ', 150, 1500, 540)

    tensile_strength= st.sidebar.slider('Tensile strength of concrete, ft(MPa)', 2.0, 6.0, 3.54)

    steel_section_ratio= st.sidebar.slider('Steel section ratio, ' +chr(961)+'s (%)', 1.2, 10.7, 4.57)

    transverse_hoop_ratio= st.sidebar.slider('Transverse hoop ratio, ' +chr(961)+'sv (%)', 0.0, 2.5, 0.54)

    surface_treatment= st.selectbox('Surface treatment',['Normal rust and mill scale', 'Sandblasted','Blast-cleaned with TSP','Derusted and polished','Checkered pattern','Corrosion'])

    concrete_type= st.selectbox('Concrete type',['NC', 'SFRC','RAC','LAC','ECC','HSC'])

    input_dict = {'Relative bonded length': bonded_length/steel_section_height, 'Relative concrete cover': cover_thickness/steel_section_height, 
          'Relative  side cover' :side_cover/steel_section_height, 'Relative steel section width': steel_section_width/steel_section_height, 
          'ST':surface_treatment,'Concrete type':concrete_type,'Tensile strength':tensile_strength,
          'Steel section ratio':steel_section_ratio/100,'Transverse hoop ratio':transverse_hoop_ratio/100 
                 }
    input_df = pd.DataFrame([input_dict])    
    
    if st.button("Predict"):
       output = predict(model=model, input_df=input_df)
       output = round(output, 3)
       output =  str(output) +'MPa'

       st.success('**The bond strength is  :  {}**'.format(output))
    st.info('***Written by Dr. Xianlin Wang,  Department of bridge engineering,  Tongji University,  E-mail:1810747@tongji.edu.cn***')
       
    #output = predict(model=model, input_df=input_df)    
    
    #st.write(output)
        
if __name__ == '__main__':
    run()
