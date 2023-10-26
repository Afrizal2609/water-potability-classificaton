import streamlit as st
import joblib

# Memuat model yang telah dilatih
model = joblib.load('model_random_forest.pkl')
scaler = joblib.load('scaler.pkl')

# Menambahkan judul ke aplikasi
st.title("Prediksi Kelayakan Air Minum")

# Menambahkan deskripsi dan informasi tentang variabel
st.write("Model Random Forest dengan Akurasi 71%")
st.write("Berikut adalah beberapa variabel yang digunakan untuk memprediksi kelayakan air minum:")
st.write("- pH value (Nilai pH): Mengukur tingkat keasaman atau kebasaan air.")
st.write("- Hardness (Kekerasan): Terkait dengan kandungan kalsium dan magnesium.")
st.write("- Solids (Total dissolved solids - TDS): Jumlah mineral dan garam yang larut dalam air.")
st.write("- Chloramines (Kloramina): Kadar klorin dalam air minum.")
st.write("- Sulfate (Sulfat): Konsentrasi sulfat dalam air.")
st.write("- Conductivity (Konduktivitas): Kemampuan air menghantarkan arus listrik.")
st.write("- Organic Carbon (Karbon Organik): Jumlah karbon dalam senyawa organik dalam air.")
st.write("- Trihalomethanes (Trihalometana): Kadar THM dalam air minum.")
st.write("- Turbidity (Kekeruhan): Kandungan materi padat dalam air.")
st.write("- Potability (Kelayakan): Menunjukkan apakah air aman untuk dikonsumsi.")

# Membuat input untuk pengguna
st.sidebar.header("Masukkan Nilai Variabel")
pH = st.sidebar.number_input("pH value", min_value=0.0, max_value=14.0, value=7.0)
hardness = st.sidebar.number_input("Hardness", min_value=0.0, value=100.0)
solids = st.sidebar.number_input("Total Dissolved Solids (TDS)", min_value=0.0, value=200.0)
chloramines = st.sidebar.number_input("Chloramines", min_value=0.0, value=4.0)
sulfate = st.sidebar.number_input("Sulfate", min_value=0.0, value=10.0)
conductivity = st.sidebar.number_input("Conductivity", min_value=0.0, value=500.0)
organic_carbon = st.sidebar.number_input("Organic Carbon", min_value=0.0, value=5.0)
trihalomethanes = st.sidebar.number_input("Trihalomethanes", min_value=0.0, value=20.0)
turbidity = st.sidebar.number_input("Turbidity", min_value=0.0, value=5.0)

# Membuat prediksi saat tombol dipencet
if st.sidebar.button("Prediksi Potabilitas"):
    # Membuat dataframe dari input pengguna
    input_data = [[pH, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]]

    scaled_data = scaler.transform(input_data)

    # Melakukan prediksi potabilitas dengan model
    prediction = model.predict(scaled_data)

    # Menampilkan hasil prediksi
    if prediction[0] == 1:
        st.success("Air diprediksi DAPAT diminum.")
    else:
        st.warning("Air diprediksi TIDAK DAPAT diminum.")