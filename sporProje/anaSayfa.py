# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anaSayfaUİ.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1094, 816)
        MainWindow.setStyleSheet(".QWidget {\n"
"   background-color: beige;\n"
"}\n"
"\n"
"/* Nice Windows-XP-style password character. */\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character: 9679;\n"
"}\n"
"\n"
"/* We provide a min-width and min-height for push buttons\n"
"   so that they look elegant regardless of the width of the text. */\n"
"QPushButton {\n"
"    background-color: palegoldenrod;\n"
"    border-width: 2px;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 5;\n"
"    padding: 3px;\n"
"    min-width: 9ex;\n"
"    min-height: 2.5ex;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: khaki;\n"
"}\n"
"\n"
"/* Increase the padding, so the text is shifted when the button is\n"
"   pressed. */\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: #d0d67c;\n"
"}\n"
"\n"
"QLabel, QAbstractButton {\n"
"    font: bold;\n"
"}\n"
"\n"
"/* Mark mandatory fields with a brownish color. */\n"
".mandatory {\n"
"    color: brown;\n"
"}\n"
"\n"
"/* Bold text on status bar looks awful. */\n"
"QStatusBar QLabel {\n"
"   font: normal;\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    border-width: 1;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 2;\n"
"}\n"
"\n"
"QComboBox, QLineEdit, QSpinBox, QTextEdit, QListView {\n"
"    background-color: cornsilk;\n"
"    selection-color: #0a214c; \n"
"    selection-background-color: #C19A6B;\n"
"}\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1;\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* We reserve 1 pixel space in padding. When we get the focus,\n"
"   we kill the padding and enlarge the border. This makes the items\n"
"   glow. */\n"
"QLineEdit, QFrame {\n"
"    border-width: 2px;\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border-color: darkkhaki;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* As mentioned above, eliminate the padding and increase the border. */\n"
"QLineEdit:focus, QFrame:focus {\n"
"    border-width: 3px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"/* A QLabel is a QFrame ... */\n"
"QLabel {\n"
"    border: none;\n"
"    padding: 0;\n"
"    background: none;\n"
"}\n"
"\n"
"/* A QToolTip is a QLabel ... */\n"
"QToolTip {\n"
"    border: 2px solid darkkhaki;\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"/* Nice to have the background color change when hovered. */\n"
"QRadioButton:hover, QCheckBox:hover {\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* Force the dialog\'s buttons to follow the Windows guidelines. */\n"
"QDialogButtonBox {\n"
"    button-layout: 0;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 801, 401))
        self.groupBox.setObjectName("groupBox")
        self.lwBrans = QtWidgets.QListWidget(self.groupBox)
        self.lwBrans.setGeometry(QtCore.QRect(70, 240, 241, 151))
        self.lwBrans.setObjectName("lwBrans")
        item = QtWidgets.QListWidgetItem()
        self.lwBrans.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lwBrans.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lwBrans.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lwBrans.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lwBrans.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lwBrans.addItem(item)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 230, 51, 21))
        self.label_8.setObjectName("label_8")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(20, 20, 311, 210))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_1 = QtWidgets.QLabel(self.widget)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout.addWidget(self.label_1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineTcKimlik = QtWidgets.QLineEdit(self.widget)
        self.lineTcKimlik.setMaxLength(11)
        self.lineTcKimlik.setObjectName("lineTcKimlik")
        self.horizontalLayout.addWidget(self.lineTcKimlik)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.lineAd = QtWidgets.QLineEdit(self.widget)
        self.lineAd.setInputMask("")
        self.lineAd.setObjectName("lineAd")
        self.horizontalLayout_2.addWidget(self.lineAd)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.lineSoyad = QtWidgets.QLineEdit(self.widget)
        self.lineSoyad.setInputMask("")
        self.lineSoyad.setObjectName("lineSoyad")
        self.horizontalLayout_3.addWidget(self.lineSoyad)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.cmbKulup = QtWidgets.QComboBox(self.widget)
        self.cmbKulup.setObjectName("cmbKulup")
        self.cmbKulup.addItem("")
        self.cmbKulup.addItem("")
        self.cmbKulup.addItem("")
        self.cmbKulup.addItem("")
        self.cmbKulup.addItem("")
        self.cmbKulup.addItem("")
        self.cmbKulup.addItem("")
        self.horizontalLayout_4.addWidget(self.cmbKulup)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.spinKilo = QtWidgets.QSpinBox(self.widget)
        self.spinKilo.setMaximum(180)
        self.spinKilo.setProperty("value", 55)
        self.spinKilo.setObjectName("spinKilo")
        self.horizontalLayout_5.addWidget(self.spinKilo)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.cmbCinsiyet = QtWidgets.QComboBox(self.widget)
        self.cmbCinsiyet.setObjectName("cmbCinsiyet")
        self.cmbCinsiyet.addItem("")
        self.cmbCinsiyet.addItem("")
        self.horizontalLayout_6.addWidget(self.cmbCinsiyet)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.checkMedeniHal = QtWidgets.QCheckBox(self.widget)
        self.checkMedeniHal.setObjectName("checkMedeniHal")
        self.horizontalLayout_7.addWidget(self.checkMedeniHal)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.cwdogumTarihi = QtWidgets.QCalendarWidget(self.groupBox)
        self.cwdogumTarihi.setGeometry(QtCore.QRect(400, 30, 392, 236))
        self.cwdogumTarihi.setObjectName("cwdogumTarihi")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(400, 10, 91, 16))
        self.label_9.setObjectName("label_9")
        self.tblwSporcuBilgi = QtWidgets.QTableWidget(self.centralwidget)
        self.tblwSporcuBilgi.setGeometry(QtCore.QRect(20, 430, 1051, 281))
        self.tblwSporcuBilgi.setRowCount(100)
        self.tblwSporcuBilgi.setColumnCount(10)
        self.tblwSporcuBilgi.setObjectName("tblwSporcuBilgi")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 730, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lblKayitSayisi = QtWidgets.QLabel(self.centralwidget)
        self.lblKayitSayisi.setGeometry(QtCore.QRect(130, 730, 191, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lblKayitSayisi.setFont(font)
        self.lblKayitSayisi.setText("")
        self.lblKayitSayisi.setObjectName("lblKayitSayisi")
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(830, 50, 221, 351))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnEkle = QtWidgets.QPushButton(self.widget1)
        self.btnEkle.setObjectName("btnEkle")
        self.verticalLayout_2.addWidget(self.btnEkle)
        self.btnSil = QtWidgets.QPushButton(self.widget1)
        self.btnSil.setObjectName("btnSil")
        self.verticalLayout_2.addWidget(self.btnSil)
        self.btnAra = QtWidgets.QPushButton(self.widget1)
        self.btnAra.setObjectName("btnAra")
        self.verticalLayout_2.addWidget(self.btnAra)
        self.btnGuncelle = QtWidgets.QPushButton(self.widget1)
        self.btnGuncelle.setObjectName("btnGuncelle")
        self.verticalLayout_2.addWidget(self.btnGuncelle)
        self.btnListele = QtWidgets.QPushButton(self.widget1)
        self.btnListele.setObjectName("btnListele")
        self.verticalLayout_2.addWidget(self.btnListele)
        self.btnCikis = QtWidgets.QPushButton(self.widget1)
        self.btnCikis.setObjectName("btnCikis")
        self.verticalLayout_2.addWidget(self.btnCikis)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1094, 26))
        self.menubar.setObjectName("menubar")
        self.menuYard_m = QtWidgets.QMenu(self.menubar)
        self.menuYard_m.setObjectName("menuYard_m")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuHakkinda = QtWidgets.QAction(MainWindow)
        self.menuHakkinda.setObjectName("menuHakkinda")
        self.menuYard_m.addAction(self.menuHakkinda)
        self.menubar.addAction(self.menuYard_m.menuAction())

        self.retranslateUi(MainWindow)
        self.cmbKulup.setCurrentIndex(-1)
        self.cmbCinsiyet.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Spor Programı"))
        self.groupBox.setTitle(_translate("MainWindow", "Sporcu Bilgileri"))
        self.lwBrans.setToolTip(_translate("MainWindow", "Sporcu Branşları"))
        __sortingEnabled = self.lwBrans.isSortingEnabled()
        self.lwBrans.setSortingEnabled(False)
        item = self.lwBrans.item(0)
        item.setText(_translate("MainWindow", "Güreş"))
        item = self.lwBrans.item(1)
        item.setText(_translate("MainWindow", "Boks"))
        item = self.lwBrans.item(2)
        item.setText(_translate("MainWindow", "Yüzme"))
        item = self.lwBrans.item(3)
        item.setText(_translate("MainWindow", "Futbol"))
        item = self.lwBrans.item(4)
        item.setText(_translate("MainWindow", "Basketbol"))
        item = self.lwBrans.item(5)
        item.setText(_translate("MainWindow", "Voleybol"))
        self.lwBrans.setSortingEnabled(__sortingEnabled)
        self.label_8.setText(_translate("MainWindow", "Branş:"))
        self.label_1.setText(_translate("MainWindow", "TC Kimlik Numarası:"))
        self.lineTcKimlik.setToolTip(_translate("MainWindow", "Sporcunun TC Kimlik Numarası"))
        self.label_2.setText(_translate("MainWindow", "Sporcu Adı:"))
        self.lineAd.setToolTip(_translate("MainWindow", "Sporcunun Adı"))
        self.label_3.setText(_translate("MainWindow", "Sporcu Soyadı:"))
        self.lineSoyad.setToolTip(_translate("MainWindow", "Sporcunun Soyadı"))
        self.label_4.setText(_translate("MainWindow", "Sporcu Kulübü:"))
        self.cmbKulup.setToolTip(_translate("MainWindow", "Spor Kulüpleri"))
        self.cmbKulup.setItemText(0, _translate("MainWindow", "Ankaragücü"))
        self.cmbKulup.setItemText(1, _translate("MainWindow", "Bursaspor"))
        self.cmbKulup.setItemText(2, _translate("MainWindow", "Fenerbahçe"))
        self.cmbKulup.setItemText(3, _translate("MainWindow", "Galatasaray"))
        self.cmbKulup.setItemText(4, _translate("MainWindow", "Beşiktaş"))
        self.cmbKulup.setItemText(5, _translate("MainWindow", "Başakşehir"))
        self.cmbKulup.setItemText(6, _translate("MainWindow", "Trabzonspor"))
        self.label_5.setText(_translate("MainWindow", "Sporcu Kilosu"))
        self.spinKilo.setToolTip(_translate("MainWindow", "Sporcu Kilosu "))
        self.spinKilo.setSuffix(_translate("MainWindow", " kg"))
        self.label_6.setText(_translate("MainWindow", "Sporcu Cinsiyeti:"))
        self.cmbCinsiyet.setToolTip(_translate("MainWindow", "Sporcu Cinsiyeti"))
        self.cmbCinsiyet.setItemText(0, _translate("MainWindow", "Erkek"))
        self.cmbCinsiyet.setItemText(1, _translate("MainWindow", "Kız"))
        self.label_7.setText(_translate("MainWindow", "Medeni Hal:"))
        self.checkMedeniHal.setToolTip(_translate("MainWindow", "Evli"))
        self.checkMedeniHal.setText(_translate("MainWindow", "Evli"))
        self.cwdogumTarihi.setToolTip(_translate("MainWindow", "Takvim"))
        self.label_9.setText(_translate("MainWindow", "Doğum Tarihi:"))
        self.label.setText(_translate("MainWindow", "Kayıt Sayısı:"))
        self.btnEkle.setToolTip(_translate("MainWindow", "Yeni Kayıt Eklemek İçin Tıklayınız"))
        self.btnEkle.setText(_translate("MainWindow", "KAYIT EKLE"))
        self.btnSil.setToolTip(_translate("MainWindow", "Kayıt Silmek İçin Tıklayınız"))
        self.btnSil.setText(_translate("MainWindow", "KAYIT SİL"))
        self.btnAra.setToolTip(_translate("MainWindow", "Kayıt Aramak İçin Tıklayınız"))
        self.btnAra.setText(_translate("MainWindow", "KAYIT ARA"))
        self.btnGuncelle.setToolTip(_translate("MainWindow", "Kayıt Güncellemek İçin Tıklayınız"))
        self.btnGuncelle.setText(_translate("MainWindow", "GÜNCELLE"))
        self.btnListele.setToolTip(_translate("MainWindow", "Kayıt Listelemek İçin Tıklayınız"))
        self.btnListele.setText(_translate("MainWindow", "KAYIT LİSTELE"))
        self.btnCikis.setToolTip(_translate("MainWindow", "Çıkış Yapmak İçin Tıklayınız"))
        self.btnCikis.setText(_translate("MainWindow", "ÇIKIŞ"))
        self.menuYard_m.setTitle(_translate("MainWindow", "Yardım"))
        self.menuHakkinda.setText(_translate("MainWindow", "Hakkında"))
