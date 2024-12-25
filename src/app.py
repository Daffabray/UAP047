import streamlit as st
import tensorflow as tf
from tensorflow.keras.utils import load_img, img_to_array
from pathlib import Path
import numpy as np
from PIL import Image

# Konfigurasi halaman aplikasi Streamlit
st.set_page_config(
    page_title="Klasifikasi Citra Batik",
    layout="wide",
)

# Header aplikasi
# st.title("Klasifikasi Citra Batik")
st.markdown(
    """
    <style>
        .title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
        }
    </style>
    <div class="title">
        Klasifikasi Citra Batik
    </div>
    """, 
    unsafe_allow_html=True
)

# Sidebar untuk memilih model
st.sidebar.subheader("Pilih Model")
available_models = ["Model VGG16", "Model CNN", "Keduanya"]
selected_model = st.sidebar.selectbox("Model yang digunakan:", available_models)

# Komponen pengunggah gambar
uploaded_file = st.file_uploader("Unggah gambar (format: PNG, JPG, JPEG):", type=['png', 'jpg', 'jpeg'])

# Fungsi untuk memuat model VGG16
@st.cache_resource
def load_vgg16():
    model_path = Path("model/vgg16_model.keras")
    return tf.keras.models.load_model(str(model_path))

# Fungsi untuk memuat model Custom CNN
@st.cache_resource
def load_custom():
    model_path = Path("model/cnn_model.keras")
    return tf.keras.models.load_model(str(model_path))

# Fungsi prediksi
@st.cache_data
def process_image(image, vgg16_model=None, custom_model=None):
    try:
        # Normalisasi gambar dan menyiapkan data
        img = load_img(image, target_size=(224, 224))
        img_array = img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Daftar label kategori
        categories = ['Buketan', 'Jlamprang', 'Liong', 'Mega_Mendung', 'Negatif', 'Singa_Barong', 'Tujuh_Rupa']

        predictions = []

        # Prediksi dengan model VGG16
        if vgg16_model:
            vgg16_output = vgg16_model.predict(img_array)
            vgg16_prob = tf.nn.softmax(vgg16_output[0])
            vgg16_top_class = np.argmax(vgg16_prob)
            predictions.append(("Model VGG16", categories[vgg16_top_class], float(vgg16_prob[vgg16_top_class])))

        # Prediksi dengan model Custom CNN
        if custom_model:
            custom_output = custom_model.predict(img_array)
            custom_prob = tf.nn.softmax(custom_output[0])
            custom_top_class = np.argmax(custom_prob)
            predictions.append(("Model CNN", categories[custom_top_class], float(custom_prob[custom_top_class])))

        return predictions

    except Exception as error:
        st.error(f"Terjadi kesalahan saat memproses gambar: {error}")
        return []

# Logika utama aplikasi
if st.button("Lakukan Prediksi"):
    if uploaded_file:
        try:
            col1, col2 = st.columns([1, 2])

            with col1:
                st.image(uploaded_file, caption="Gambar yang Diunggah", use_container_width=True)

            with col2:
                st.subheader("Hasil Prediksi")

                with st.spinner("Memuat model dan memproses gambar..."):
                    results = []

                    # Memuat model sesuai pilihan pengguna
                    if selected_model in ["Model VGG16", "Keduanya"]:
                        vgg16 = load_vgg16()
                        results.extend(process_image(uploaded_file, vgg16_model=vgg16))

                    if selected_model in ["Model CNN", "Keduanya"]:
                        custom = load_custom()
                        results.extend(process_image(uploaded_file, custom_model=custom))

                    for model, label, probability in results:
                        st.write(f"### {model}")
                        st.write(f"Prediksi: **{label}** ({probability:.2%})")

        except Exception as error:
            st.error(f"Terjadi kesalahan: {error}")
    else:
        st.warning("Harap unggah gambar terlebih dahulu!")

# Footer aplikasi


