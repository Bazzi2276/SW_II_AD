import sys
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QRadioButton
from PyQt5.QtCore import QSize
from qt_material import apply_stylesheet

from questions import Question

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
        firstPage = FirstPage()
        self.addWidget(firstPage)
        secondPage = SecondPage()
        self.addWidget(secondPage)

class FirstPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    # UI 설정
    def initUI(self):

        # title 부분 UI
        hTopBox = QHBoxLayout()
        titleLbl = QLabel('MBTI 검사지(미정)')
        hTopBox.addStretch(1)
        hTopBox.addWidget(titleLbl)
        hTopBox.addStretch(1)

        # 학번, 이름 입력 칸 UI
        hMiddle1Box = QHBoxLayout()
        numberLbl = QLabel('학번: ')
        self.numberEdit = QLineEdit()
        hMiddle1Box.addStretch(1)
        hMiddle1Box.addWidget(numberLbl)
        hMiddle1Box.addWidget(self.numberEdit)
        hMiddle1Box.addStretch(1)

        hMiddle2Box = QHBoxLayout()
        nameLbl = QLabel('이름: ')
        self.nameEdit = QLineEdit()
        hMiddle2Box.addStretch(1)
        hMiddle2Box.addWidget(nameLbl)
        hMiddle2Box.addWidget(self.nameEdit)
        hMiddle2Box.addStretch(1)
        
        # 다음 페이지 버튼 UI
        hBttomBox = QHBoxLayout()
        nextPageBtn = QPushButton("next")
        # nextPageBtn.setStyleSheet("color: blue;"
        #                       "background-color: #87CEFA;"
        #                       "border-style: dashed;"
        #                       "border-width: 3px;"
        #                       "border-color: #1E90FF")
        nextPageBtn.clicked.connect(self.secondPage)
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

    def secondPage(self):
        main.setCurrentIndex(main.currentIndex()+1) 

class SecondPage(QWidget):

    def __init__(self):
        super().__init__()
        self.question = Question()
        self.initUI()
        
    def initUI(self):

        vBox = QVBoxLayout()

        q1Lbl = QLabel(self.question.getQuestion())

        hTopBox = QHBoxLayout()
        y1Lbl = QLabel('동의')
        q1Btn1 = QRadioButton()
        q1Btn2 = QRadioButton()
        q1Btn3 = QRadioButton()
        q1Btn4 = QRadioButton()
        q1Btn5 = QRadioButton()
        n1Lbl = QLabel('비동의')
        hTopBox.addWidget(y1Lbl)
        hTopBox.addWidget(q1Btn1)
        hTopBox.addWidget(q1Btn2)
        hTopBox.addWidget(q1Btn3)
        hTopBox.addWidget(q1Btn4)
        hTopBox.addWidget(q1Btn5)
        hTopBox.addWidget(n1Lbl)

        q2Lbl = QLabel(self.question.getQuestion())

        hMiddleBox = QHBoxLayout()
        y2Lbl = QLabel('동의')
        q2Btn1 = QRadioButton()
        q2Btn2 = QRadioButton()
        q2Btn3 = QRadioButton()
        q2Btn4 = QRadioButton()
        q2Btn5 = QRadioButton()
        n2Lbl = QLabel('비동의')
        hMiddleBox.addWidget(y2Lbl)
        hMiddleBox.addWidget(q2Btn1)
        hMiddleBox.addWidget(q2Btn2)
        hMiddleBox.addWidget(q2Btn3)
        hMiddleBox.addWidget(q2Btn4)
        hMiddleBox.addWidget(q2Btn5)
        hMiddleBox.addWidget(n2Lbl)

        q3Lbl = QLabel(self.question.getQuestion())  

        hBottomBox = QHBoxLayout()
        y3Lbl = QLabel('동의')
        q3Btn1 = QRadioButton()
        q3Btn2 = QRadioButton()
        q3Btn3 = QRadioButton()
        q3Btn4 = QRadioButton()
        q3Btn5 = QRadioButton()
        n3Lbl = QLabel('비동의')
        hBottomBox.addWidget(y3Lbl)
        hBottomBox.addWidget(q3Btn1)
        hBottomBox.addWidget(q3Btn2)
        hBottomBox.addWidget(q3Btn3)
        hBottomBox.addWidget(q3Btn4)
        hBottomBox.addWidget(q3Btn5)
        hBottomBox.addWidget(n3Lbl)     
        
        vBox.addWidget(q1Lbl)
        vBox.addLayout(hTopBox)
        vBox.addWidget(q2Lbl)
        vBox.addLayout(hMiddleBox)
        vBox.addWidget(q3Lbl)
        vBox.addLayout(hBottomBox)

        self.setLayout(vBox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    app.exec_()

