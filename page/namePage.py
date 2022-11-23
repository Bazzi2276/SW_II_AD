from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QRadioButton, QButtonGroup, QProgressBar, QGraphicsView, QGraphicsScene, QGraphicsProxyWidget
from PyQt5.QtCore import QSize, Qt
from qt_material import apply_stylesheet

from define.questions import Question
from define.determineMBTI import DetermineMBTI
from define.values import Values

class NamePage(QWidget):
    def __init__(self, main):
        super().__init__()
        self.initUI()
        self.main = main
        
    
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
        self.main.setCurrentIndex(self.main.currentIndex()+1) 
        self.main.resultPage.setNameNumber(self.nameEdit.text(), self.numberEdit.text())