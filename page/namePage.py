from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QRadioButton, QButtonGroup, QProgressBar, QGraphicsView, QGraphicsScene, QGraphicsProxyWidget
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFontDatabase, QPixmap
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

        self.fdb = QFontDatabase()
        self.fdb.addApplicationFont('./SeoulNamsanB.ttf')
        self.fdb.addApplicationFont('./SeoulNamsanEB.ttf')
        
        hTopBox = QHBoxLayout()
        hContentBox = QHBoxLayout()
        hMiddleLeftBox = QHBoxLayout()
        hMiddle1Box = QHBoxLayout()
        hMiddle2Box = QHBoxLayout()

        self.numberEdit = QLineEdit()
        self.nameEdit = QLineEdit()

        uiGroups = {
            'title' : {'layout': hTopBox, 'widget': [QLabel('소융대 MBTI 검사')]},
            'content': {'layout': hContentBox, 'widget': [QLabel('<소융대 MBTI 검사>는\n자신의 MBTI와 잘 맞는 학부생을 찾을 수 있는\n소프트웨어 융합대학 학부생 전용 MBTI 검사입니다.')]},
            'koomin': {'layout': hMiddleLeftBox, 'widget': [QLabel()]},
            'number' : {'layout': hMiddle1Box, 'widget': [QLabel('학번: '), self.numberEdit]},
            'name': {'layout': hMiddle2Box, 'widget': [QLabel('이름: '), self.nameEdit]}
        }

        uiGroups['content']['widget'][0].setAlignment(Qt.AlignCenter)
        pixmap = QPixmap('pyimage/쿠민.JPG')
        pixmap = pixmap.scaledToWidth(self.width() // 2)
        uiGroups['koomin']['widget'][0].setPixmap(pixmap)
        uiGroups['koomin']['widget'][0].setStyleSheet('border: 1px solid lightgray;')

        # 폰트 변경
        uiGroups['title']['widget'][0].setStyleSheet('font-family: 서울남산체 EB; font-size: 40pt;')
        uiGroups['content']['widget'][0].setStyleSheet('font-family: 서울남산체 B; font-size: 15pt;')
        uiGroups['number']['widget'][0].setStyleSheet('font-family: 서울남산체 B; font-size: 15pt;')
        uiGroups['name']['widget'][0].setStyleSheet('font-family: 서울남산체 B; font-size: 15pt;')

        for label in uiGroups.keys():
            layout = uiGroups[label]['layout']
            layout.addStretch(1)
            for widget in uiGroups[label]['widget']:
                layout.addWidget(widget)
            layout.addStretch(1)

        hMiddleRightBox = QVBoxLayout()
        hMiddleRightBox.addStretch(1)
        hMiddleRightBox.addLayout(hMiddle1Box)
        hMiddleRightBox.addLayout(hMiddle2Box)
        hMiddleBox = QHBoxLayout()
        hMiddleBox.addStretch(1)
        hMiddleBox.addLayout(hMiddleLeftBox)
        hMiddleBox.addSpacing(20)
        hMiddleBox.addLayout(hMiddleRightBox)
        hMiddleBox.addStretch(1)

        # 다음 페이지 버튼 UI
        hBttomBox = QHBoxLayout()
        nextPageBtn = QPushButton("시작하기")
        nextPageBtn.setStyleSheet("font-family: 서울남산체 EB; font-size: 40pt;")
        nextPageBtn.setMinimumWidth(self.width() // 2)
        nextPageBtn.setMinimumHeight(nextPageBtn.height() // 3)
        # nextPageBtn.setStyleSheet("color: blue;"
        #                       "background-color: #87CEFA;"
        #                       "border-style: dashed;"
        #                       "border-width: 3px;"
        #                       "border-color: #1E90FF")
        nextPageBtn.clicked.connect(self.questionPage)
        hBttomBox.addStretch(1)
        hBttomBox.addWidget(nextPageBtn)
        hBttomBox.addStretch(1)

        # UI 위치 조정
        vBox= QVBoxLayout()
        vBox.addStretch(1)
        vBox.addLayout(hTopBox)
        vBox.addStretch(1)
        vBox.addLayout(hContentBox)
        vBox.addStretch(1)
        vBox.addLayout(hMiddleBox)
        vBox.addStretch(1)
        vBox.addLayout(hBttomBox)
        vBox.addStretch(1)
        
        self.setLayout(vBox)

    def questionPage(self):
        if self.nameEdit.text() == '' or self.numberEdit.text() == '' :
            return
        self.main.setCurrentIndex(self.main.currentIndex()+1) 
        self.main.resultPage.setNameNumber(self.nameEdit.text(), self.numberEdit.text())
