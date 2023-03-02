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
with cent_co:
    st.image("https://i2.wp.com/ummah-futures.net/wp-content/uploads/2019/12/%D8%A7%D9%84%D9%84%D8%AC%D9%86%D8%A9-%D8%A7%D9%84%D8%A7%D9%82%D8%AA%D8%B5%D8%A7%D8%AF%D9%8A%D8%A9-%D9%88%D8%A7%D9%84%D8%A7%D8%AC%D8%AA%D9%85%D8%A7%D8%B9%D9%8A%D8%A9-%D9%84%D8%BA%D8%B1%D8%A8%D9%8A-%D8%A2%D8%B3%D9%8A%D8%A7-1.jpg?w=500&ssl=1")
    
left_col, center_co = st.columns([1,4])
with center_co:
    st.title(""" "اســتـبـيـان "المجتمع العربي: مجموعة الاحصاءات والمؤشرات الاجتماعية""")    
    
#Welcome Message 


st.write('## "This dashboard allows the instructors to visually moniter that performance of students using several metrics and across multiple attributes" ')
# streamlit expander, useful if mor info is wanted about something but
# you dont want to clutter the page up
st.write("### Quick Guide: You can check students performance across the attributes by selecting the attribute from the side bar on the left, and read more info about the dataset and see a sample using the buttons below:")
with st.expander("Click for more information on the student performence dataset:"):
    st.write("The student performence data set is a multivariate data set that represents students scores across 3 subjects, Math, reading, and writing, and ever student belongs to one of the 5 groups: A, B, C, D, or E")
    st.write("The data set consists of 990 students.")


