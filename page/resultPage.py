from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QRadioButton, QButtonGroup, QProgressBar, QGraphicsView, QGraphicsScene, QGraphicsProxyWidget
from PyQt5.QtCore import QSize, Qt
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

        label1 = QLabel("당신의 성격 유형은 :")
        label1.setAlignment(Qt.AlignCenter)
        label1Font = label1.font()
        label1Font.setPointSize(20) 
        label1.setFont(label1Font)

        self.mbtiLbl = QLabel()
        self.mbtiLbl.setAlignment(Qt.AlignCenter)
        mbtiLblFont = self.mbtiLbl.font()
        mbtiLblFont.setBold(True)
        mbtiLblFont.setPointSize(50)
        self.mbtiLbl.setFont(mbtiLblFont)


        self.eLbl = QLabel()
        self.iLbl = QLabel()
        self.pbar1 = QProgressBar()
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.eLbl)
        hbox1.addWidget(self.pbar1)
        hbox1.addWidget(self.iLbl)

        self.nLbl = QLabel()
        self.sLbl = QLabel()
        self.pbar2 = QProgressBar()
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.nLbl)
        hbox2.addWidget(self.pbar2)
        hbox2.addWidget(self.sLbl)

        self.tLbl = QLabel()
        self.fLbl = QLabel()
        self.pbar3 = QProgressBar()
        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.tLbl)
        hbox3.addWidget(self.pbar3)
        hbox3.addWidget(self.fLbl)

        self.jLbl = QLabel()
        self.pLbl = QLabel()
        self.pbar4 = QProgressBar()
        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.jLbl)
        hbox4.addWidget(self.pbar4)
        hbox4.addWidget(self.pLbl)

        label2 = QLabel("나와 잘맞는 MBTI:")
        label2.setAlignment(Qt.AlignCenter)
        label2Font = label2.font()
        label2Font.setPointSize(20) 
        label2Font.setBold(True)
        label2.setFont(label2Font)

        hbox5 = QHBoxLayout()
        self.suitedMbtiLbl_1 = QLabel()
        self.celebrity1 = QLabel()
        self.student1 = QLabel()
        hbox5.addStretch(1)
        hbox5.addWidget(self.suitedMbtiLbl_1)
        hbox5.addWidget(self.celebrity1)
        hbox5.addWidget(self.student1)
        hbox5.addStretch(1)
            
        hbox6 = QHBoxLayout()
        self.suitedMbtiLbl_2 = QLabel()
        self.celebrity2 = QLabel()
        self.student2 = QLabel()
        font = self.student2.font()
        font.setPointSize(30)
        self.student2.setFont(font)
        hbox6.addStretch(1)
        hbox6.addWidget(self.suitedMbtiLbl_2)
        hbox6.addWidget(self.celebrity2)
        hbox6.addWidget(self.student2)
        hbox6.addStretch(1)
        
        vBox.addWidget(label1)
        vBox.addWidget(self.mbtiLbl)
        vBox.addLayout(hbox1)
        vBox.addLayout(hbox2)
        vBox.addLayout(hbox3)
        vBox.addLayout(hbox4)
        vBox.addStretch(1)
        vBox.addWidget(label2)
        vBox.addStretch(1)
        vBox.addLayout(hbox5)
        vBox.addLayout(hbox6)
        vBox.addStretch(5)

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
        determineMBTI = self.main.determineMBTI

        ePercent = int((determineMBTI.sum1 / 52) * 100)
        iPercent = 100 - ePercent
        nPercent = int((determineMBTI.sum2 / 52) * 100)
        sPercent = 100 - nPercent
        tPercent = int((determineMBTI.sum3 / 52) * 100)
        fPercent = 100 - tPercent
        jPercent = int((determineMBTI.sum4 / 52) * 100)
        pPercent = 100 - jPercent

        self.iLbl.setText("I " + str(iPercent) + "%")
        self.eLbl.setText("E " + str(ePercent) + "%")
        self.nLbl.setText("N " + str(nPercent) + "%")
        self.sLbl.setText("S " + str(sPercent) + "%")
        self.tLbl.setText("T " + str(tPercent) + "%")
        self.fLbl.setText("F " + str(fPercent) + "%")
        self.jLbl.setText("J " + str(jPercent) + "%")
        self.pLbl.setText("P " + str(pPercent) + "%")

        self.pbar1.setValue(max(ePercent, iPercent))
        self.pbar1.setInvertedAppearance(ePercent < iPercent)
        self.pbar2.setValue(max(nPercent, sPercent))
        self.pbar2.setInvertedAppearance(nPercent < sPercent)
        self.pbar3.setValue(max(tPercent, fPercent))
        self.pbar3.setInvertedAppearance(tPercent < fPercent)
        self.pbar4.setValue(max(jPercent, pPercent))
        self.pbar4.setInvertedAppearance(jPercent < pPercent)

        self.suitedMbtiLbl_1.setText(self.main.values.findSuitedMBTI(self.mbti)[0])
        self.suitedMbtiLbl_2.setText(self.main.values.findSuitedMBTI(self.mbti)[1])
        self.celebrity1.setText(list(self.main.values.savedMBTI[self.main.values.findSuitedMBTI(self.mbti)[0]]["연예인"])[0])
        self.celebrity2.setText(list(self.main.values.savedMBTI[self.main.values.findSuitedMBTI(self.mbti)[1]]["연예인"])[0])
        #self.student1.setText(i for i in list(main.values.savedMBTI[main.values.findSuitedMBTI(self.mbti)[0]]["학생"]))
        #self.student2.setText(i for i in list(main.values.savedMBTI[main.values.findSuitedMBTI(self.mbti)[1]]["학생"]))
        self.student2.setText("응가")