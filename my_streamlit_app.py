import streamlit as st

st.title('Hello Wilders, welcome to my application!')

st.write("I enjoy to discover streamlit possibilities")

name = st.text_input("Please give me your name :")
name_length = len(name)
st.write("Your name has ",name_length,"characters")

#je tente un widget

icecream = st.radio("What's your favourite icecream flavour ?", ("Chocolate", "Vanilla", "Strawberry"))
if icecream == "Chocolate":
    st.write("Chocolate ! You're right ! It's chocolate icecream or nothing.")
else :
    st.write("Pffff, you don't understand anything about life")



import pandas as pd
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)
df_weather

st.line_chart(df_weather['MAX_TEMPERATURE_C'])

# exemple avec seaborn

import seaborn as sns
viz_correlation = sns.heatmap(df_weather.corr(), center=0, cmap = sns.color_palette("vlag", as_cmap=True))
st.pyplot(viz_correlation.figure)

# tentative avec plotly

st.write("J'essaie avec plotly")
import plotly.express as px
viz_bubble = px.scatter(data_frame = df_weather, x= "DATE", y="MAX_TEMPERATURE_C",size='PRECIP_TOTAL_DAY_MM',color='PRECIP_TOTAL_DAY_MM', color_continuous_scale='agsunset')
viz_bubble.update_layout(title_text='Max Temperatures and Precipitations', title_x=0.5)
viz_bubble.update_xaxes(title_text='Dates')
viz_bubble.update_yaxes(title_text='Temperatures (celsius)')
st.plotly_chart(viz_bubble)




