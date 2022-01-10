import streamlit as st
import pandas as pd
st.title('Dataset de voiture')
url = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
cars = pd.read_csv(url)
st.header("Dataset : ")

continent = st.radio("Choix de la zone géographique pour l'affichage du df", ("US", "Europe", "Japon"))
if continent == "US":
    cars[cars['continent'].str.contains('US.')]
    st.write('Voici le dataset filtré sur les US')
    st.write('Il contient',len(cars[cars['continent'].str.contains('US.')]),'des',len(cars),'voitures du dataset.')
elif continent == "Europe" :
    cars[cars['continent'].str.contains('Europe.')]
    st.write("Voici le dataset filtré sur l'Europe")
    st.write('Il contient', len(cars[cars['continent'].str.contains('Europe')]), 'des', len(cars), 'voitures du dataset.')
elif continent == "Japon":
    cars[cars['continent'].str.contains('Japan.')]
    st.write('Voici le dataset filtré sur le Japon.')
    st.write('Il contient', len(cars[cars['continent'].str.contains('Japan.')]), 'des', len(cars), 'voitures du dataset.')
import seaborn as sns

st.header("Les corrélations : ")

continent2 = st.radio("Choix de la zone géographique pour la heatmap de corrélations", ("US", "Europe", "Japon"))
if continent2 == "US":
    hm_cars = sns.heatmap(cars[cars['continent'].str.contains('US.')].corr(), center=0, cmap=sns.color_palette("vlag", as_cmap=True))
    st.pyplot(hm_cars.figure, clear_figure = True)
    st.write('Voici la heatmap filtré sur les US.')
elif continent2 == "Europe" :
    hm_cars2 = sns.heatmap(cars[cars['continent'].str.contains('Europe.')].corr(), center=0, cmap=sns.color_palette("vlag", as_cmap=True))
    st.pyplot(hm_cars2.figure, clear_figure = True)
    st.write("Voici la heatmap filtrée sur l'Europe.")
elif continent2 == "Japon":
    hm_cars3 = sns.heatmap(cars[cars['continent'].str.contains('Japan.')].corr(), center=0, cmap=sns.color_palette("vlag", as_cmap=True))
    st.pyplot(hm_cars3.figure, clear_figure = True)
    st.write("Voici la heatmap filtrée sur le Japon.")


st.header("Le nombre de cylindres : ")

continent3 = st.radio("Choix de la zone géographique pour afficher les voitures selon leur cylindre", ("US", "Europe", "Japon"))
if continent3 == "US":
    #bc =st.bar_chart(cars[cars['continent'].str.contains('US.')]['cylinders'])
    #st.bar_chart(bc)
    dp_cars = sns.countplot(cars[cars['continent'].str.contains('US.')]['cylinders'])
    st.pyplot(dp_cars.figure)
    st.write('Voici le graphique filtré sur les US.')
    st.write('Le nombre moyen de cylindres est :', round(cars[cars['continent'].str.contains('US.')]['cylinders'].mean(),2))
elif continent3 == "Europe" :
    dp_cars2 = sns.countplot(cars[cars['continent'].str.contains('Europe.')]['cylinders'])
    st.pyplot(dp_cars2.figure)
    st.write("Voici le graphique filtré sur l'Europe.")
    st.write('Le nombre moyen de cylindres est :', round(cars[cars['continent'].str.contains('Europe.')]['cylinders'].mean(),2))
elif continent3 == "Japon":
    dp_cars3 = sns.countplot(cars[cars['continent'].str.contains('Japan.')]['cylinders'])
    st.pyplot(dp_cars3.figure)
    st.write("Voici le graphique filtré sur le Japon.")
    st.write('Le nombre moyen de cylindres est :', round(cars[cars['continent'].str.contains('Japan.')]['cylinders'].mean(),2))


st.header("Poids, hp et mpg")
import plotly.express as px
continent4 = st.selectbox("Choix de la zone géographique pour afficher les voitures selon leur poids,hp et mpg", ("US", "Europe", "Japon"))
if continent4 == "US":
    viz_bubble = px.scatter(data_frame = cars[cars['continent'].str.contains('Japan.')], x= 'weightlbs', y='hp',size='mpg',color='mpg', color_continuous_scale='agsunset')
    viz_bubble.update_layout(title_text='Poids,hp et mpg', title_x=0.5)
    viz_bubble.update_xaxes(title_text='Poids')
    viz_bubble.update_yaxes(title_text='Hp')
    st.plotly_chart(viz_bubble)
elif continent4 == "Europe":
    viz_bubble2 = px.scatter(data_frame = cars[cars['continent'].str.contains('Europe')], x= 'weightlbs', y='hp',size='mpg',color='mpg', color_continuous_scale='agsunset')
    viz_bubble2.update_layout(title_text='Poids,hp et mpg', title_x=0.5)
    viz_bubble2.update_xaxes(title_text='Poids')
    viz_bubble2.update_yaxes(title_text='Hp')
    st.plotly_chart(viz_bubble2)
elif continent4 == "Japon":
    viz_bubble3 = px.scatter(data_frame = cars[cars['continent'].str.contains('Japan.')], x= 'weightlbs', y='hp',size='mpg',color='mpg', color_continuous_scale='agsunset')
    viz_bubble3.update_layout(title_text='Poids,hp et mpg', title_x=0.5)
    viz_bubble3.update_xaxes(title_text='Poids')
    viz_bubble3.update_yaxes(title_text='Hp')
    st.plotly_chart(viz_bubble3)




