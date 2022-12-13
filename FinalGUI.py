from PyQt5 import QtCore, QtGui, QtWidgets
import time
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QDialog
class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        self.cs=0
        self.ec=0
        self.ce=0
        self.bt=0
        self.mc=0
        self.max=0
        self.ls=[]
        MainWindow.setObjectName("Course Selector")
        MainWindow.resize(1123, 856)


        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(460, 480, 171, 61))
        self.b1.setObjectName("b1")
        self.b1.clicked.connect(self.q01)

        self.l1 = QtWidgets.QLabel(self.centralwidget)
        self.l1.setGeometry(QtCore.QRect(130, 150, 881, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        self.l1.setFont(font)
        self.l1.setObjectName("l1")
        
        self.l2 = QtWidgets.QLabel(self.centralwidget)
        self.l2.setGeometry(QtCore.QRect(50, 220, 1021, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.l2.setFont(font)
        self.l2.setAutoFillBackground(False)
        self.l2.setObjectName("l2")
        
        self.l3 = QtWidgets.QLabel(self.centralwidget)
        self.l3.setGeometry(QtCore.QRect(270, 320, 581, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)   
        self.l3.setFont(font)
        self.l3.setObjectName("l3")
        
        self.l4 = QtWidgets.QLabel(self.centralwidget)
        self.l4.setGeometry(QtCore.QRect(200, 380, 741, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)       
        self.l4.setFont(font)
        self.l4.setObjectName("l4")

        #Common For All Screens
        self.progressBar = QtWidgets.QProgressBar(MainWindow)
        self.by1 = QtWidgets.QPushButton(MainWindow)
        self.by2 = QtWidgets.QPushButton(MainWindow)
        self.by3 = QtWidgets.QPushButton(MainWindow)
        self.by4 = QtWidgets.QPushButton(MainWindow)
        self.by5 = QtWidgets.QPushButton(MainWindow)
        self.by6 = QtWidgets.QPushButton(MainWindow)
        self.by7 = QtWidgets.QPushButton(MainWindow)
        self.by8 = QtWidgets.QPushButton(MainWindow)
        self.by9 = QtWidgets.QPushButton(MainWindow)
        self.by10 = QtWidgets.QPushButton(MainWindow)
        self.by11 = QtWidgets.QPushButton(MainWindow)
        self.by12 = QtWidgets.QPushButton(MainWindow)
        self.by13 = QtWidgets.QPushButton(MainWindow)
        self.by14 = QtWidgets.QPushButton(MainWindow)
        self.by15 = QtWidgets.QPushButton(MainWindow)
        self.bn1 = QtWidgets.QPushButton(MainWindow)
        self.bn2 = QtWidgets.QPushButton(MainWindow)
        self.bn3 = QtWidgets.QPushButton(MainWindow)
        self.bn4 = QtWidgets.QPushButton(MainWindow)
        self.bn5 = QtWidgets.QPushButton(MainWindow)
        self.bn6 = QtWidgets.QPushButton(MainWindow)
        self.bn7 = QtWidgets.QPushButton(MainWindow)
        self.bn8 = QtWidgets.QPushButton(MainWindow)
        self.bn9 = QtWidgets.QPushButton(MainWindow)
        self.bn10 = QtWidgets.QPushButton(MainWindow)
        self.bn11 = QtWidgets.QPushButton(MainWindow)
        self.bn12 = QtWidgets.QPushButton(MainWindow)
        self.bn13 = QtWidgets.QPushButton(MainWindow)
        self.bn14 = QtWidgets.QPushButton(MainWindow)
        self.bn15 = QtWidgets.QPushButton(MainWindow)

        self.lf1 = QtWidgets.QLabel(self.centralwidget)
        self.lf2 = QtWidgets.QLabel(self.centralwidget)
        self.lf3 = QtWidgets.QLabel(self.centralwidget)


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Course Selector"))
        self.b1.setText(_translate("MainWindow", "Begin"))
        self.l1.setText(_translate("MainWindow", "Welcome to Course Selector"))
        self.l2.setText(_translate("MainWindow", "I will help you decide your course for Engineering"))
        self.l3.setText(_translate("MainWindow", "You will be asked a few questions"))
        self.l4.setText(_translate("MainWindow", "which can help us understand your interest"))

    def close(self):
        MainWindow.deleteLater()

    def q01(self):
        self.l1.setText("Do you like technology?")
        self.l1.setGeometry(QtCore.QRect(280, 260, 551, 81))
        font = QtGui.QFont()
        self.l1.adjustSize()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.by1.setGeometry(QtCore.QRect(380, 440, 161, 61))
        self.by1.setObjectName("y")
        self.bn1.setGeometry(QtCore.QRect(548, 440, 161, 61))
        self.bn1.setObjectName("n")
        self.by1.setText("Yes")
        self.bn1.setText("No")
        self.l1.setFont(font)
        self.l2.deleteLater()
        self.l3.deleteLater()
        self.l4.deleteLater()
        self.b1.deleteLater()
        self.progressBar.setGeometry(QtCore.QRect(10, 750, 1101, 71))
        self.progressBar.setMaximum(15)
        self.progressBar.setProperty("value", 1)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.by1.clicked.connect(self.y01)
        self.bn1.clicked.connect(self.n01)   
    def y01(self):
        self.cs+=1
        self.ec+=1
        self.mc+=1
        self.q02()
    def n01(self):
        self.bt+=1
        self.ce+=1
        self.q02()

    def q02(self):
        self.l1.setText("Do you like cars?")
        self.l1.setGeometry(QtCore.QRect(360, 260, 391, 81))        
        self.progressBar.setProperty("value", 2)
        self.by1.deleteLater()
        self.bn1.deleteLater()
        self.by2.setGeometry(QtCore.QRect(380, 440, 161, 61))
        self.by2.setObjectName("y")
        self.bn2.setGeometry(QtCore.QRect(548, 440, 161, 61))
        self.bn2.setObjectName("n")
        self.by2.setText("Yes")
        self.bn2.setText("No")
        self.by2.clicked.connect(self.y02)
        self.bn2.clicked.connect(self.n02)
    def y02(self):
        self.mc+=1
        self.q03()
    def n02(self):
        self.bt+=1
        self.ce+=1
        self.cs+=1
        self.ec+=1
        self.q03()

    def q03(self):
        self.l1.setText("Do you like building homes in minecraft?")
        self.l1.setGeometry(QtCore.QRect(100, 260, 911, 81))        
        self.progressBar.setProperty("value", 3)
        self.by2.deleteLater()
        self.bn2.deleteLater()
        self.by3.setGeometry(QtCore.QRect(380, 440, 161, 61))
        self.by3.setObjectName("y")
        self.bn3.setGeometry(QtCore.QRect(548, 440, 161, 61))
        self.bn3.setObjectName("n")
        self.by3.setText("Yes")
        self.bn3.setText("No")
        self.by3.clicked.connect(self.y03)
        self.bn3.clicked.connect(self.n03)
    def y03(self):
        self.ce+=1
        self.cs+=1
        self.mc+=1
        self.q04()        
    def n03(self):
        self.bt+=1
        self.ec+=1
        self.q04()

    def q04(self):
        self.l1.setText("Do you like to play with chemicals?")
        self.l1.setGeometry(QtCore.QRect(160, 260, 781, 81))        
        self.progressBar.setProperty("value", 4)
        self.by3.deleteLater()
        self.bn3.deleteLater()
        self.by4.setGeometry(QtCore.QRect(380, 440, 161, 61))
        self.by4.setObjectName("y")
        self.bn4.setGeometry(QtCore.QRect(548, 440, 161, 61))
        self.bn4.setObjectName("n")
        self.by4.setText("Yes")
        self.bn4.setText("No")
        self.by4.clicked.connect(self.y04)
        self.bn4.clicked.connect(self.n04)        
    def y04(self):
        self.bt+=1
        self.q05()
    def n04(self):
        self.ce+=1
        self.cs+=1
        self.mc+=1
        self.ec+=1
        self.q05()

    def q05(self):
        self.l1.setText("Do you like fixing things rather than replacing?")
        self.l1.setGeometry(QtCore.QRect(40, 260, 1041, 81))        
        self.progressBar.setProperty("value", 5)
        self.by4.deleteLater()
        self.bn4.deleteLater()
        self.by5.setGeometry(QtCore.QRect(380, 440, 161, 61))
        self.by5.setObjectName("y")
        self.bn5.setGeometry(QtCore.QRect(548, 440, 161, 61))
        self.bn5.setObjectName("n")
        self.by5.setText("Yes")
        self.bn5.setText("No")
        self.by5.clicked.connect(self.y05)
        self.bn5.clicked.connect(self.n05)
    def y05(self):
        self.cs+=1
        self.mc+=1
        self.ec+=1
        self.q06()
    def n05(self):
        self.ce+=1
        self.bt+=1
        self.q06()

    def q06(self):
        self.l1.setText("Do you like to study plants and animals?")
        self.l1.setGeometry(QtCore.QRect(100, 260, 901, 81))        
        self.progressBar.setProperty("value", 6)
        self.by5.deleteLater()
        self.bn5.deleteLater()
        self.by6.setGeometry(QtCore.QRect(380, 440, 161, 61))
        self.by6.setObjectName("y")
        self.bn6.setGeometry(QtCore.QRect(548, 440, 161, 61))
        self.bn6.setObjectName("n")
        self.by6.setText("Yes")
        self.bn6.setText("No")
        self.by6.clicked.connect(self.y06)
        self.bn6.clicked.connect(self.n06)
    def y06(self):
        self.bt+=1
        self.q07()
    def n06(self):
        self.ce+=1
        self.cs+=1
        self.mc+=1
        self.ec+=1
        self.q07()

    def q07(self):
        self.l1.setText("Do you want to settle abroad?")
        self.l1.setGeometry(QtCore.QRect(220, 260, 671, 81))        
        self.progressBar.setProperty("value", 7)
        self.by6.deleteLater()
        self.bn6.deleteLater()
        self.by7.setGeometry(QtCore.QRect(380, 440, 161, 61))
        self.by7.setObjectName("y")
        self.bn7.setGeometry(QtCore.QRect(548, 440, 161, 61))
        self.bn7.setObjectName("n")
        self.by7.setText("Yes")
        self.bn7.setText("No")
        self.by7.clicked.connect(self.y07)
        self.bn7.clicked.connect(self.n07)
    def y07(self):
        self.cs+=1
        self.mc+=1
        self.ec+=1
        self.q08()
    def n07(self):
        self.ce+=1
        self.bt+=1
        self.q08()
    
    def q08(self):
        self.l1.setText("Do you like building things in lego?")
        self.l1.setGeometry(QtCore.QRect(170, 260, 781, 81))        
        self.progressBar.setProperty("value", 8)
        self.by7.deleteLater()
        self.bn7.deleteLater()
        self.by8.setGeometry(QtCore.QRect(380, 440, 161, 61))
        self.by8.setObjectName("y")
        self.bn8.setGeometry(QtCore.QRect(548, 440, 161, 61))
        self.bn8.setObjectName("n")
        self.by8.setText("Yes")
        self.bn8.setText("No")
        self.by8.clicked.connect(self.y08)
        self.bn8.clicked.connect(self.n08)
    def y08(self):
        self.cs+=1
        self.mc+=1
        self.ec+=1
        self.ce+=1
        self.q09()
    def n08(self):
        self.bt+=1
        self.q09()
    
    def q09(self):
        self.l1.setText("Do you open up machines to see what\'s inside?")
        self.l1.setGeometry(QtCore.QRect(30, 260, 1061, 81))        
        self.progressBar.setProperty("value", 9)
        self.by8.deleteLater()
        self.bn8.deleteLater()
        self.by9.setGeometry(QtCore.QRect(380, 440, 161, 61))
        self.by9.setObjectName("y")
        self.bn9.setGeometry(QtCore.QRect(548, 440, 161, 61))
        self.bn9.setObjectName("n")
        self.by9.setText("Yes")
        self.bn9.setText("No")
        self.by9.clicked.connect(self.y09)
        self.bn9.clicked.connect(self.n09)
    def y09(self):
        self.cs+=1
        self.mc+=1
        self.ec+=1
        self.q10()
    def n09(self):
        self.ce+=1
        self.bt+=1
        self.q10()

    def q10(self):
        self.l1.setText("Do you want to find cures to new diseases?")
        self.l1.setGeometry(QtCore.QRect(70, 260, 971, 81))        
        self.progressBar.setProperty("value", 10)
        self.by9.deleteLater()
        self.bn9.deleteLater()
        self.by10.setGeometry(QtCore.QRect(380, 440, 161, 61))
        self.by10.setObjectName("y")
        self.bn10.setGeometry(QtCore.QRect(548, 440, 161, 61))
        self.bn10.setObjectName("n")
        self.by10.setText("Yes")
        self.bn10.setText("No")
        self.by10.clicked.connect(self.y10)
        self.bn10.clicked.connect(self.n10)
    def y10(self):
        self.cs+=1
        self.bt+=1
        self.q11()
    def n10(self):
        self.ce+=1
        self.mc+=1
        self.ec+=1
        self.q11()
    
    def q11(self):
        self.l1.setText("Have you ever wondered how humans think?")
        self.l1.setGeometry(QtCore.QRect(60, 260, 1001, 81))        
        self.progressBar.setProperty("value", 11)
        self.by10.deleteLater()
        self.bn10.deleteLater()
        self.by11.setGeometry(QtCore.QRect(380, 440, 161, 61))
        self.by11.setObjectName("y")
        self.bn11.setGeometry(QtCore.QRect(548, 440, 161, 61))
        self.bn11.setObjectName("n")
        self.by11.setText("Yes")
        self.bn11.setText("No")
        self.by11.clicked.connect(self.y11)
        self.bn11.clicked.connect(self.n11)
    def y11(self):
        self.cs+=1
        self.bt+=1
        self.q12()
    def n11(self):
        self.ce+=1
        self.mc+=1
        self.ec+=1        
        self.q12()
    
    def q12(self):
        self.l1.setText("Did you like the movie I,Robot?")
        self.l1.setGeometry(QtCore.QRect(200, 260, 701, 81))        
        self.progressBar.setProperty("value", 12)
        self.by11.deleteLater()
        self.bn11.deleteLater()
        self.by12.setGeometry(QtCore.QRect(380, 440, 161, 61))
        self.by12.setObjectName("y")
        self.bn12.setGeometry(QtCore.QRect(548, 440, 161, 61))
        self.bn12.setObjectName("n")
        self.by12.setText("Yes")
        self.bn12.setText("No")
        self.by12.clicked.connect(self.y12)
        self.bn12.clicked.connect(self.n12)
    def y12(self):
        self.cs+=1
        self.mc+=1
        self.ec+=1
        self.q13()
    def n12(self):
        self.ce+=1
        self.bt+=1
        self.q13()
    
    def q13(self):
        self.l1.setText("Do you like smart homes?")
        self.l1.setGeometry(QtCore.QRect(260, 260, 581, 81))        
        self.progressBar.setProperty("value", 13)
        self.by12.deleteLater()
        self.bn12.deleteLater()
        self.by13.setGeometry(QtCore.QRect(380, 440, 161, 61))
        self.by13.setObjectName("y")
        self.bn13.setGeometry(QtCore.QRect(548, 440, 161, 61))
        self.bn13.setObjectName("n")
        self.by13.setText("Yes")
        self.bn13.setText("No")
        self.by13.clicked.connect(self.y13)
        self.bn13.clicked.connect(self.n13)
    def y13(self):
        self.cs+=1
        self.mc+=1
        self.ec+=1
        self.ce+=1
        self.q14()
    def n13(self):
        self.bt+=1
        self.q14()
    
    def q14(self):
        self.l1.setText("Have you used any Linux distros before?")
        self.l1.setGeometry(QtCore.QRect(100, 260, 911, 81))        
        self.progressBar.setProperty("value", 14)
        self.by13.deleteLater()
        self.bn13.deleteLater()
        self.by14.setGeometry(QtCore.QRect(380, 440, 161, 61))
        self.by14.setObjectName("y")
        self.bn14.setGeometry(QtCore.QRect(548, 440, 161, 61))
        self.bn14.setObjectName("n")
        self.by14.setText("Yes")
        self.bn14.setText("No")
        self.by14.clicked.connect(self.y14)
        self.bn14.clicked.connect(self.n14)
    def y14(self):
        self.cs+=1
        self.mc+=1
        self.ec+=1
        self.q15()
    def n14(self):
        self.ce+=1
        self.bt+=1
        self.q15()

    def q15(self):
        self.l1.setText("Do you prioritze a high income over passion?")
        self.l1.setGeometry(QtCore.QRect(50, 260, 1021, 81))        
        self.progressBar.setProperty("value", 15)
        self.by14.deleteLater()
        self.bn14.deleteLater()
        self.by15.setGeometry(QtCore.QRect(380, 440, 161, 61))
        self.by15.setObjectName("y")
        self.bn15.setGeometry(QtCore.QRect(548, 440, 161, 61))
        self.bn15.setObjectName("n")
        self.by15.setText("Yes")
        self.bn15.setText("No")
        self.by15.clicked.connect(self.y15)
        self.bn15.clicked.connect(self.n15)
    def y15(self):
        self.cs+=1
        self.final()
    def n15(self):
        self.ce+=1
        self.mc+=1
        self.ec+=1
        self.cs+=1
        self.bt+=1
        self.final()

    def final(self):
        
        self.ls.append(self.cs)
        self.ls.append(self.ec)
        self.ls.append(self.ec)
        self.ls.append(self.bt)
        self.ls.append(self.mc)
        ls1=self.ls
        max1=max(ls1)
        ls2=["CS","EC","CE","BT","MC"]
        ind=ls1.index(max1)
        print(max1, ls2[ind])
        if ls2[ind]=="CS":
            self.finalcs()
        if ls2[ind]=="EC":
            self.finalec()
        if ls2[ind]=="MC":
            self.finalmc()
        if ls2[ind]=="CE":
            self.finalce()
        if ls2[ind]=="BT":
            self.finalbt()

    def finalcs(self):
        self.l1.deleteLater()
        self.by15.deleteLater()
        self.bn15.deleteLater()
        self.progressBar.deleteLater()
        self.lf1.setGeometry(QtCore.QRect(90, 260, 931, 81))
        self.lf1.setObjectName(u"lf1")
        self.lf1.setText("Computer Science Enginnering is the best choice!")
        font = QtGui.QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(25)
        self.lf1.setFont(font)
        self.lf2.setObjectName(u"lf2")
        self.lf2.setText("Thank you for using our product")
        self.lf2.setGeometry(QtCore.QRect(360, 490, 361, 41))
        font1 = QtGui.QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(15)
        self.lf2.setFont(font1)
        self.lf3.setObjectName(u"lf3")
        self.lf3.setText("Hope we were of help to you")
        self.lf3.setGeometry(QtCore.QRect(380, 530, 321, 41))
        self.lf3.setFont(font1)
    
    def finalec(self):
        self.l1.deleteLater()
        self.by15.deleteLater()
        self.bn15.deleteLater()
        self.progressBar.deleteLater()
        self.lf1.setGeometry(QtCore.QRect(90, 260, 951, 81))
        self.lf1.setObjectName(u"lf1")
        self.lf1.setText("Electronics/Comms Enginnering is the best choice!")
        font = QtGui.QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(25)
        self.lf1.setFont(font)
        self.lf2.setObjectName(u"lf2")
        self.lf2.setText("Thank you for using our product")
        self.lf2.setGeometry(QtCore.QRect(360, 490, 361, 41))
        font1 = QtGui.QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(15)
        self.lf2.setFont(font1)
        self.lf3.setObjectName(u"lf3")
        self.lf3.setText("Hope we were of help to you")
        self.lf3.setGeometry(QtCore.QRect(380, 530, 321, 41))
        self.lf3.setFont(font1)

    def finalmc(self):
        self.l1.deleteLater()
        self.by15.deleteLater()
        self.bn15.deleteLater()
        self.progressBar.deleteLater()
        self.lf1.setGeometry(QtCore.QRect(160, 260, 801, 81))
        self.lf1.setObjectName(u"lf1")
        self.lf1.setText("Mechanical Enginnering is the best choice!")
        font = QtGui.QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(25)
        self.lf1.setFont(font)
        self.lf2.setObjectName(u"lf2")
        self.lf2.setText("Thank you for using our product")
        self.lf2.setGeometry(QtCore.QRect(360, 490, 361, 41))
        font1 = QtGui.QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(15)
        self.lf2.setFont(font1)
        self.lf3.setObjectName(u"lf3")
        self.lf3.setText("Hope we were of help to you")
        self.lf3.setGeometry(QtCore.QRect(380, 530, 321, 41))
        self.lf3.setFont(font1)

    def finalce(self):
        self.l1.deleteLater()
        self.by15.deleteLater()
        self.bn15.deleteLater()
        self.progressBar.deleteLater()
        self.lf1.setGeometry(QtCore.QRect(230, 260, 671, 81))
        self.lf1.setObjectName(u"lf1")
        self.lf1.setText("Civil Enginnering is the best choice!")
        font = QtGui.QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(25)
        self.lf1.setFont(font)
        self.lf2.setObjectName(u"lf2")
        self.lf2.setText("Thank you for using our product")
        self.lf2.setGeometry(QtCore.QRect(360, 490, 361, 41))
        font1 = QtGui.QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(15)
        self.lf2.setFont(font1)
        self.lf3.setObjectName(u"lf3")
        self.lf3.setText("Hope we were of help to you")
        self.lf3.setGeometry(QtCore.QRect(380, 530, 321, 41))
        self.lf3.setFont(font1)
    
    def finalbt(self):
        self.l1.deleteLater()
        self.by15.deleteLater()
        self.bn15.deleteLater()
        self.progressBar.deleteLater()
        self.lf1.setGeometry(QtCore.QRect(200, 260, 731, 81))
        self.lf1.setObjectName(u"lf1")
        self.lf1.setText("Biotech Enginnering is the best choice!")
        font = QtGui.QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(25)
        self.lf1.setFont(font)
        self.lf2.setObjectName(u"lf2")
        self.lf2.setText("Thank you for using our product")
        self.lf2.setGeometry(QtCore.QRect(360, 490, 361, 41))
        font1 = QtGui.QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(15)
        self.lf2.setFont(font1)
        self.lf3.setObjectName(u"lf3")
        self.lf3.setText("Hope we were of help to you")
        self.lf3.setGeometry(QtCore.QRect(380, 530, 321, 41))
        self.lf3.setFont(font1)


import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
