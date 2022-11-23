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
            self.main.resultPage.chanegenAnonymous()

        self.main.resultPage.setDetermineMBTI()        
        self.main.setCurrentIndex(self.main.currentIndex()+1)