import sys
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QRadioButton, QButtonGroup, QProgressBar, QGraphicsView, QGraphicsScene, QGraphicsProxyWidget
from PyQt5.QtCore import QSize, Qt
from qt_material import apply_stylesheet

from questions import Question
from determineMBTI import DetermineMBTI
from values import Values

class Main(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.add()
        self.initUI()
        self.show()

    # UI 설정
    def initUI(self):
        self.move(600,100)
        self.setFixedSize(QSize(800, 900))
        self.setWindowTitle('MBTI 검사지(아직 미정)')
        apply_stylesheet(app, theme = 'light_pink.xml')
    
    # stack에 다른 페이지들 추가
    def add(self):
        namePage = NamePage()
        self.addWidget(namePage)
        questionPage = QuestionPage()
        self.addWidget(questionPage)
        self.agreementPage = AgreementPage()
        self.determineMBTI = DetermineMBTI()
        self.values = Values()
        self.addWidget(self.agreementPage)
        self.resultPage = ResultPage()
        self.addWidget(self.resultPage)

class NamePage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    # UI 설정
    def initUI(self):

        
        hTopBox = QHBoxLayout()
        hMiddle1Box = QHBoxLayout()
        hMiddle2Box = QHBoxLayout()

        self.numberEdit = QLineEdit()
        self.nameEdit = QLineEdit()

        uiGroups = {
            'title' : {'layout': hTopBox, 'widget': [QLabel('MBTI 검사지(미정)')]},
            'number' : {'layout': hMiddle1Box, 'widget': [QLabel('학번: '), self.numberEdit]},
            'name': {'layout': hMiddle2Box, 'widget': [QLabel('이름: '), self.nameEdit]}
        }

        for label in uiGroups.keys():
            layout = uiGroups[label]['layout']
            layout.addStretch(1)
            for widget in uiGroups[label]['widget']:
                layout.addWidget(widget)
            layout.addStretch(1)

        # 다음 페이지 버튼 UI
        hBttomBox = QHBoxLayout()
        nextPageBtn = QPushButton("시작하기")
        # nextPageBtn.setStyleSheet("color: blue;"
        #                       "background-color: #87CEFA;"
        #                       "border-style: dashed;"
        #                       "border-width: 3px;"
        #                       "border-color: #1E90FF")
        nextPageBtn.clicked.connect(self.questionPage)
        hBttomBox.addStretch(1)
        hBttomBox.addWidget(nextPageBtn)

        # UI 위치 조정
        vBox= QVBoxLayout()
        vBox.addLayout(hTopBox)
        vBox.addStretch(1)
        vBox.addLayout(hMiddle1Box)
        vBox.addLayout(hMiddle2Box)
        vBox.addStretch(1)
        vBox.addLayout(hBttomBox)
        
        self.setLayout(vBox)

    def questionPage(self):
        if self.nameEdit.text() == '' or self.numberEdit.text() == '' :
            return
        main.setCurrentIndex(main.currentIndex()+1) 
        main.resultPage.setNameNumber(self.nameEdit.text(), self.numberEdit.text())

class QuestionPage(QWidget):

    def __init__(self):
        super().__init__()
        self.question = Question()
        self.initUI()
        
    def initUI(self):

        vBox = QVBoxLayout()

        #첫 번째 질문과 버튼들
        self.q1LblIdx = self.question.getQuestionIdx()
        self.q1Lbl = QLabel(self.question.getQuestion())

        h1Box = QHBoxLayout()
        y1Lbl = QLabel('비동의')
        q1Btn1 = QRadioButton()
        q1Btn2 = QRadioButton()
        q1Btn3 = QRadioButton()
        q1Btn4 = QRadioButton()
        q1Btn5 = QRadioButton()
        self.q1group = QButtonGroup(self)
        self.q1group.addButton(q1Btn1, 0)
        self.q1group.addButton(q1Btn2, 1)
        self.q1group.addButton(q1Btn3, 2)
        self.q1group.addButton(q1Btn4, 3)
        self.q1group.addButton(q1Btn5, 4)
        n1Lbl = QLabel('동의')
        h1Box.addWidget(y1Lbl)
        h1Box.addWidget(q1Btn1)
        h1Box.addWidget(q1Btn2)
        h1Box.addWidget(q1Btn3)
        h1Box.addWidget(q1Btn4)
        h1Box.addWidget(q1Btn5)
        h1Box.addWidget(n1Lbl)

        #두 번째 질문과 버튼들
        self.q2LblIdx = self.question.getQuestionIdx()
        self.q2Lbl = QLabel(self.question.getQuestion())

        h2Box = QHBoxLayout()
        y2Lbl = QLabel('비동의')
        q2Btn1 = QRadioButton()
        q2Btn2 = QRadioButton()
        q2Btn3 = QRadioButton()
        q2Btn4 = QRadioButton()
        q2Btn5 = QRadioButton()
        self.q2group = QButtonGroup(self)
        self.q2group.addButton(q2Btn1, 0)
        self.q2group.addButton(q2Btn2, 1)
        self.q2group.addButton(q2Btn3, 2)
        self.q2group.addButton(q2Btn4, 3)
        self.q2group.addButton(q2Btn5, 4)
        n2Lbl = QLabel('동의')
        h2Box.addWidget(y2Lbl)
        h2Box.addWidget(q2Btn1)
        h2Box.addWidget(q2Btn2)
        h2Box.addWidget(q2Btn3)
        h2Box.addWidget(q2Btn4)
        h2Box.addWidget(q2Btn5)
        h2Box.addWidget(n2Lbl)

        #세 번째 질문과 버튼들
        self.q3LblIdx = self.question.getQuestionIdx()
        self.q3Lbl = QLabel(self.question.getQuestion())  

        h3Box = QHBoxLayout()
        y3Lbl = QLabel('비동의')
        q3Btn1 = QRadioButton()
        q3Btn2 = QRadioButton()
        q3Btn3 = QRadioButton()
        q3Btn4 = QRadioButton()
        q3Btn5 = QRadioButton()
        self.q3group = QButtonGroup(self)
        self.q3group.addButton(q3Btn1, 0)
        self.q3group.addButton(q3Btn2, 1)
        self.q3group.addButton(q3Btn3, 2)
        self.q3group.addButton(q3Btn4, 3)
        self.q3group.addButton(q3Btn5, 4)
        n3Lbl = QLabel('동의')
        h3Box.addWidget(y3Lbl)
        h3Box.addWidget(q3Btn1)
        h3Box.addWidget(q3Btn2)
        h3Box.addWidget(q3Btn3)
        h3Box.addWidget(q3Btn4)
        h3Box.addWidget(q3Btn5)
        h3Box.addWidget(n3Lbl) 

        # next 페이지 버튼 UI
        hBttomBox = QHBoxLayout()
        nextPageBtn = QPushButton("next")
        nextPageBtn.clicked.connect(self.clickedNextButton)
        hBttomBox.addStretch(1)
        hBttomBox.addWidget(nextPageBtn)
        
        vBox.addWidget(self.q1Lbl)
        vBox.addLayout(h1Box)
        vBox.addWidget(self.q2Lbl)
        vBox.addLayout(h2Box)
        vBox.addWidget(self.q3Lbl)
        vBox.addLayout(h3Box)
        vBox.addLayout(hBttomBox)

        self.setLayout(vBox)
    
    def clickedNextButton(self):


        # 모든 설문지를 완성했을 때 다음 페이지로 넘어가기 위한 설정
        if self.question.getQuestionIdx() == 48:
            main.resultPage.setMBTI(main.determineMBTI.mbtiCalc())
            main.setCurrentIndex(main.currentIndex()+1) 
            return
        
        # 모든 항목을 체크했을 때 다음 페이지로 넘어가게 하기 위한 설정
        if self.q1group.checkedButton() == None or self.q2group.checkedButton() == None or self.q3group.checkedButton() == None:
            return

        # 현재 페이지의 질문 결과 저장
        main.determineMBTI.mbtiSum(self.q1LblIdx, self.q1group.checkedId())
        main.determineMBTI.mbtiSum(self.q2LblIdx, self.q2group.checkedId())
        main.determineMBTI.mbtiSum(self.q3LblIdx, self.q3group.checkedId())

        # 버튼 리셋
        # self.q1group.setExclusive(False)
        # self.q2group.setExclusive(False)
        # self.q3group.setExclusive(False) 
        # self.q1group.checkedButton().setChecked(False)
        # self.q2group.checkedButton().setChecked(False)
        # self.q3group.checkedButton().setChecked(False) 
        # self.q1group.setExclusive(True)
        # self.q2group.setExclusive(True)
        # self.q3group.setExclusive(True) 

        
        # 질문지 업데이트
        self.q1LblIdx = self.question.getQuestionIdx()
        self.q1Lbl.setText(self.question.getQuestion())
        self.q2LblIdx = self.question.getQuestionIdx()
        self.q2Lbl.setText(self.question.getQuestion())
        self.q3LblIdx = self.question.getQuestionIdx()
        self.q3Lbl.setText(self.question.getQuestion())


class AgreementPage(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        agreenentLbl = QLabel("실명 전체 공개에 동의하십니까?")

        hBox = QHBoxLayout()
        agreeBtn = QRadioButton('동의')
        disagreeBtn = QRadioButton('비동의')
        self.buttongroup = QButtonGroup(self)
        self.buttongroup.addButton(agreeBtn, 1)
        self.buttongroup.addButton(disagreeBtn, 2)
        hBox.addWidget(agreeBtn)
        hBox.addWidget(disagreeBtn)

        nextBtn = QPushButton('next')
        nextBtn.clicked.connect(self.resultPage)

        vBox = QVBoxLayout()
        vBox.addWidget(agreenentLbl)
        vBox.addLayout(hBox)
        vBox.addWidget(nextBtn)

        self.setLayout(vBox)

    #결과 페이지로 가기
    def resultPage(self):
        if self.buttongroup.checkedButton() == None:
            return

        if self.buttongroup.checkedId() == 2:
            main.resultPage.chanegenAnonymous()
        main.setCurrentIndex(main.currentIndex()+1) 

        main.resultPage.setDetermineMBTI()

class ResultPage(QWidget):
    def __init__(self):
        super().__init__()
        self.mbti = ''
        self.name = ''
        self.number = ''
        self.initUI()

    def initUI(self):
       
        vBox = QVBoxLayout()

        label1 = QLabel("당신의 성격 유형은 :")
        label1.setAlignment(Qt.AlignCenter)
        label1Font = label1.font()
        label1Font.setPointSize(20) 
        label1.setFont(label1Font)

        self.mbtiLbl = QLabel();
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

    def setDetermineMBTI(self):
        determineMBTI = main.determineMBTI

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

        self.suitedMbtiLbl_1.setText(main.values.findSuitedMBTI(self.mbti)[0])
        self.suitedMbtiLbl_2.setText(main.values.findSuitedMBTI(self.mbti)[1])
        self.celebrity1.setText(list(main.values.savedMBTI[main.values.findSuitedMBTI(self.mbti)[0]]["연예인"])[0])
        self.celebrity2.setText(list(main.values.savedMBTI[main.values.findSuitedMBTI(self.mbti)[1]]["연예인"])[0])
        #self.student1.setText(i for i in list(main.values.savedMBTI[main.values.findSuitedMBTI(self.mbti)[0]]["학생"]))
        #self.student2.setText(i for i in list(main.values.savedMBTI[main.values.findSuitedMBTI(self.mbti)[1]]["학생"]))
        self.student2.setText("응가")
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    app.exec_()

