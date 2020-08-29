from PyQt5.QtGui import *
import os
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import time
import os,subprocess,sys
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from hill import *
from cesar import *
from RSA import *
from fctbd import *
import pickle
from des import *
class Ui_graphic(QWidget):
    global   etat,username,C,algochoisis,cesarpas,vikey,rsapc,rsapr,level,descle,ha,hb,hc,hd,FilePath
    def __init__(self):
        super(Ui_graphic, self).__init__()
        loadUi("graphic.ui", self)
        self.etat=0
        self.level=None
        self.msg_7.hide()
        self.msg.hide()
        self.FilePath=""
        self.label_42.hide()
        self.radioButton_6.hide()
        self.radioButton_7.hide()
        self.msg_2.hide()
        self.msg_3.hide()
        self.msg_4.hide()
        self.msg_5.hide() 
        self.msg_14.hide()
        self.msg_6.hide()
        self.msg_8.hide()
        self.msg_9.hide()
        self.msg_10.hide()
        self.msg_11.hide()
        self.msg_13.hide()
        self.msg_12.hide()
        self.msg_15.hide()
        self.loginbt_5.hide()
        self.exit.clicked.connect(self.close)
        self.reduit.clicked.connect(self.showMinimized)
        self.main.setCurrentWidget(self.acceuil)
        self.creataccountbt.clicked.connect(self.switch_to_inscription)
        self.gologinbt.clicked.connect(self.switch_to_acceuil)
        self.confirmebt.clicked.connect(self.switch_to_expertinsc)
        self.cesarbtn.clicked.connect(self.switch_to_cesar)
        self.hillbtn.clicked.connect(self.switch_to_hill)
        self.vignerebtn.clicked.connect(self.switch_to_vignere)
        self.RSAbtn.clicked.connect(self.switch_to_RSA)
        self.DESbtn.clicked.connect(self.switch_to_DES)
        self.next1.clicked.connect(self.switch_to_page2)
        self.next2.clicked.connect(self.switch_to_page3)
        self.confirme_beginner.clicked.connect(self.switch_to_inscrfinal)
        self.confirme_expert.clicked.connect(self.switch_to_acceuil2)
        self.loginbt.clicked.connect(self.login)
        self.loginbt_2.clicked.connect(self.switch_to_inscrfinal)
        self.loginbt_3.clicked.connect(self.switch_to_inscrfinal)
        self.loginbt_4.clicked.connect(self.switch_to_tfichier)
        self.loginbt_5.clicked.connect(self.switch_to_tmessage)
        self.loginbt_6.clicked.connect(self.switch_to_login)
        self.loginbt_7.clicked.connect(self.choosePath)
        self.cryptebtn.clicked.connect(self.crypter)
        self.decryptebtn.clicked.connect(self.decrypter)
        self.cryptebtn_2.clicked.connect(self.crypterf)
        self.decryptebtn_5.clicked.connect(self.open)
        self.next1_2.clicked.connect(self.switch_to_page1)
        self.next1_3.clicked.connect(self.switch_to_page2)

        
        self.decryptebtn_2.clicked.connect(self.decrypterf)
        self.debutant.toggled.connect(self.msg.hide)
        self.expert_2.toggled.connect(self.msg.hide)
        self.radioButton_5.toggled.connect(self.hide__)
        self.radioButton_4.toggled.connect(self.show__)
        self.setWindowFlags(Qt.FramelessWindowHint)
    def switch_to_login(self):
        self.msg_11.hide()
        self.msg_12.hide()
        self.msg_13.hide()
        self.msg_14.hide()
        self.msg_15.hide()
        self.main.setCurrentWidget(self.acceuil)
    def switch_to_tfichier(self):
        self.msg_11.hide()
        self.msg_12.hide()
        self.msg_13.hide()
        self.msg_14.hide()
        self.msg_15.hide()
        self.loginbt_4.hide()
        self.loginbt_5.show()
        self.type.setCurrentWidget(self.tfichier)
    def switch_to_tmessage(self):
        self.msg_11.hide()
        self.msg_12.hide()
        self.msg_13.hide()
        self.msg_14.hide()
        self.msg_15.hide()
        self.loginbt_5.hide()
        self.loginbt_4.show()
        self.type.setCurrentWidget(self.tmessage)
    def hide__(self):
        self.label_42.hide() 
        self.radioButton_6.hide() 
        self.radioButton_7.hide() 
        self.radioButton_7.setChecked(True)
        
    def show__(self):
         self.label_42.show()
         self.radioButton_6.show()
         self.radioButton_7.show()
    def crypterf(self):
        self.FilePath=self.chemin.text()
        self.msg_11.hide()
        self.msg_12.hide()
        self.msg_13.hide()
        self.msg_14.hide()
        self.msg_15.hide()
        if self.FilePath=="":
            self.msg_11.show()
        else:
            extension=os.path.splitext(self.FilePath)
            if ".txt" in extension[1]:
                try:
                    with open(self.FilePath, 'r') as myfile:
                        data = myfile.read()
                    if self.algochoisis==0:
                        txt=cesar(data,self.cesarpas)
                    if self.algochoisis==1:
                        txt=viencrypt(data,self.vikey)
                    if self.algochoisis==2:
                        txt=hillencrypt(data,self.C)
                    if self.algochoisis==3 :
                            encrypted_msg=encrypt(self.rsapc, data)
                            txt='µ'.join(map(lambda x: str(x), encrypted_msg))
                    
                    if self.algochoisis==4 :
                        txt=des(data,self.descle)
                    os.remove(self.FilePath)
                    with open(self.FilePath, 'w') as outputfile:
                        outputfile.write(str(txt))
                    self.msg_14.show()


                except :
                    self.msg_13.show()
            else :
                self.msg_12.show()      
        

    def decrypterf(self):
        self.FilePath=self.chemin.text()
        self.msg_11.hide()
        self.msg_12.hide()
        self.msg_13.hide()
        self.msg_14.hide()
        self.msg_15.hide()
        if self.FilePath=="":
            self.msg_11.show()
        else:
            extension=os.path.splitext(self.FilePath)
            if ".txt" in extension[1]:
                try:
                    with open(self.FilePath, 'r') as myfile:
                        data = myfile.read()
                    if self.algochoisis==0:
                        txt=cesar(data,-self.cesarpas)
                    if self.algochoisis==1:
                        txt=videcrypt(data,self.vikey)
                    if self.algochoisis==2:
                        txt=hilldecrypt(data,self.C)
                    if self.algochoisis==3 :
                            encrypted_msg=decrypt(self.rsapc, data)
                            txt='µ'.join(map(lambda x: str(x), encrypted_msg))
                    
                    if self.algochoisis==4 :
                        txt=des(data,self.descle)
                    os.remove(self.FilePath)
                    with open(self.FilePath, 'w') as outputfile:
                        outputfile.write(str(txt))
                    self.msg_15.show()


                except :
                    self.msg_13.show()
            else :
                self.msg_12.show()      
        
    def crypter(self):
        

        if self.algochoisis==0:
            txt=cesar(self.message.toPlainText().upper(),self.cesarpas)
        if self.algochoisis==1:
            txt=viencrypt(self.message.toPlainText().upper(),self.vikey)
        if self.algochoisis==2:
            txt=hillencrypt(self.message.toPlainText().upper(),self.C)
        if self.algochoisis==3 :
                encrypted_msg=encrypt(self.rsapc, self.message.toPlainText())
                txt='µ'.join(map(lambda x: str(x), encrypted_msg)) 
        if self.algochoisis==4 :
            txt=des(self.message.toPlainText(),self.descle)
        self.resultat.setPlainText(txt)
    def decrypter(self):
        if(self.message.toPlainText()!=""):            
            if self.algochoisis==0 :
                txt=cesar(self.message.toPlainText().upper(),-self.cesarpas)
            if self.algochoisis==1:
                txt=videcrypt(self.message.toPlainText().upper(),self.vikey)
            if self.algochoisis==2 :
                txt=hilldecrypt(self.message.toPlainText().upper(),self.C)
            if self.algochoisis==3 :
                encrypted_ms=list(map(int, (self.message.toPlainText().split('µ'))))
                txt=decrypt(self.rsapr, encrypted_ms)
            if self.algochoisis==4 :
                txt=des(self.message.toPlainText(),self.descle,True)
        self.resultat.setPlainText(txt)
    def login(self):
        self.msg_4.hide()
        self.msg_5.hide()
        if check_name(self.username_3.text()):
            self.username=self.username_3.text()
            if check_password(self.username,self.password_3.text()):
                if get_level(self.username)=="expert":
                    self.level=1
                    self.loginbt_3.hide()
                if get_level(self.username)=="beginner":
                    self.level=0
                    self.loginbt_2.hide()   
                self.algochoisis=get_algoch(self.username)
                self.etat=1
                if self.algochoisis== 0:
                    self.algochoi_2.setCurrentWidget(self.cesar_2)
                    self.main.setCurrentWidget(self.cryptage)
                    self.cesarpas=get_cle(self.username)
                if self.algochoisis== 1:
                    self.algochoi_2.setCurrentWidget(self.vignere_2)
                    self.main.setCurrentWidget(self.cryptage)
                    self.vikey=get_cle(self.username)
                if self.algochoisis==2:
                    self.algochoi_2.setCurrentWidget(self.hill_2)
                    self.main.setCurrentWidget(self.cryptage)
                    self.C=get_cle(self.username)
                if self.algochoisis==3:
                    self.algochoi_2.setCurrentWidget(self.RSA_2)
                    self.main.setCurrentWidget(self.cryptage)
                    self.ha,self.hb,self.hc,self.hd=get_cle(self.username)
                if self.algochoisis==4:
                    self.algochoi_2.setCurrentWidget(self.DES_2)
                    self.main.setCurrentWidget(self.cryptage)
                    self.descle=get_cle(self.username)
                if self.algochoisis==None:
                    if get_level(self.username)=="expert":
                        self.main.setCurrentWidget(self.expert)
                        self.algochoi.setCurrentWidget(self.cesar)
                    if get_level(self.username)=="beginner":
                        self.main.setCurrentWidget(self.Debutant) 
                        self.beginner_qts.setCurrentWidget(self.page1)                
            else:
                self.msg_5.show()==True
        else:
            self.msg_4.show()==True
    def switch_to_expertinsc(self):
        self.msg_3.hide()
        self.msg_2.hide()
        self.msg_6.hide()
        self.msg_8.hide()
        username=self.usernamei.text()
        password=self.passwordi.text()
        password1=self.password_4.text()
        if len(username)<6:
            self.msg_3.show()==True
        elif len(password)<8:
            self.msg_6.show()==True
        elif password!=password1:
            self.msg_2.show()==True
        else:
            self.username=username
            if self.expert_2.isChecked():
                if nouveauutil(username,password,"expert")==None:
                    self.msg_8.show()==True
                else :
                    self.main.setCurrentWidget(self.expert)
                    self.algochoi.setCurrentWidget(self.cesar)
                    self.level=1
            elif self.debutant.isChecked():
                if nouveauutil(username,password,"beginner")==None:
                    self.msg_8.show()==True
                else:
                    self.level=0
                    self.main.setCurrentWidget(self.Debutant) 
                    self.beginner_qts.setCurrentWidget(self.page1)
            else:
                self.msg.show()==True


    def switch_to_inscrfinal(self):
        self.msg_11.hide()
        self.msg_12.hide()
        self.msg_13.hide()
        self.msg_14.hide()
        self.msg_15.hide()
        if self.level==0:
            self.RSAbtn.hide()
            self.hillbtn.hide()
            self.vignerebtn.hide()
            self.cesarbtn.hide()
            self.DESbtn.hide()
            self.label_16.hide()
        if self.etat==0:
            reponses=[]
            # quel est votre niveau en mathématique [faible ,moyen ,élevé ]
            if self.radioButton.isChecked():
                reponses.append(1)
            elif self.radioButton_2.isChecked():
                reponses.append(2)
            else:
                reponses.append(3)
            # quel est le degré de sensibilité de vos fichiers[bas sensibilité,moyen sensibilité,haute sensibilité]
            if self.radioButton_10.isChecked():
                reponses.append(1)
            elif self.radioButton_11.isChecked():
                reponses.append(2)
            else:
                reponses.append(3)
            # avez-vous des bases en cryptographie / faites-vous la différence entre la crypto symétrique et crypto assymétrique 
            if self.radioButton_6.isChecked():
                reponses.append(1)
            else :
                reponses.append(2)
            # vous fichiers sont-ils destinées pour être utiliser :[local,externe]
            if self.radioButton_9.isChecked():
                reponses.append(1)
            else :
                reponses.append(2)
            #  Quelle  degré de cryptage voulez-vous :[faible ,moyen ,élevé ]
            if self.radioButton_29.isChecked():
                reponses.append(1)
            elif self.radioButton_30.isChecked():
                reponses.append(2)
            else:
                reponses.append(3)

            #temps de cryptage : rapide (moins sécurisé)/ long
            if self.radioButton_32.isChecked():
                reponses.append(1)
            else :
                reponses.append(2)
            filename = 'model.sav'
            loaded_model = pickle.load(open(filename, 'rb'))    
            result=loaded_model.predict([reponses])
            self.algochoisis=result[0]
            if self.algochoisis== 0:
                self.algochoi.setCurrentWidget(self.cesar)
                self.cesarbtn.setChecked(True)
            if self.algochoisis== 1:
                self.algochoi.setCurrentWidget(self.vignere)
                self.vignerebtn.setChecked(True)
            if self.algochoisis==2:
                self.algochoi.setCurrentWidget(self.hill)
                self.hillbtn.setChecked(True)
            if self.algochoisis==3:
                self.algochoi.setCurrentWidget(self.RSA)
                self.RSAbtn.setChecked(True)
            if self.algochoisis==4:
                self.algochoi.setCurrentWidget(self.DES)
                self.DESbtn.setChecked(True)
        else:
            self.algochoisis=get_algoch(self.username)
            if self.algochoisis== 0:
                self.algochoi.setCurrentWidget(self.cesar)
                self.cesarbtn.setChecked(True)
            if self.algochoisis== 1:
                self.algochoi.setCurrentWidget(self.vignere)
                self.vignerebtn.setChecked(True)
            if self.algochoisis==2:
                self.algochoi.setCurrentWidget(self.hill)
                self.hillbtn.setChecked(True)
            if self.algochoisis==3:
                self.algochoi.setCurrentWidget(self.RSA)
                self.RSAbtn.setChecked(True)
            if self.algochoisis==4:
                self.algochoi.setCurrentWidget(self.DES)
                self.DESbtn.setChecked(True)
        self.main.setCurrentWidget(self.expert)
        
    def switch_to_acceuil2(self):
        self.msg_7.hide()
        self.msg_9.hide()
        self.msg_10.hide()
        if self.etat== 1 :
            if get_algoch(self.username)==0:
                supprimer_algo(self.username,"cesar")
            if get_algoch(self.username)==1:
                supprimer_algo(self.username,"vignere")
            if get_algoch(self.username)==2:
                supprimer_algo(self.username,"hill")
            if get_algoch(self.username)==3:
                supprimer_algo(self.username,"rsa")
            if get_algoch(self.username)==4:
                supprimer_algo(self.username,"des")
            if self.cesarbtn.isChecked():
                self.algochoisis=0
                set_algoch(self.username,0)
                add_cesar(self.username,int(self.cesarcle.text()))
                self.algochoi_2.setCurrentWidget(self.cesar_2)
                self.cesarpas=get_cle(self.username)
                self.main.setCurrentWidget(self.cryptage)
            if self.vignerebtn.isChecked():
                self.algochoisis=1
                set_algoch(self.username,1)
                add_vignere(self.username,self.vignerecle.text())
                self.algochoi_2.setCurrentWidget(self.vignere_2)
                self.main.setCurrentWidget(self.cryptage)
                self.vikey=get_cle(self.username)
            if self.hillbtn.isChecked():  
                cle=make_key(int(self.hilla.text()),int(self.hillb.text()),int(self.hillc.text()),int(self.hilld.text()))
                try:
                    if cle!=None:
                        self.C=cle
                        self.algochoisis=2
                        set_algoch(self.username,2)
                        add_hill(self.username,self.C[0][0],self.C[0][1],self.C[1][0],self.C[1][1])
                        self.main.setCurrentWidget(self.cryptage)
                        self.algochoi_2.setCurrentWidget(self.hill_2)
                    else:
                        self.msg_7.show()==True
                except :
                    self.msg_7.show()==True
                
            if self.RSAbtn.isChecked():
                try:
                    public, private = generate_keypair(self.rsap.value(), self.rsaq.value())
                    self.algochoisis=3
                    self.main.setCurrentWidget(self.cryptage)
                    self.rsapc=(public[0], public[1])
                    self.rsapr=(private[0], private[1])
                    set_algoch(self.username,3)
                    add_rsa(self.username,public[1],public[0],private[0])
                    self.algochoi_2.setCurrentWidget(self.RSA_2)
                except :
                      self.msg_10.show()                    
            if self.DESbtn.isChecked():
                x=self.rachid.text()
                if len(x)<8:
                    self.msg_9.show()
                else:
                    self.descle=x
                    self.algochoisis=4
                    set_algoch(self.username,4)
                    add_des(self.username,self.descle)
                    self.main.setCurrentWidget(self.cryptage)
                    self.algochoi_2.setCurrentWidget(self.DES_2)

                                    
        else:
            if get_level(self.username)=="expert":
                self.level=1
                self.loginbt_3.hide()
            if get_level(self.username)=="beginner":
                self.level=0
                self.loginbt_2.hide() 
            if self.cesarbtn.isChecked():
                set_algoch(self.username,0)
                add_cesar(self.username,int(self.cesarcle.text()))
                self.main.setCurrentWidget(self.acceuil)
            if self.vignerebtn.isChecked():
                set_algoch(self.username,1)
                add_vignere(self.username,self.vignerecle.text())
                self.main.setCurrentWidget(self.acceuil)
            if self.hillbtn.isChecked():  
                cle=make_key(int(self.hilla.text()),int(self.hillb.text()),int(self.hillc.text()),int(self.hilld.text()))
                if cle!=None:
                    self.C=cle
                    self.algochoisis=2
                    set_algoch(self.username,2)
                    add_hill(self.username,self.C[0][0],self.C[0][1],self.C[1][0],self.C[1][1])
                    self.main.setCurrentWidget(self.acceuil)
                else:
                    self.msg_7.show()==True

            if self.RSAbtn.isChecked():
                try:
                    public, private = generate_keypair(self.rsap.value(), self.rsaq.value())
                    self.algochoisis=3
                    self.rsapc=(public[0], public[1])
                    self.rsapr=(private[0], private[1])
                    set_algoch(self.username,3)
                    add_rsa(self.username,public[1],public[0],private[0])
                    self.main.setCurrentWidget(self.acceuil)
                except :
                      self.msg_10.show()
            if self.DESbtn.isChecked():
                x=self.rachid.text()
                if len(x)<8:
                    self.msg_9.show()
                else:
                    self.descle=x
                    self.algochoisis=4
                    set_algoch(self.username,4)
                    add_des(self.username,self.descle)
                    self.main.setCurrentWidget(self.acceuil)
    def switch_to_page1(self):
        self.beginner_qts.setCurrentWidget(self.page1)
    def switch_to_page2(self):
        self.beginner_qts.setCurrentWidget(self.page2)
    def switch_to_page3(self):
        self.beginner_qts.setCurrentWidget(self.page3)
    def switch_to_vignere(self):
        self.algochoi.setCurrentWidget(self.vignere)
    def switch_to_RSA(self):
        self.algochoi.setCurrentWidget(self.RSA)
    def switch_to_DES(self):
        self.algochoi.setCurrentWidget(self.DES)
    def switch_to_hill(self):
        self.algochoi.setCurrentWidget(self.hill)
    def switch_to_cesar(self):
        self.algochoi.setCurrentWidget(self.cesar)
    def switch_to_inscription(self):
        self.main.setCurrentWidget(self.inscription)       
    def switch_to_acceuil(self):
        self.main.setCurrentWidget(self.acceuil)
    def open(self):
        self.FilePath=self.chemin.text()
        self.msg_11.hide()
        self.msg_12.hide()
        self.msg_13.hide()
        self.msg_14.hide()
        self.msg_15.hide()
        if self.FilePath=="":
            self.msg_11.show()
        else:
            extension=os.path.splitext(self.FilePath)
            if ".txt" in extension[1]:
                try:
                    if sys.platform == "win32":
                        
                        os.startfile(self.FilePath)
                        
                except :
                    self.msg_13.show()
            else :
                self.msg_12.show()      
        
        
    def choosePath(self):
        self.msg_11.hide()
        self.msg_12.hide()
        self.msg_13.hide()
        self.msg_14.hide()
        self.msg_15.hide()
        self.FilePath,type = QFileDialog.getOpenFileName(self)
        self.chemin.setText(self.FilePath)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = Ui_graphic()
    myapp.show()
    sys.exit(app.exec_())
