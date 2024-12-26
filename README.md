# Klasifikasi Batik Menggunakan VGG16 dan CNN

## Deskripsi Proyek

Proyek ini bertujuan untuk mengembangkan aplikasi web yang dapat memprediksi klasifikasi batik. Pada progam ini menggunakan dataset batik yang terbagi menjadi 7 kelas yaitu Buketan, Jlamprang, Liong, Mega Mendung, Negatif, singa Barong, dan Tujuh Rupa. Datset terdiri dari 3.629 data. 

Model yang digunakan CNN (Convolutional Neural Network) dan VGG 16

## Depedensi
**Streamlit** Digunakan untuk membangun aplikasi WEB

**Tensorflow dan Keras** Untuk pengembangan dan pelatihan model machine learning dan deep learning

**Matplotlib.pyplot** Untuk membuat visualisasi data, seperti grafik dan plot

**Import Os** Untuk Mengelola file

**Import Numpy** Untuk mengelola dan melakukan komputasi numerik pada array

**Import Gdown** Untuk Instal file pada Gdrive

## Preprocessing dan Modelling

**Preprocessing**

Gambar akan diputar secara acak hingga 20 derajat, Gambar dapat digeser secara horizontal, Gambar digeser secara vertikal hingga 10% dari tinggi gambar, Memiringkan gambar 10%, Gambar akan diperkecil atau diperbesar secara acak hingga 10%.

**Modelling** 
Model yang digunakan yaitu VGG16 dan CNN

**Grafik Analisa**

![Grafik VGG16](https://github.com/Daffabray/UAP047/blob/main/Grafik%20Akurasi/vgg16.png)

**Grafik VGG16**

Accuracy: Training Accuracy cepat mencapai 1, Validation Accuracy tinggi dan stabil.

Loss: Training Loss turun drastis mendekati 0, Validation Loss rendah dan stabil.

![Grafik CNN](https://github.com/Daffabray/UAP047/blob/main/Grafik%20Akurasi/cnn.png)

**Grafik CNN**

Accuracy: Training dan Validation Accuracy meningkat konsisten, menunjukkan model belajar dan generalisasi dengan baik.

Loss: Training dan Validation Loss menurun signifikan dengan perbedaan kecil, menandakan tidak ada overfitting.

**Perbandingan**

VGG16 lebih cepat mencapai akurasi tinggi dan loss rendah.

CNN lebih stabil dan fleksibel, cocok untuk penyesuaian kasus tertentu.


**Hasil Klasifikasi**

![Kalsifikasi Report](https://github.com/Daffabray/UAP047/blob/main/Grafik%20Akurasi/Screenshot%20(102).png)

Berdasarkan laporan klasifikasi untuk model VGG16 dan CNN:

**VGG16**

Precision, Recall, dan F1-Score: Sangat tinggi untuk semua kelas (mendekati atau mencapai 1), menunjukkan bahwa model ini sangat efektif dalam mengklasifikasikan semua kategori dengan tingkat kesalahan yang minimal.

Akurasi: 99%, menunjukkan kinerja yang hampir sempurna pada data uji.

Kelebihan: Hasil ini didukung oleh kemampuan transfer learning dari model VGG16, yang sudah dilatih pada dataset besar sebelumnya.

**CNN**

Precision, Recall, dan F1-Score: Masih tinggi untuk sebagian besar kelas, namun ada kelemahan pada kelas "Negatif" (Precision: 0.81, Recall: 0.60), yang menurunkan performa keseluruhan.

Akurasi: 90%, lebih rendah dibandingkan VGG16.

Kelebihan dan Kekurangan: Model CNN menunjukkan kemampuan yang baik, tetapi tanpa manfaat fitur pra-latih, membutuhkan penyesuaian lebih lanjut.

**Perbandingan**

Akurasi: VGG16 (99%) lebih unggul dibandingkan CNN (90%).

Konsistensi Antar Kelas: VGG16 lebih konsisten dengan skor tinggi untuk semua kelas. CNN memiliki masalah pada kelas "Negatif".

Konteks Penggunaan: VGG16 lebih cocok untuk aplikasi yang membutuhkan hasil cepat dan akurat, sedangkan CNN mungkin lebih fleksibel untuk eksperimen dan adaptasi.

## Tampilan WEB

![Tampilan2](https://github.com/Daffabray/UAP047/blob/main/Tampilan/Screenshot%20(103).png)


![Tampilan1](https://github.com/Daffabray/UAP047/blob/main/Tampilan/Screenshot%20(104).png)


## Link Model

Link Pembuatan Model : [Colab](https://colab.research.google.com/drive/17ZHgzijLX2j9hNGIhZXdsgbpn1hPYBxr?usp=sharing)

VGG16 : [VGG16](https://drive.google.com/file/d/1FtAHDXYGWxYdS3k_lPoS4x_Rt-OO3DkG/view?usp=sharing)

CNN   : [CNN]
