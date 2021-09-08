

#---------------KÜTÜPHANELER--------------#
#-----------------------------------------#
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from anaSayfa import *
from menuHakkinda import *

#---------------UYGULAMA OLUŞTURMA--------------#
#-----------------------------------------------#

Uygulama=QApplication(sys.argv)
penAna=QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(penAna)
penAna.show()


penHakkinda=QDialog()
ui2=Ui_Dialog()
ui2.setupUi(penHakkinda)

#---------------VERİTABANI OLUŞTURMA------------#
#-----------------------------------------------#

import sqlite3
global curs
global conn

conn=sqlite3.connect("sporProgramı.db")
curs=conn.cursor()

sorguSporcuTabloOlustur=("""CREATE TABLE IF NOT EXISTS spor(
                         Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                         TCNo TEXT NOT NULL UNIQUE,
                         SporcuAdi TEXT NOT NULL,
                         SporcuSoyadi TEXT NOT NULL,
                         KulupAdi TEXT NOT NULL,
                         Brans TEXT NOT NULL,
                         Cinsiyet TEXT NOT NULL,
                         DTarihi TEXT NOT NULL,
                         MHal TEXT NOT NULL,
                         Kilo TEXT NOT NULL)""")


curs.execute(sorguSporcuTabloOlustur)
conn.commit()

#---------------KAYDET--------------------------#
#-----------------------------------------------#

def EKLE():
    _lineTcKimlik=ui.lineTcKimlik.text()
    _lineAd=ui.lineAd.text()
    _lineSoyad=ui.lineSoyad.text()
    _cmbKulup=ui.cmbKulup.currentText()
    _lwBrans=ui.lwBrans.currentItem().text()
    _cmbCinsiyet=ui.cmbCinsiyet.currentText()
    _cwdogumTarihi=ui.cwdogumTarihi.selectedDate().toString(QtCore.Qt.ISODate)
    if ui.checkMedeniHal.isChecked():
        _checkMedeniHal="Evli"
    else:
        _checkMedeniHal="Bekar"
    _spinKilo=ui.spinKilo.value()
    
    
    curs.execute("""INSERT INTO spor(
                          TCNo,SporcuAdi,SporcuSoyadi,KulupAdi,Brans,Cinsiyet,DTarihi,MHal,Kilo)
    VALUES(?,?,?,?,?,?,?,?,?)""",(_lineTcKimlik,_lineAd,_lineSoyad,_cmbKulup,_lwBrans,_cmbCinsiyet,_cwdogumTarihi,_checkMedeniHal,_spinKilo))
    conn.commit()
    LISTELE()

#---------------LISTELE-------------------------#
#-----------------------------------------------#

def LISTELE():
    ui.tblwSporcuBilgi.clear()
    ui.tblwSporcuBilgi.setHorizontalHeaderLabels(("No","TC Kimlik No","Sporcu Adı","Sporcu Soyadı","Kulüp Adı","Branş","Cinsiyet","Doğum Tarihi","Medeni Hal","Sporcu Kilosu"))
    ui.tblwSporcuBilgi.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    curs.execute("SELECT * FROM spor")
    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate(satirVeri):
            ui.tblwSporcuBilgi.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))
    
    ui.lineTcKimlik.clear()
    ui.lineAd.clear()
    ui.lineSoyad.clear()
    ui.cmbKulup.setCurrentIndex(-1)
    ui.spinKilo.setValue(55)
    ui.cmbCinsiyet.setCurrentIndex(-1)
    curs.execute("SELECT COUNT(*) FROM spor")
    kayitSayisi=curs.fetchone()
    ui.lblKayitSayisi.setText(str(kayitSayisi[0]))

LISTELE()

#---------------CIKIS---------------------------#
#-----------------------------------------------#

def CIKIS():
    cevap=QMessageBox.question(penAna,"Kapat","Cıkmak icin emin misiniz ?",QMessageBox.Yes | QMessageBox.No)
    if cevap==QMessageBox.Yes:
        conn.close()
        sys.exit(Uygulama.exec_())
    else:
        penAna.show()

#---------------SILME---------------------------#
#-----------------------------------------------#

def SIL():
    cevap=QMessageBox.question(penAna,"Kayıt Sil","kaydı silmek için emin misiniz ?",QMessageBox.Yes | QMessageBox.No)
    if cevap==QMessageBox.Yes:
        secili=ui.tblwSporcuBilgi.selectedItems()
        silinecek=secili[1].text()
        try:
            curs.execute("DELETE FROM spor WHERE TCNo={}".format(str(silinecek)))
            conn.commit()
            LISTELE()
            ui.statusbar.showMessage("Kayit Silme Işlemi Başarı ile Gerçekleşti",10000)
        except Exception as Hata:
            ui.statusbar.showMessage("Şöyle bir hata ile Karşılaşıldı "+str(Hata))
        
        
    else:
        ui.statusbar.showMessage("Silme işlemi iptal edildi...",10000)


#---------------ARAMA---------------------------#
#-----------------------------------------------#

