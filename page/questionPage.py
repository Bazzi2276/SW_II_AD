from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, \
    QLineEdit, QRadioButton, QButtonGroup, QProgressBar, QGraphicsView, QGraphicsScene, QGraphicsProxyWidget
from PyQt5.QtCore import QSize, Qt
from qt_material import apply_stylesheet

from define.questions import Question
from define.determineMBTI import DetermineMBTI
from define.values import Values


class QuestionPage(QWidget):

    def __init__(self, main):
        super().__init__()
        self.question = Question()
        self.initUI()
        self.main = main

    def initUI(self):

        vBox = QVBoxLayout()

        # 첫 번째 질문과 버튼들

        self.q1LblIdx = self.question.getQuestionIdx()
        self.q1Lbl = QLabel(self.question.getQuestion())
        self.q1Lbl.setStyleSheet("font-family: 08서울남산체 EB; font-size: 15pt;")
        self.q1Lbl.setAlignment(Qt.AlignCenter)

        h1Box = QHBoxLayout()
        y1Lbl = QLabel('비동의')
        y1Lbl.setAlignment(Qt.AlignRight)
        y1Lbl.setStyleSheet("font-family: 08서울남산체 EB; font-size: 12pt;")
        q1Btn1 = QRadioButton()
        q1Btn1.setStyleSheet("QRadioButton::indicator"
                             "{width: 50px; height: 50px;}"
                             "QRadioButton::indicator::unchecked"       #버튼 클릭 X 시
                             "{image: url(C:/pyimage/radiobuttonDisagree_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:hover"  #버튼 위에 마우스가 올라가있을 시
                             "{image: url(C:/pyimage/radiobuttonDisagree_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:pressed"    #버튼 누를 때
                             "{image: url(C:/pyimage/radiobuttonDisagree_checked.png);}"
                             "QRadioButton::indicator::checked "            #버튼 클릭 됐을 때
                             "{image: url(C:/pyimage/radiobuttonDisagree_checked.png);}"
                             "QRadioButton::indicator:checked:hover "       #클릭된 버튼 위에 마우스가 올라갈 때
                             "{image: url(C:/pyimage/radiobuttonDisagree_checked.png);}"
                             "QRadioButton::indicator:checked:pressed "     #클릭된 버튼 클릭할 때
                             "{image: url(C:/pyimage/radiobuttonDisagree_checked.png);")

        q1Btn2 = QRadioButton()
        q1Btn2.setStyleSheet("QRadioButton::indicator"
                             "{width: 40px; height: 40px;}"
                             "QRadioButton::indicator::unchecked"  # 버튼 클릭 X 시
                             "{image: url(C:/pyimage/radiobuttonDisagree_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:hover"  # 버튼 위에 마우스가 올라가있을 시
                             "{image: url(C:/pyimage/radiobuttonDisagree_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:pressed"  # 버튼 누를 때
                             "{image: url(C:/pyimage/radiobuttonDisagree_checked.png);}"
                             "QRadioButton::indicator::checked "  # 버튼 클릭 됐을 때
                             "{image: url(C:/pyimage/radiobuttonDisagree_checked.png);}"
                             "QRadioButton::indicator:checked:hover "  # 클릭된 버튼 위에 마우스가 올라갈 때
                             "{image: url(C:/pyimage/radiobuttonDisagree_checked.png);}"
                             "QRadioButton::indicator:checked:pressed "  # 클릭된 버튼 클릭할 때
                             "{image: url(C:/pyimage/radiobuttonDisagree_checked.png);")
        q1Btn3 = QRadioButton()
        q1Btn3.setStyleSheet("QRadioButton::indicator"
                             "{width: 30px; height: 30px;}"
                             "QRadioButton::indicator::unchecked"  # 버튼 클릭 X 시
                             "{image: url(C:/pyimage/radiobuttonCenter_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:hover"  # 버튼 위에 마우스가 올라가있을 시
                             "{image: url(C:/pyimage/radiobuttonCenter_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:pressed"  # 버튼 누를 때
                             "{image: url(C:/pyimage/radiobuttonCenter_checked.png);}"
                             "QRadioButton::indicator::checked "  # 버튼 클릭 됐을 때
                             "{image: url(C:/pyimage/radiobuttonCenter_checked.png);}"
                             "QRadioButton::indicator:checked:hover "  # 클릭된 버튼 위에 마우스가 올라갈 때
                             "{image: url(C:/pyimage/radiobuttonCenter_checked.png);}"
                             "QRadioButton::indicator:checked:pressed "  # 클릭된 버튼 클릭할 때
                             "{image: url(C:/pyimage/radiobuttonCenter_checked.png);")

        q1Btn4 = QRadioButton()
        q1Btn4.setStyleSheet("QRadioButton::indicator"
                             "{width: 40px; height: 40px;}"
                             "QRadioButton::indicator::unchecked"  # 버튼 클릭 X 시
                             "{image: url(C:/pyimage/radiobuttonAgree_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:hover"  # 버튼 위에 마우스가 올라가있을 시
                             "{image: url(C:/pyimage/radiobuttonAgree_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:pressed"  # 버튼 누를 때
                             "{image: url(C:/pyimage/radiobuttonAgree_checked.png);}"
                             "QRadioButton::indicator::checked "  # 버튼 클릭 됐을 때
                             "{image: url(C:/pyimage/radiobuttonAgree_checked.png);}"
                             "QRadioButton::indicator:checked:hover "  # 클릭된 버튼 위에 마우스가 올라갈 때
                             "{image: url(C:/pyimage/radiobuttonAgree_checked.png);}"
                             "QRadioButton::indicator:checked:pressed "  # 클릭된 버튼 클릭할 때
                             "{image: url(C:/pyimage/radiobuttonAgree_checked.png);")

        q1Btn5 = QRadioButton()
        q1Btn5.setStyleSheet("QRadioButton::indicator"
                             "{width: 50px; height: 50px;}"
                             "QRadioButton::indicator::unchecked"  # 버튼 클릭 X 시
                             "{image: url(C:/pyimage/radiobuttonAgree_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:hover"  # 버튼 위에 마우스가 올라가있을 시
                             "{image: url(C:/pyimage/radiobuttonAgree_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:pressed"  # 버튼 누를 때
                             "{image: url(C:/pyimage/radiobuttonAgree_checked.png);}"
                             "QRadioButton::indicator::checked "  # 버튼 클릭 됐을 때
                             "{image: url(C:/pyimage/radiobuttonAgree_checked.png);}"
                             "QRadioButton::indicator:checked:hover "  # 클릭된 버튼 위에 마우스가 올라갈 때
                             "{image: url(C:/pyimage/radiobuttonAgree_checked.png);}"
                             "QRadioButton::indicator:checked:pressed "  # 클릭된 버튼 클릭할 때
                             "{image: url(C:/pyimage/radiobuttonAgree_checked.png);")


        self.q1group = QButtonGroup(self)
        self.q1group.addButton(q1Btn1, 0)
        self.q1group.addButton(q1Btn2, 1)
        self.q1group.addButton(q1Btn3, 2)
        self.q1group.addButton(q1Btn4, 3)
        self.q1group.addButton(q1Btn5, 4)
        n1Lbl = QLabel('동의')
        n1Lbl.setAlignment(Qt.AlignLeft)
        n1Lbl.setStyleSheet("font-family: 08서울남산체 EB; font-size: 12pt;")
        h1Box.addWidget(y1Lbl)
        h1Box.addWidget(q1Btn1)
        h1Box.addWidget(q1Btn2)
        h1Box.addWidget(q1Btn3)
        h1Box.addWidget(q1Btn4)
        h1Box.addWidget(q1Btn5)
        h1Box.addWidget(n1Lbl)

        # 두 번째 질문과 버튼들
        self.q2LblIdx = self.question.getQuestionIdx()
        self.q2Lbl = QLabel(self.question.getQuestion())
        self.q2Lbl.setStyleSheet("font-family: 08서울남산체 EB; font-size: 15pt;")
        self.q2Lbl.setAlignment(Qt.AlignCenter)

        h2Box = QHBoxLayout()
        y2Lbl = QLabel('비동의')
        y2Lbl.setAlignment(Qt.AlignRight)
        y2Lbl.setStyleSheet("font-family: 08서울남산체 EB; font-size: 12pt;")
        q2Btn1 = QRadioButton()
        q2Btn1.setStyleSheet("QRadioButton::indicator"
                             "{width: 50px; height: 50px;}"
                             "QRadioButton::indicator::unchecked"  # 버튼 클릭 X 시
                             "{image: url(C:/pyimage/radiobuttonDisagree_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:hover"  # 버튼 위에 마우스가 올라가있을 시
                             "{image: url(C:/pyimage/radiobuttonDisagree_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:pressed"  # 버튼 누를 때
                             "{image: url(C:/pyimage/radiobuttonDisagree_checked.png);}"
                             "QRadioButton::indicator::checked "  # 버튼 클릭 됐을 때
                             "{image: url(C:/pyimage/radiobuttonDisagree_checked.png);}"
                             "QRadioButton::indicator:checked:hover "  # 클릭된 버튼 위에 마우스가 올라갈 때
                             "{image: url(C:/pyimage/radiobuttonDisagree_checked.png);}"
                             "QRadioButton::indicator:checked:pressed "  # 클릭된 버튼 클릭할 때
                             "{image: url(C:/pyimage/radiobuttonDisagree_checked.png);")

        q2Btn2 = QRadioButton()
        q2Btn2.setStyleSheet("QRadioButton::indicator"
                             "{width: 40px; height: 40px;}"
                             "QRadioButton::indicator::unchecked"  # 버튼 클릭 X 시
                             "{image: url(C:/pyimage/radiobuttonDisagree_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:hover"  # 버튼 위에 마우스가 올라가있을 시
                             "{image: url(C:/pyimage/radiobuttonDisagree_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:pressed"  # 버튼 누를 때
                             "{image: url(C:/pyimage/radiobuttonDisagree_checked.png);}"
                             "QRadioButton::indicator::checked "  # 버튼 클릭 됐을 때
                             "{image: url(C:/pyimage/radiobuttonDisagree_checked.png);}"
                             "QRadioButton::indicator:checked:hover "  # 클릭된 버튼 위에 마우스가 올라갈 때
                             "{image: url(C:/pyimage/radiobuttonDisagree_checked.png);}"
                             "QRadioButton::indicator:checked:pressed "  # 클릭된 버튼 클릭할 때
                             "{image: url(C:/pyimage/radiobuttonDisagree_checked.png);")

        q2Btn3 = QRadioButton()
        q2Btn3.setStyleSheet("QRadioButton::indicator"
                             "{width: 30px; height: 30px;}"
                             "QRadioButton::indicator::unchecked"  # 버튼 클릭 X 시
                             "{image: url(C:/pyimage/radiobuttonCenter_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:hover"  # 버튼 위에 마우스가 올라가있을 시
                             "{image: url(C:/pyimage/radiobuttonCenter_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:pressed"  # 버튼 누를 때
                             "{image: url(C:/pyimage/radiobuttonCenter_checked.png);}"
                             "QRadioButton::indicator::checked "  # 버튼 클릭 됐을 때
                             "{image: url(C:/pyimage/radiobuttonCenter_checked.png);}"
                             "QRadioButton::indicator:checked:hover "  # 클릭된 버튼 위에 마우스가 올라갈 때
                             "{image: url(C:/pyimage/radiobuttonCenter_checked.png);}"
                             "QRadioButton::indicator:checked:pressed "  # 클릭된 버튼 클릭할 때
                             "{image: url(C:/pyimage/radiobuttonCenter_checked.png);")

        q2Btn4 = QRadioButton()
        q2Btn4.setStyleSheet("QRadioButton::indicator"
                             "{width: 40px; height: 40px;}"
                             "QRadioButton::indicator::unchecked"  # 버튼 클릭 X 시
                             "{image: url(C:/pyimage/radiobuttonAgree_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:hover"  # 버튼 위에 마우스가 올라가있을 시
                             "{image: url(C:/pyimage/radiobuttonAgree_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:pressed"  # 버튼 누를 때
                             "{image: url(C:/pyimage/radiobuttonAgree_checked.png);}"
                             "QRadioButton::indicator::checked "  # 버튼 클릭 됐을 때
                             "{image: url(C:/pyimage/radiobuttonAgree_checked.png);}"
                             "QRadioButton::indicator:checked:hover "  # 클릭된 버튼 위에 마우스가 올라갈 때
                             "{image: url(C:/pyimage/radiobuttonAgree_checked.png);}"
                             "QRadioButton::indicator:checked:pressed "  # 클릭된 버튼 클릭할 때
                             "{image: url(C:/pyimage/radiobuttonAgree_checked.png);")

        q2Btn5 = QRadioButton()
        q2Btn5.setStyleSheet("QRadioButton::indicator"
                             "{width: 50px; height: 50px;}"
                             "QRadioButton::indicator::unchecked"  # 버튼 클릭 X 시
                             "{image: url(C:/pyimage/radiobuttonAgree_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:hover"  # 버튼 위에 마우스가 올라가있을 시
                             "{image: url(C:/pyimage/radiobuttonAgree_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:pressed"  # 버튼 누를 때
                             "{image: url(C:/pyimage/radiobuttonAgree_checked.png);}"
                             "QRadioButton::indicator::checked "  # 버튼 클릭 됐을 때
                             "{image: url(C:/pyimage/radiobuttonAgree_checked.png);}"
                             "QRadioButton::indicator:checked:hover "  # 클릭된 버튼 위에 마우스가 올라갈 때
                             "{image: url(C:/pyimage/radiobuttonAgree_checked.png);}"
                             "QRadioButton::indicator:checked:pressed "  # 클릭된 버튼 클릭할 때
                             "{image: url(C:/pyimage/radiobuttonAgree_checked.png);")


        self.q2group = QButtonGroup(self)
        self.q2group.addButton(q2Btn1, 0)
        self.q2group.addButton(q2Btn2, 1)
        self.q2group.addButton(q2Btn3, 2)
        self.q2group.addButton(q2Btn4, 3)
        self.q2group.addButton(q2Btn5, 4)
        n2Lbl = QLabel('동의')
        n2Lbl.setAlignment(Qt.AlignLeft)
        n2Lbl.setStyleSheet("font-family: 08서울남산체 EB; font-size: 12pt;")
        h2Box.addWidget(y2Lbl)
        h2Box.addWidget(q2Btn1)
        h2Box.addWidget(q2Btn2)
        h2Box.addWidget(q2Btn3)
        h2Box.addWidget(q2Btn4)
        h2Box.addWidget(q2Btn5)
        h2Box.addWidget(n2Lbl)

        # 세 번째 질문과 버튼들
        self.q3LblIdx = self.question.getQuestionIdx()
        self.q3Lbl = QLabel(self.question.getQuestion())
        self.q3Lbl.setStyleSheet("font-family: 08서울남산체 EB; font-size: 15pt;")
        self.q3Lbl.setAlignment(Qt.AlignCenter)


        h3Box = QHBoxLayout()
        y3Lbl = QLabel('비동의')
        y3Lbl.setAlignment(Qt.AlignRight)
        y3Lbl.setStyleSheet("font-family: 08서울남산체 EB; font-size: 12pt;")
        q3Btn1 = QRadioButton()
        q3Btn1.setStyleSheet("QRadioButton::indicator"
                             "{width: 50px; height: 50px;}"
                             "QRadioButton::indicator::unchecked"  # 버튼 클릭 X 시
                             "{image: url(C:/pyimage/radiobuttonDisagree_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:hover"  # 버튼 위에 마우스가 올라가있을 시
                             "{image: url(C:/pyimage/radiobuttonDisagree_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:pressed"  # 버튼 누를 때
                             "{image: url(C:/pyimage/radiobuttonDisagree_checked.png);}"
                             "QRadioButton::indicator::checked "  # 버튼 클릭 됐을 때
                             "{image: url(C:/pyimage/radiobuttonDisagree_checked.png);}"
                             "QRadioButton::indicator:checked:hover "  # 클릭된 버튼 위에 마우스가 올라갈 때
                             "{image: url(C:/pyimage/radiobuttonDisagree_checked.png);}"
                             "QRadioButton::indicator:checked:pressed "  # 클릭된 버튼 클릭할 때
                             "{image: url(C:/pyimage/radiobuttonDisagree_checked.png);")

        q3Btn2 = QRadioButton()
        q3Btn2.setStyleSheet("QRadioButton::indicator"
                             "{width: 40px; height: 40px;}"
                             "QRadioButton::indicator::unchecked"  # 버튼 클릭 X 시
                             "{image: url(C:/pyimage/radiobuttonDisagree_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:hover"  # 버튼 위에 마우스가 올라가있을 시
                             "{image: url(C:/pyimage/radiobuttonDisagree_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:pressed"  # 버튼 누를 때
                             "{image: url(C:/pyimage/radiobuttonDisagree_checked.png);}"
                             "QRadioButton::indicator::checked "  # 버튼 클릭 됐을 때
                             "{image: url(C:/pyimage/radiobuttonDisagree_checked.png);}"
                             "QRadioButton::indicator:checked:hover "  # 클릭된 버튼 위에 마우스가 올라갈 때
                             "{image: url(C:/pyimage/radiobuttonDisagree_checked.png);}"
                             "QRadioButton::indicator:checked:pressed "  # 클릭된 버튼 클릭할 때
                             "{image: url(C:/pyimage/radiobuttonDisagree_checked.png);")

        q3Btn3 = QRadioButton()
        q3Btn3.setStyleSheet("QRadioButton::indicator"
                             "{width: 30px; height: 30px;}"
                             "QRadioButton::indicator::unchecked"  # 버튼 클릭 X 시
                             "{image: url(C:/pyimage/radiobuttonCenter_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:hover"  # 버튼 위에 마우스가 올라가있을 시
                             "{image: url(C:/pyimage/radiobuttonCenter_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:pressed"  # 버튼 누를 때
                             "{image: url(C:/pyimage/radiobuttonCenter_checked.png);}"
                             "QRadioButton::indicator::checked "  # 버튼 클릭 됐을 때
                             "{image: url(C:/pyimage/radiobuttonCenter_checked.png);}"
                             "QRadioButton::indicator:checked:hover "  # 클릭된 버튼 위에 마우스가 올라갈 때
                             "{image: url(C:/pyimage/radiobuttonCenter_checked.png);}"
                             "QRadioButton::indicator:checked:pressed "  # 클릭된 버튼 클릭할 때
                             "{image: url(C:/pyimage/radiobuttonCenter_checked.png);")

        q3Btn4 = QRadioButton()
        q3Btn4.setStyleSheet("QRadioButton::indicator"
                             "{width: 40px; height: 40px;}"
                             "QRadioButton::indicator::unchecked"  # 버튼 클릭 X 시
                             "{image: url(C:/pyimage/radiobuttonAgree_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:hover"  # 버튼 위에 마우스가 올라가있을 시
                             "{image: url(C:/pyimage/radiobuttonAgree_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:pressed"  # 버튼 누를 때
                             "{image: url(C:/pyimage/radiobuttonAgree_checked.png);}"
                             "QRadioButton::indicator::checked "  # 버튼 클릭 됐을 때
                             "{image: url(C:/pyimage/radiobuttonAgree_checked.png);}"
                             "QRadioButton::indicator:checked:hover "  # 클릭된 버튼 위에 마우스가 올라갈 때
                             "{image: url(C:/pyimage/radiobuttonAgree_checked.png);}"
                             "QRadioButton::indicator:checked:pressed "  # 클릭된 버튼 클릭할 때
                             "{image: url(C:/pyimage/radiobuttonAgree_checked.png);")

        q3Btn5 = QRadioButton()
        q3Btn5.setStyleSheet("QRadioButton::indicator"
                             "{width: 50px; height: 50px;}"
                             "QRadioButton::indicator::unchecked"  # 버튼 클릭 X 시
                             "{image: url(C:/pyimage/radiobuttonAgree_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:hover"  # 버튼 위에 마우스가 올라가있을 시
                             "{image: url(C:/pyimage/radiobuttonAgree_unchecked.png);}"
                             "QRadioButton::indicator:unchecked:pressed"  # 버튼 누를 때
                             "{image: url(C:/pyimage/radiobuttonAgree_checked.png);}"
                             "QRadioButton::indicator::checked "  # 버튼 클릭 됐을 때
                             "{image: url(C:/pyimage/radiobuttonAgree_checked.png);}"
                             "QRadioButton::indicator:checked:hover "  # 클릭된 버튼 위에 마우스가 올라갈 때
                             "{image: url(C:/pyimage/radiobuttonAgree_checked.png);}"
                             "QRadioButton::indicator:checked:pressed "  # 클릭된 버튼 클릭할 때
                             "{image: url(C:/pyimage/radiobuttonAgree_checked.png);")

        self.q3group = QButtonGroup(self)
        self.q3group.addButton(q3Btn1, 0)
        self.q3group.addButton(q3Btn2, 1)
        self.q3group.addButton(q3Btn3, 2)
        self.q3group.addButton(q3Btn4, 3)
        self.q3group.addButton(q3Btn5, 4)
        n3Lbl = QLabel('동의')
        n3Lbl.setAlignment(Qt.AlignLeft)
        n3Lbl.setStyleSheet("font-family: 08서울남산체 EB; font-size: 12pt;" )
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
        nextPageBtn.setStyleSheet("font-family: 08서울남산체 EB; font-size: 12pt;" )
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

        # 모든 항목을 체크했을 때 다음 페이지로 넘어가게 하기 위한 설정
        if self.q1group.checkedButton() == None or self.q2group.checkedButton() == None or self.q3group.checkedButton() == None:
            return

        # 현재 페이지의 질문 결과 저장
        self.main.determineMBTI.mbtiSum(self.q1LblIdx, self.q1group.checkedId())
        self.main.determineMBTI.mbtiSum(self.q2LblIdx, self.q2group.checkedId())
        self.main.determineMBTI.mbtiSum(self.q3LblIdx, self.q3group.checkedId())

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

        # 모든 설문지를 완성했을 때 다음 페이지로 넘어가기 위한 설정
        if self.question.getQuestionIdx() == 48:
            self.main.resultPage.setMBTI(self.main.determineMBTI.mbtiCalc())
            self.main.setCurrentIndex(self.main.currentIndex() + 1)
            return

        # 질문지 업데이트
        self.q1LblIdx = self.question.getQuestionIdx()
        self.q1Lbl.setText(self.question.getQuestion())
        self.q2LblIdx = self.question.getQuestionIdx()
        self.q2Lbl.setText(self.question.getQuestion())
        self.q3LblIdx = self.question.getQuestionIdx()
        self.q3Lbl.setText(self.question.getQuestion())

