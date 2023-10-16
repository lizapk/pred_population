import streamlit as st
import pickle
import pandas as pd

# Muat model
model = pickle.load(open('global_population.sav','rb'))

# Buat prediksi
input_data = year = st.slider("Tentukan Tahun",1,30, step=1)
predictions = model.predict(input_data)

# Buat DataFrame untuk hasil prediksi
df = pd.DataFrame({'Input': input_data, 'Predicted': predictions})

# Tampilkan hasil prediksi dalam grafik garis
st.line_chart(df.set_index('Input'))

# Tambahkan judul
st.title('Hasil Prediksi dengan Grafik Garis')
