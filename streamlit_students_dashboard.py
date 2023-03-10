#import the required libraries 

import streamlit as st
import pandas as pd
import numpy as np 
import plotly.express as px  
import json
from streamlit_lottie import st_lottie


st.set_page_config(
    page_title="اســتـبـيـان المجتمع العربي",
    page_icon= "🇺🇳",
    layout='wide'
)

st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)


#defining lottie function to visualize animated pictures
def load_lottiefile(filepath: str):
    with open(filepath) as f:
        return json.load(f)


left_co, cent_co,last_co = st.columns(3)
with last_co:
    st.image("https://i2.wp.com/ummah-futures.net/wp-content/uploads/2019/12/%D8%A7%D9%84%D9%84%D8%AC%D9%86%D8%A9-%D8%A7%D9%84%D8%A7%D9%82%D8%AA%D8%B5%D8%A7%D8%AF%D9%8A%D8%A9-%D9%88%D8%A7%D9%84%D8%A7%D8%AC%D8%AA%D9%85%D8%A7%D8%B9%D9%8A%D8%A9-%D9%84%D8%BA%D8%B1%D8%A8%D9%8A-%D8%A2%D8%B3%D9%8A%D8%A7-1.jpg?w=500&ssl=1")
with left_co:
    st.image("https://www.unescwa.org/sites/default/files/images/flags/Flag_of_Bahrain.svg")
st.image("title.PNG")


leftt_co, centt_co,lastt_co = st.columns([1,1,2])
with lastt_co :
    st.title('البحرين')
    st.image("SUB HEADER.PNG")
    
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col1:
    st.write("[Population - السكان]()")

with col2:
    st.write("[Labor - العمالة](https://docs.google.com/spreadsheets/d/1UGEiAmFwx7iiY1WV1s7l0TFz08pQPGju/edit?usp=sharing&ouid=100083186149459779256&rtpof=true&sd=true)")
with col3:
    st.write("[Poverty - الفقر]()")
with col4:
    st.write("[Education - التعليم]()")
with col5:
    st.write("[Culture - الثقافة]()")
with col6:
    st.write("[Health - الصحة]()")
with col7:
    st.write("[Housing Conditions - المساكن]()")   
    

#edit footer
page_style= """
    <style>
    footer{
        visibility: visible;
        }
    footer:after{
        content: 'Developed by Ali Maatouk - ESCWA Statistics, Information Society and Technology Cluster';
        display:block;
        position:relative;
        color:#1e54e4;
    }
    </style>"""

st.markdown(page_style, unsafe_allow_html=True)