def ARA():
    arananTC=ui.lineTcKimlik.text()
    arananAd=ui.lineAd.text()
    arananSoyad=ui.lineSoyad.text()
    curs.execute("SELECT * FROM spor WHERE TCNo=? OR SporcuAdi=? OR SporcuSoyadi=? OR (SporcuAdi=? AND SporcuSoyadi=?)",(arananTC,arananAd,arananSoyad,arananAd,arananSoyad))
    conn.commit()
    ui.tblwSporcuBilgi.clear()
    ui.tblwSporcuBilgi.setHorizontalHeaderLabels(("No","TC Kimlik No","Sporcu Adı","Sporcu Soyadı","Kulüp Adı","Branş","Cinsiyet","Doğum Tarihi","Medeni Hal","Sporcu Kilosu"))
    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate(satirVeri):
            ui.tblwSporcuBilgi.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))



#---------------DOLDURMA------------------------#
#-----------------------------------------------#
def DOLDUR():
    secili=ui.tblwSporcuBilgi.selectedItems()
    ui.lineTcKimlik.setText(secili[1].text())
    ui.lineAd.setText(secili[2].text())
    ui.lineSoyad.setText(secili[3].text())
    ui.cmbKulup.setCurrentText(secili[4].text())
    if secili[5].text()=="Güreş":
        ui.lwBrans.item(0).setSelected(True)
        ui.lwBrans.setCurrentItem(ui.lwBrans.item(0))
    if secili[5].text()=="Boks":
        ui.lwBrans.item(1).setSelected(True)
        ui.lwBrans.setCurrentItem(ui.lwBrans.item(1))
    if secili[5].text()=="Yüzme":
        ui.lwBrans.item(2).setSelected(True)
        ui.lwBrans.setCurrentItem(ui.lwBrans.item(2))
    if secili[5].text()=="Futbol":
        ui.lwBrans.item(3).setSelected(True)
        ui.lwBrans.setCurrentItem(ui.lwBrans.item(3))
    if secili[5].text()=="Basketbol":
        ui.lwBrans.item(4).setSelected(True)
        ui.lwBrans.setCurrentItem(ui.lwBrans.item(4))
    if secili[5].text()=="Voleybol":
        ui.lwBrans.item(5).setSelected(True)
        ui.lwBrans.setCurrentItem(ui.lwBrans.item(5))
    ui.cmbCinsiyet.setCurrentText(secili[6].text())
    yil=int(secili[7].text()[0:4])
    ay=int(secili[7].text()[5:7])
    gun=int(secili[7].text()[8:10])
    ui.cwdogumTarihi.setSelectedDate(QtCore.QDate(yil,ay,gun))
    if secili[8].text()=="Evli":
        ui.checkMedeniHal.setChecked(True)
    else:
        ui.checkMedeniHal.setChecked(False)
    ui.spinKilo.setValue(int(secili[9].text()))
    
#---------------GUNCELLE------------------------#
#-----------------------------------------------#

def GUNCELLE():
    cevap=QMessageBox.question(penAna,"Kayıt Guncelle","kaydı guncellemek icin emin misiniz ?",QMessageBox.Yes | QMessageBox.No)
    if cevap==QMessageBox.Yes:
        try:
            secili=ui.tblwSporcuBilgi.selectedItems()
            _id=int(secili[0].text())
            _lineTcKimlik=ui.lineTcKimlik.text()
            _lineAd=ui.lineAd.text()
            _lineSoyad=ui.lineSoyad.text()
            _cmbKulup=ui.cmbKulup.currentText()
            _lwBrans=ui.lwBrans.currentItem().text()
            _cmbCinsiyet=ui.cmbCinsiyet.currentText()
            _cwdogumTarihi=ui.cwdogumTarihi.selectedDate().toString(QtCore.Qt.ISODate)
            if ui.checkMedeniHal.isChecked():
                _checkMedeniHal="Evli"
            else:
                _checkMedeniHal="Bekar"
            _spinKilo=ui.spinKilo.value()
            
            curs.execute("UPDATE spor SET TCNo=?, SporcuAdi=?, SporcuSoyadi=?, KulupAdi=? ,Brans=?, Cinsiyet=?, DTarihi=?, MHal=?, Kilo=? WHERE Id=?",(_lineTcKimlik, _lineAd, _lineSoyad, _cmbKulup, _lwBrans, _cmbCinsiyet, _cwdogumTarihi, _checkMedeniHal, _spinKilo, _id))
            conn.commit()
            LISTELE()
            ui.statusbar.showMessage("Güncelleme başarı ile tammalandı",10000)
        except Exception as Hata:
            ui.statusbar.showMessage("böyle bir hata ile karşılaştık : "+str(Hata))
    else:
        ui.statusbar.showMessage("Guncelleme iptal edildi...",10000)
    
#---------------HAKKINDA------------------------#
#-----------------------------------------------#

def HAKKINDA():
    penHakkinda.show()


#---------------SIGNAL-SLOT---------------------#
#-----------------------------------------------#
ui.btnEkle.clicked.connect(EKLE)
ui.btnListele.clicked.connect(LISTELE)
ui.btnCikis.clicked.connect(CIKIS)
ui.btnSil.clicked.connect(SIL)
ui.btnAra.clicked.connect(ARA)
ui.tblwSporcuBilgi.itemSelectionChanged.connect(DOLDUR)
ui.btnGuncelle.clicked.connect(GUNCELLE)
ui.menuHakkinda.triggered.connect(HAKKINDA)



sys.exit(Uygulama.exec_())

    
    