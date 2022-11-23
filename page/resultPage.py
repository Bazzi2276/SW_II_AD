from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QRadioButton, QButtonGroup, QProgressBar, QGraphicsView, QGraphicsScene, QGraphicsProxyWidget
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont, QFontDatabase
from qt_material import apply_stylesheet

from define.questions import Question
from define.determineMBTI import DetermineMBTI
from define.values import Values

class ResultPage(QWidget):
    def __init__(self, main):
        super().__init__()
        self.mbti = ''
        self.name = ''
        self.number = ''
        self.main = main
        self.initUI()

    def initUI(self):
        vBox = QVBoxLayout()

        self.label1 = QLabel(f"NAME님의 성격 유형은 :")
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setStyleSheet("font-family: 08서울남산체 EB; font-size: 20pt;")

        self.mbtiLbl = QLabel()
        self.mbtiLbl.setAlignment(Qt.AlignCenter)
        self.mbtiLbl.setStyleSheet("font-family: 08서울남산체 EB; font-size: 30pt;" "font-style: bold;")

        self.eLbl = QLabel(self)
        self.eLbl.setStyleSheet("font-family: 08서울남산체 EB; font-size: 20pt;" "font-style: bold;")
        self.iLbl = QLabel(self)
        self.iLbl.setStyleSheet("font-family: 08서울남산체 EB; font-size: 20pt;" "font-style: bold;")
        self.pbar1 = QProgressBar(self)

        self.eLbl.move(30, 201)
        eLbl2 = QLabel('E(외향형)', self)
        eLbl2.setStyleSheet("font-family: 08서울남산체 EB; font-size: 12pt;" "font-style: bold;")
        eLbl2.move(100, 170)
        self.pbar1.setGeometry(100, 200, 600, 35)
        iLbl2 = QLabel('I(내향형)', self)
        iLbl2.setStyleSheet("font-family: 08서울남산체 EB; font-size: 12pt;" "font-style: bold;")
        iLbl2.move(640, 170)
        self.iLbl.move(710, 201)

        self.nLbl = QLabel(self)
        self.nLbl.setStyleSheet("font-family: 08서울남산체 EB; font-size: 20pt;" "font-style: bold;")
        self.sLbl = QLabel(self)
        self.sLbl.setStyleSheet("font-family: 08서울남산체 EB; font-size: 20pt;" "font-style: bold;")
        self.pbar2 = QProgressBar(self)

        self.nLbl.move(30, 266)
        nLbl2 = QLabel('N(직관형)', self)
        nLbl2.setStyleSheet("font-family: 08서울남산체 EB; font-size: 12pt;" "font-style: bold;")
        nLbl2.move(100, 235)
        self.pbar2.setGeometry(100, 265, 600, 35)
        sLbl2 = QLabel('S(현실형)', self)
        sLbl2.setStyleSheet("font-family: 08서울남산체 EB; font-size: 12pt;" "font-style: bold;")
        sLbl2.move(635, 235)
        self.sLbl.move(710, 266)

        self.tLbl = QLabel(self)
        self.tLbl.setStyleSheet("font-family: 08서울남산체 EB; font-size: 20pt;" "font-style: bold;")
        self.fLbl = QLabel(self)
        self.fLbl.setStyleSheet("font-family: 08서울남산체 EB; font-size: 20pt;" "font-style: bold;")
        self.pbar3 = QProgressBar(self)

        self.tLbl.move(30, 331)
        tLbl2 = QLabel('T(이성적)', self)
        tLbl2.setStyleSheet("font-family: 08서울남산체 EB; font-size: 12pt;" "font-style: bold;")
        tLbl2.move(100, 300)
        self.pbar3.setGeometry(100, 330, 600, 35)
        fLbl2 = QLabel('F(감정적)', self)
        fLbl2.setStyleSheet("font-family: 08서울남산체 EB; font-size: 12pt;" "font-style: bold;")
        fLbl2.move(635, 300)
        self.fLbl.move(710, 331)

        self.jLbl = QLabel(self)
        self.jLbl.setStyleSheet("font-family: 08서울남산체 EB; font-size: 20pt;" "font-style: bold;")
        self.pLbl = QLabel(self)
        self.pLbl.setStyleSheet("font-family: 08서울남산체 EB; font-size: 20pt;" "font-style: bold;")
        self.pbar4 = QProgressBar(self)

        self.jLbl.move(30, 396)
        jLbl2 = QLabel('J(계획형)', self)
        jLbl2.setStyleSheet("font-family: 08서울남산체 EB; font-size: 12pt;" "font-style: bold;")
        jLbl2.move(100, 365)
        self.pbar4.setGeometry(100, 395, 600, 35)
        pLbl2 = QLabel('P(자율적)', self)
        pLbl2.setStyleSheet("font-family: 08서울남산체 EB; font-size: 12pt;" "font-style: bold;")
        pLbl2.move(635, 365)
        self.pLbl.move(710, 396)

        label2 = QLabel("나와 잘맞는 MBTI:")
        label2.setAlignment(Qt.AlignCenter)
        label2.setStyleSheet("font-family: 08서울남산체 EB; font-size: 25pt;")

        hBox1 = QHBoxLayout()
        self.suitedMbtiLbl_1 = QLabel()
        self.suitedMbtiLbl_1.setStyleSheet("font-family: 08서울남산체 EB; font-size: 25pt;" "font-style: bold;")
        self.celebrity1 = QLabel()
        self.celebrity1.setStyleSheet("font-family: 08서울남산체 EB; font-size: 15pt; border-style: solid; border-width: 2px; border-color: #FF4081; border-radius: 3px;")
        self.celebrity1.setAlignment(Qt.AlignCenter)
        self.student1 = QLabel()
        self.student1.setStyleSheet("font-family: 08서울남산체 EB; font-size: 15pt; border-style: solid; border-width: 2px; border-color: #FF4081; border-radius: 3px;")
        self.student1.setAlignment(Qt.AlignCenter)
        hBox1.addStretch(3)
        hBox1.addWidget(self.suitedMbtiLbl_1)
        hBox1.addStretch(1)
        hBox1.addWidget(self.celebrity1)
        hBox1.addStretch(1)
        hBox1.addWidget(self.student1)
        hBox1.addStretch(5)
            
        hBox2 = QHBoxLayout()
        self.suitedMbtiLbl_2 = QLabel()
        self.suitedMbtiLbl_2.setStyleSheet("font-family: 08서울남산체 EB; font-size: 25pt;" "font-style: bold;")
        self.celebrity2 = QLabel()
        self.celebrity2.setStyleSheet("font-family: 08서울남산체 EB; font-size: 15pt; border-style: solid; border-width: 2px; border-color: #FF4081; border-radius: 3px;")
        self.celebrity2.setAlignment(Qt.AlignCenter)
        self.student2 = QLabel()
        self.student2.setStyleSheet("font-family: 08서울남산체 EB; font-size: 15pt; border-style: solid; border-width: 2px; border-color: #FF4081; border-radius: 3px;")
        self.student2.setAlignment(Qt.AlignCenter)
        hBox2.addStretch(3)
        hBox2.addWidget(self.suitedMbtiLbl_2)
        hBox2.addStretch(1)
        hBox2.addWidget(self.celebrity2)
        hBox2.addStretch(1)
        hBox2.addWidget(self.student2)
        hBox2.addStretch(5)
        
        vBox.addStretch(1)
        vBox.addWidget(self.label1)
        vBox.addStretch(1)
        vBox.addWidget(self.mbtiLbl)
        vBox.addStretch(12)
        vBox.addWidget(label2)
        vBox.addStretch(2)
        vBox.addLayout(hBox1)
        vBox.addStretch(1)
        vBox.addLayout(hBox2)
        vBox.addStretch(4)
        vBox.setAlignment(Qt.AlignCenter)

        self.setLayout(vBox)

    def setMBTI(self, mbti):
        self.mbti = mbti
        self.mbtiLbl.setText(mbti)
    
    def setNameNumber(self, name, number):
        self.name = name
        self.number = number

    def chanegenAnonymous(self):
        self.name = self.name[0] + "O" + self.name[2:]
        self.number = ''

    def setDetermineMBTI(self):
        self.main.values.saveStudentInfo(self.name, self.number, self.mbti)

        determineMBTI = self.main.determineMBTI

        self.label1.setText(f"{self.name}님의 성격 유형은 : ")

        ePercent = int((determineMBTI.sum1 / 48) * 100)
        iPercent = 100 - ePercent
        nPercent = int((determineMBTI.sum2 / 48) * 100)
        sPercent = 100 - nPercent
        tPercent = int((determineMBTI.sum3 / 48) * 100)
        fPercent = 100 - tPercent
        jPercent = int((determineMBTI.sum4 / 48) * 100)
        pPercent = 100 - jPercent


        self.eLbl.setText(str(ePercent) + "%")
        self.iLbl.setText(str(iPercent) + "%")
        self.nLbl.setText(str(nPercent) + "%")
        self.sLbl.setText(str(sPercent) + "%")
        self.tLbl.setText(str(tPercent) + "%")
        self.fLbl.setText(str(fPercent) + "%")
        self.jLbl.setText(str(jPercent) + "%")
        self.pLbl.setText(str(pPercent) + "%")

        self.pbar1.setValue(max(ePercent, iPercent))
        self.pbar1.setInvertedAppearance(ePercent < iPercent)
        self.pbar2.setValue(max(nPercent, sPercent))
        self.pbar2.setInvertedAppearance(nPercent < sPercent)
        self.pbar3.setValue(max(tPercent, fPercent))
        self.pbar3.setInvertedAppearance(tPercent < fPercent)
        self.pbar4.setValue(max(jPercent, pPercent))
        self.pbar4.setInvertedAppearance(jPercent < pPercent)

        self.suitedMbtiLbl_1.setText(self.main.values.findSuitedMBTI(self.mbti)[0] + " :")
        self.suitedMbtiLbl_2.setText(self.main.values.findSuitedMBTI(self.mbti)[1] + " :")
        self.celebrity1.setText("  " + list(self.main.values.savedMBTI[self.main.values.findSuitedMBTI(self.mbti)[0]]["연예인"])[0] + "  ")
        self.celebrity2.setText("  " + list(self.main.values.savedMBTI[self.main.values.findSuitedMBTI(self.mbti)[1]]["연예인"])[0] + "  ")

        s1 = [i for i in list(self.main.values.savedMBTI[self.main.values.findSuitedMBTI(self.mbti)[0]]["학생"])]
        for i in range(len(s1)):
            s1[i] =  self.main.values.savedNumber[s1[i]] + ' ' + s1[i]

        s2 = [i for i in list(self.main.values.savedMBTI[self.main.values.findSuitedMBTI(self.mbti)[1]]["학생"])]
        for i in range(len(s2)):
            s2[i] =  self.main.values.savedNumber[s2[i]] + ' ' + s2[i]
            
        self.student1.setText('\n' + '\n'.join(s1) + '\n')
        self.student2.setText("\n" + '\n'.join(s2) + "\n")