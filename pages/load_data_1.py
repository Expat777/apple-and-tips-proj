import pandas as pd 
import streamlit as st
import matplotlib.pyplot as plt 
import seaborn as sns
import yfinance as yf

uploaded_file = st.file_uploader(
    'Загрузите файл в формате CSV',
    type = ['csv']
)
if uploaded_file:
    df = pd.read_csv(uploaded_file)