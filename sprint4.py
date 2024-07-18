import pandas as pd # type: ignore
import streamlit as st # type: ignore
import plotly.express as px # type: ignore
import altair as alt # type: ignore

df_cars = pd.read_csv(r'https://github.com/DC89/sprint4pjkt/blob/main/vehicles_us.csv')

df_cars['model_year'] = df_cars['model_year'].fillna(0) #subs NaN values for zero so we can chart them

df_carsNew = df_cars.drop(df_cars[df_cars['model_year'] <= 1999.0].index) #new df with only "new" (< 20 years old) cars
fig2 = px.histogram(df_carsNew, x='model_year')
fig3 = px.scatter(x=df_carsNew['model_year'], y=df_carsNew['days_listed']) 

df_carsClassic = df_cars.drop(df_cars[(df_cars['model_year'] > 1999.0) | (df_cars['model_year'] == 0)].index) #looks for cars older than 1999 excluding values of zero
fig4 = px.histogram(df_carsClassic, x='model_year')
fig5 = px.scatter(x=df_carsClassic['model_year'], y=df_carsClassic['days_listed'])
st.header('Classic cars vs. New Cars', divider='red')


check0 = st.checkbox('Classics instead of New', key='daysListed') #checkbox to swap between classic cars and new cars scatterplots
st.write(check0)

if check0:
    st.write(fig5)
else:
    st.write(fig3)

check1 = st.checkbox('Classics instead of New', key='quantityOnLot') #checkbox to switch between classic cars and new car histograms
st.write(check1)

if check1:
    st.write(fig4)
else:
    st.write(fig2)
