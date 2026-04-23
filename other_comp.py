import pandas as pd 
import streamlit as st
import matplotlib.pyplot as plt 
import seaborn as sns
import yfinance as yf
# Список компаний для выбора
companies = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Сбербанк": "SBER.ME",
    "Газпром": "GAZP.ME",
    "NVIDIA": "NVDA",
    "Tesla": "TSLA"
}

st.sidebar.header('Настройки')

# 1. Выбор компании
selected_company_name = st.sidebar.selectbox("Выберите компанию:", list(companies.keys()))
selected_ticker = companies[selected_company_name]

# 2. Выбор периода (ваш старый код)
time_period = st.sidebar.selectbox(
    'Выберите период',
    options = ['1mo', '3mo', '6mo', '1y', '5y'],
    index=3
)

# 3. Обновленная функция загрузки (принимает тикер)
@st.cache_data
def load_data(ticker_code, period):
    ticker = yf.Ticker(ticker_code)
    df = ticker.history(period=period)
    return df, ticker.info

data, info = load_data(selected_ticker, time_period)

# В st.title теперь будет подставляться имя выбранной компании
st.title(f"Аналитика котировок {selected_company_name}")