#import the required libraries 

import streamlit as st
import pandas as pd
import numpy as np 
import plotly.express as px  

st.set_page_config(
    page_title="اســتـبـيـان المجتمع العربي",
    page_icon= "🇺🇳",
    layout='wide'
)

left_co, cent_co,last_co = st.columns(3)
with last_co:
    st.image("https://i2.wp.com/ummah-futures.net/wp-content/uploads/2019/12/%D8%A7%D9%84%D9%84%D8%AC%D9%86%D8%A9-%D8%A7%D9%84%D8%A7%D9%82%D8%AA%D8%B5%D8%A7%D8%AF%D9%8A%D8%A9-%D9%88%D8%A7%D9%84%D8%A7%D8%AC%D8%AA%D9%85%D8%A7%D8%B9%D9%8A%D8%A9-%D9%84%D8%BA%D8%B1%D8%A8%D9%8A-%D8%A2%D8%B3%D9%8A%D8%A7-1.jpg?w=500&ssl=1")
with left_co:
    st.image("https://cdn.britannica.com/67/5767-004-E0FF7201/Flag-Bahrain.jpg")
with cent_co:
    st.title("               Bahrain - البحرين")
    
    
left_col, center_co = st.columns([1,4])
with center_co:
    st.title(""" 17 - "اســتـبـيـان "المجتمع العربي: مجموعة الاحصاءات والمؤشرات الاجتماعية""")

leftt_co, centt_co,lastt_co = st.columns([1,1,2])
with lastt_co :
        st.write('## الرجاء اختيار موضوع الاستبان عبر الضغط على الأزرار ادناه ')

#Welcome Message 


