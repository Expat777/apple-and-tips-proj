import pandas as pd 
import streamlit as st
import matplotlib.pyplot as plt 
import seaborn as sns
import yfinance as yf

st.set_page_config(page_title='Анализ чаевых', layout='wide')
st.title('Анализ чаевых ил локальногго файла')

@st.cache_data
def load_custom_data(file_path):
    df = pd.read_csv(file_path)
    return df

file_name='tips.csv'

try:
    df = load_custom_data(file_name)
    st.sidebar.success(f"Файл '{file_name}' успешно загружен")

    selected_sex = st.sidebar.multiselect(
        'Выберете пол :',
        options  = df['sex'].unique(),
        default = df['sex'].unique() 
    )
    filtered_df = df[df['sex'].isin(selected_sex)]

    col1,col2,col3 = st.columns(3)
    col1.metric("Всего строк", len(filtered_df))
    col2.metric("Суммарный чек", f"${filtered_df['total_bill'].sum():.2f}")
    col3.metric("Средний %  чаевых", f"{(filtered_df['tip'] / filtered_df['total_bill']).mean()*100:.1f}%")


    st.subheader('Анализ Данных')

    fig, ax =plt.subplots(figsize=(10, 5))
    sns.regplot(data=filtered_df, x='total_bill', y='tip',scatter_kws={"alpha":0.5}, ax=ax)
    ax.set_title('Линия тренда : Чек против Чаевых')
    st.pyplot(fig)

    st.subheader('Сырые данные')
    st.dataframe(filtered_df, use_container_width=True)

except FileNotFoundError:
    st.error(f"❌ Файл '{file_name}' не найден в папке с программой!")
    st.info("Пожалуйста, убедись, что файл лежит в той же папке, что и твой .py скрипт.")

