import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

with st.sidebar :
    selected = option_menu ('MATEMATIKA',
    ['Hitung Aritmatika',
     'Hitung Pangkat',],
    default_index=0)

if (selected == 'Hitung Aritmatika') :
    st.title('Hitung Aritmatika')

    nilai_a = st.number_input ("Masukkan nilai a", 0)
    nilai_n = st.number_input ("Masukkan nilai n", 0)
    nilai_d = st.number_input ("Masukkan nilai d", 0)
    hitung = st.button ("Hitung Deret")

    if hitung : 
        jumlah = (nilai_n/2) * (2*nilai_a + (nilai_n-1)*nilai_d)
        st.write ("Hasil perhitungan deret ", jumlah)

if (selected == 'Hitung Pangkat') :
    st.title('Hitung Pangkat')

    angka = st.number_input ("Masukkan angka", 0)
    pangkat = st.number_input ("Masukkan pangkat", 0)
    hitung = st.button ("Hitung Pangkat")

    if hitung :
        hasil = angka ** pangkat
        st.write ("Hasil perhitungan pangkat ", hasil)
