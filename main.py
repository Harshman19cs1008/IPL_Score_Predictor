# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 17:42:59 2023

@author: HARSH
"""

import streamlit as st
import pandas as pd
import pickle
with open("model_pickle",'rb')as f:
    pipe=pickle.load(f)
st.title("IPL Score Predictor")
team=['Royal Challengers Bangalore', 'Sunrisers Hyderabad',
       'Delhi Capitals', 'Chennai Super Kings', 'Kolkata Knight Riders',
       'Punjab Kings', 'Rajasthan Royals', 'Mumbai Indians']
col1, col2 = st.columns(2)
with col1:
   BattingTeam=st.selectbox('Batting Team',sorted(team))
with col2:
   BowlingTeam= st.selectbox("Bowling Team", sorted(team))
cities=['Ahmedabad', 'Mumbai', 'Navi Mumbai', 'Pune', 'Dubai', 'Sharjah',
       'Abu Dhabi', 'Delhi', 'Chennai', 'Hyderabad', 'Visakhapatnam',
       'Chandigarh', 'Bengaluru', 'Kolkata', 'Jaipur', 'Indore',
       'Bangalore', 'Raipur', 'Ranchi', 'Cuttack', 'Dharamsala', 'Nagpur',
       'Johannesburg', 'Centurion', 'Durban', 'Bloemfontein',
       'Port Elizabeth', 'Kimberley', 'East London', 'Cape Town']
City = st.selectbox('Select city',sorted(cities))

col3,col4,col5 = st.columns(3)

with col3:
    Current_Score = st.number_input('Current Score')
with col4:
    overs = st.number_input('Overs done(works for over>5)')
with col5:
    wickets = st.number_input('Wickets out')

last_five = st.number_input('Runs scored in last 5 overs')

if st.button('Predict Score'):
    Balls_left = 120 - (overs*6)
    Wicket_left = 10 -wickets
    crr = Current_Score/overs

    input_df = pd.DataFrame(
     {'BattingTeam': [BattingTeam], 'BowlingTeam': [BowlingTeam],'City':City, 'Current_Score': [Current_Score],'Balls_left': [Balls_left], 'Wicket_left': [Wicket_left], 'crr': [crr], 'last_five': [last_five]})
    result = pipe.predict(input_df)
    st.header("Predicted Score - " + str(int(result[0])))