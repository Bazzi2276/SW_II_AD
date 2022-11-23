from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QRadioButton, QButtonGroup, QProgressBar, QGraphicsView, QGraphicsScene, QGraphicsProxyWidget
from PyQt5.QtCore import QSize, Qt
from qt_material import apply_stylesheet

from define.questions import Question
from define.determineMBTI import DetermineMBTI
from define.values import Values

class AgreementPage(QWidget):

    def __init__(self, main):
        super().__init__()
        self.initUI()
        self.main = main
        
    def initUI(self):
        
        agreenentLbl = QLabel("실명 전체 공개에 동의하십니까?")
        agreenentLbl.setStyleSheet("font-family: 08서울남산체 EB; font-size: 40pt;" "font-style: bold;")
        agreenentLbl.setAlignment((Qt.AlignCenter))

        hBox = QHBoxLayout()
        agreeBtn = QRadioButton('동의')
        agreeBtn.setStyleSheet("QRadioButton::indicator""{""width : 100px;""height : 100px;""}")
        disagreeBtn = QRadioButton('비동의')
        disagreeBtn.setStyleSheet("QRadioButton::indicator""{""width : 100px;""height : 100px;""}")
        self.buttongroup = QButtonGroup(self)
        self.buttongroup.addButton(agreeBtn, 1)
        self.buttongroup.addButton(disagreeBtn, 2)
        hBox.addStretch(1)
        hBox.addWidget(agreeBtn)
        hBox.addStretch(1)
        hBox.addWidget(disagreeBtn)
        hBox.addStretch(1)

        explainLbl = QLabel('비동의 선택 시 \'나의 MBTI와 잘 맞는 학부생\' 이름 칸에\n <홍O동>처럼 이름이 부분 표시됩니다.\n 또한 학번에 대한 정보는 표시되지 않습니다.')
        explainLbl.setAlignment(Qt.AlignRight)
        explainLbl.setStyleSheet("font-family: 08서울남산체 EB; font-size: 15pt;" "font-style: bold;")

        h2Box = QHBoxLayout()
        nextBtn = QPushButton('next')
        nextBtn.clicked.connect(self.resultPage)
        h2Box.addStretch(1)
        h2Box.addWidget(nextBtn)

        vBox = QVBoxLayout()
        vBox.addStretch(2)
        vBox.addWidget(agreenentLbl)
        vBox.addStretch(2)
        vBox.addLayout(hBox)
        vBox.addStretch(1)
        vBox.addWidget(explainLbl)
        vBox.addStretch(4)
        vBox.addLayout(h2Box)

        self.setLayout(vBox)

    #결과 페이지로 가기
    def resultPage(self):
        if self.buttongroup.checkedButton() == None:
            return

        if self.buttongroup.checkedId() == 2:
            self.main.resultPage.chanegenAnonymous()

        self.main.resultPage.setDetermineMBTI()        
        self.main.setCurrentIndex(self.main.currentIndex()+1)