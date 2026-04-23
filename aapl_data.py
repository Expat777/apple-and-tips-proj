import pandas as pd 
import streamlit as st
import matplotlib.pyplot as plt 
import seaborn as sns
import yfinance as yf




st.set_page_config(page_title='Инвест-борд эйпл', layout='wide')

st.title("Аналитика котировок Эйпл (AAPL)")


@st.cache_data
def load_data(period):
    ticker = yf.Ticker("AAPL")
    df = ticker.history(period=period)
    return df, ticker.info

st.sidebar.header('Настройки')
time_period = st.sidebar.selectbox(
    'Выберите период',
    options = ['1mo', '3mo', '6mo', '1y', '2y', '5y', 'max'],
    index=3,
    format_func=lambda x:{"1mo": "1 месяц", "3mo": "3 месяца", "6mo": "6 месяцев", 
                           "1y": "1 год", "2y": "2 года", "5y": "5 лет", "max": "Всё время"}[x]
)

data, info = load_data(time_period)
current_price = info.get('currentPrice', 0)
prev_close = info.get('previousClose', 0)
price_diff = current_price - prev_close

col1, col2, col3 = st.columns(3)
col1.metric('Текущая цена' , f"${current_price}", f"{price_diff:.2f} $")
col2.metric("РЫночная капитализацияб", f"{info.get('marketCap', 0) // 10**9}  млрд $")
col3.metric('Валюта', info.get('currency', 'USD'))

st.subheader(f'График зависимости за {time_period}')
st.line_chart(data['Close'])
with st.expander('Просмотреть сырые данные'):
    st.dataframe(data.sort_index(ascending=False))

    st.write('--')
    st.subheader(' about company')
    st.write(info.get('longBusnessSummary'))           