import sys #mengimport system
from PyQt5.QtWidgets import *

if __name__ == '__main__': #untuk menentukan inilo tugas utamanya python
    app = QApplication(sys.argv) #yang di dalam kurung adalah parameter
    form = QWidget() #membuat form dengan perintah QWidget
    form.setGeometry(80,80,800,300) #ukuran window terhadap layar(x), dari atas(y), lebar,tinggi
    form.setWindowTitle("PyQt5 Form") #Judul jendela

#Menampilkan teks label
    label = QLabel(form) #label = variabel
    label.setText("Masukkan Biodata Anda") #menampilkan tulisan/judul yang tidak bisa diubah lagi
    label.setStyleSheet("background-color: blue; color: red; font: bold 30px; ") #mengatur ukuran,warna font tulisan

    lineEdit1 = QLineEdit() #QLineEdit digunakan untuk memunculkan kotak inputan dengan variabel lineEdit1
    lineEdit2 = QLineEdit() #QLineEdit digunakan untuk memunculkan kotak inputan dengan variabel lineEdit2
    lineEdit3 = QLineEdit() #QLineEdit digunakan untuk memunculkan kotak inputan dengan variabel lineEdit3

    layout = QFormLayout() #layout = variabel
    layout.addRow(label)
    layout.addRow("Name", lineEdit1) #addRow digunakan untuk menambah baris baru(Form) dengan awalan text (name), setelah itu kotak untuk inputan
    layout.addRow("Adress", lineEdit2) #addRow digunakan untuk menambah baris baru(Form) dengan awalan text (Adress), setelah itu kotak untuk inputan
    layout.addWidget(lineEdit3) #menambahkan widget lineEdit


    check1 = QCheckBox("Makan") #Menampilkan pilihan klik persegi
    check2 = QCheckBox("Tidur") #Menampilkan pilihan klik persegi
    check3 = QCheckBox("Main") #Menampilkan pilihan klik persegi
    layout.addRow("Hobby", check1) #addRow digunakan untuk menambah baris baru(checkBox)dengan awalan text (name), setelah itu kotak untuk inputan
    layout.addWidget(check2) #menambahkan widget check2(tidur)
    layout.addWidget(check3) #menambahkan widget check3(main)


    rad1 = QRadioButton("Pelajar") #Menampilkan pilihan klik lingkaran dan hanya bisa memilih salah satu saja
    rad2 = QRadioButton("Pegawai") #Menampilkan pilihan klik lingkaran dan hanya bisa memilih salah satu saja
    rad3 = QRadioButton("Wirasawasta") #Menampilkan pilihan klik lingkaran dan hanya bisa memilih salah satu saja
    layout.addRow("Status", rad1) #addRow digunakan untuk menambah baris baru(RadioButton)dengan awalan text (Status), setelah itu kotak untuk inputan
    layout.addWidget(rad2) #menambahkan widget rad2(Pegawai)
    layout.addWidget(rad3) #menambahkan widget rad3(Wiraswasta)



#perintah proses menjalankan
    form.setLayout(layout)
    form.show()
    app.exec_()