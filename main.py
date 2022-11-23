import sys
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QRadioButton, QButtonGroup, QProgressBar, QGraphicsView, QGraphicsScene, QGraphicsProxyWidget
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont, QFontDatabase
from qt_material import apply_stylesheet

from define.questions import Question
from define.determineMBTI import DetermineMBTI
from define.values import Values

from page.namePage import NamePage
from page.questionPage import QuestionPage
from page.agreementPage import AgreementPage
from page.resultPage import ResultPage

class Main(QStackedWidget):
    def __init__(self):
        super().__init__()
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
        namePage = NamePage(main)
        self.addWidget(namePage)
        questionPage = QuestionPage(main)
        self.addWidget(questionPage)
        self.agreementPage = AgreementPage(main)
        self.determineMBTI = DetermineMBTI()
        self.values = Values()
        self.addWidget(self.agreementPage)
        self.resultPage = ResultPage(main)
        self.addWidget(self.resultPage)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    fontDB = QFontDatabase()
    fontDB.addApplicationFont('SeoulNamsanEB.ttf')
    fontDB.addApplicationFont('SeoulNamsanB.ttf')

    main = Main()
    main.add()
    app.exec_()

