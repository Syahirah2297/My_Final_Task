import streamlit as st
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
from PIL import Image

model= pd.load_model(https://raw.githubusercontent.com/Syahirah2297/My_Final_Task/main/NBA_season1718_salary.csv)

X = model.drop('label', axis = 1)
X.head()
y = data['label']
y.head()

model = RandomForestClassifier()
model.fit(X, Y)

streamlit.title('Salary Prediction for NBA players 2017-2018')
streamlit.sidebar.header('Player Data')
image = Image.open('nba2k20.jpg')
streamlit.image(image,'')

def user_details():
    country = streamlit.sidebar.selectbox('Country: USA (3) ,CAN (1), AUS (0), Others (2)',('3','2','1','0'))
    jersey = streamlit.sidebar.number_input('Jersey Number', 0,100, 1 )
    team = streamlit.sidebar.slider('Team', 0,30, 1 )
    position = streamlit.sidebar.slider('Position', 0,10, 1 )
    rating = streamlit.sidebar.slider('Rating', 50,100, 1 )
    draft_year = streamlit.sidebar.slider('Draft Year', 2000,2020, 2000)
    draft_round = streamlit.sidebar.slider('Draft Round', 1,10, 1)
    draft_peak = streamlit.sidebar.slider('Draft Peak', 1,30, 1)

    user_details_data = {
        'country':country,
        'jersey':jersey,
        'team':team,
        'position':position,
        'rating':rating,
        'draft_year':draft_year,
        'draft_round':draft_round,
        'draft_peak':draft_peak
    }
    player_details = pd.DataFrame(user_details_data, index=[0])
    return player_details

user_data = user_details()
streamlit.header('Player Data')
streamlit.write(user_data)

salary = model.predict(user_data)
streamlit.subheader('Estimation Salary of The Player')
streamlit.subheader('$'+str(np.round(salary[0], 2)))

streamlit.write("""
This app predict the **Salary of NBA Player 2017-2018* based on the data obtained from https://www.kaggle.com/isaienkov/nba2k20-player-dataset in Kaggle.
""")

   
