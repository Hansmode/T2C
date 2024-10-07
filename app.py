import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title("Dashboard Bike Sharing Data Visualization")


    customers_df = pd.read_csv("https://raw.githubusercontent.com/Hansmode/T2B/refs/heads/main/day.csv")

    st.subheader('Rata-rata Jumlah Peminjam Sepeda Berdasarkan Musim')
    customer_season = customers_df.groupby(by="season")["cnt"].mean().reset_index()

    pic1, ax1 = plt.subplots(figsize=(10, 6))
    sns.barplot(x="season", y="cnt", data=customer_season, palette="Blues", ax=ax1)
    ax1.set_title('Rata-rata Jumlah Peminjam Sepeda Berdasarkan Musim', fontsize=14)
    ax1.set_xlabel('Musim', fontsize=12)
    ax1.set_ylabel('Rata-rata Jumlah Peminjam', fontsize=12)
    ax1.set_xticklabels(['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin'])  
    ax1.grid(True)

    st.pyplot(pic1)

    st.subheader('Total Peminjam Terdaftar Berdasarkan Tahun')
    registered_year = customers_df.groupby(by="yr")["registered"].sum().reset_index()

    pic2, ax2 = plt.subplots(figsize=(10, 6))
    sns.barplot(x='yr', y='registered', data=registered_year, palette='Blues', ax=ax2)
    ax2.set_title('Total Peminjam Terdaftar Berdasarkan Tahun', fontsize=16)
    ax2.set_xlabel('Tahun', fontsize=12)
    ax2.set_ylabel('Total Peminjam Terdaftar', fontsize=12)
    ax2.set_xticklabels(['2011', '2012']) 

    st.pyplot(pic2)

if __name__ == "__main__":
    main()
