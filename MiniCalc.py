import sys
import math

from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.uic import loadUiType

form_class = loadUiType("MiniCalc.ui")[0]
class CalcClass(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        nums = [self.b0, self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9] # list로 받음
        for number in nums:
            number.clicked.connect(self.Nums)
        self.bDel.clicked.connect(self.bDelClick)
        self.bClear.clicked.connect(self.bClearClick)
        self.bRun.clicked.connect(self.bRunClick)
        self.bPlus.clicked.connect(self.bPlusClick)
        self.bMinus.clicked.connect(self.bMinusClick)
        self.bMult.clicked.connect(self.bMultClick)
        self.bDivide.clicked.connect(self.bDevideClick)
        self.bDot.clicked.connect(self.bDotClick)
        self.b00.clicked.connect(self.b00Click) #
        self.bSqrt.clicked.connect(self.bSqrtClick) #
        self.bRoundBracketLeft.clicked.connect(self.bRoundBracketLeftClick) #
        self.bRoundBracketRight.clicked.connect(self.bRoundBracketRightClick) #

    def Nums(self):
        global num
        sender = self.sender() # sender는 어떤 버튼이 클릭되었는지 정보 가져옴
        newNum = int(sender.text()) # 레이블 값을 가져와서 정수로 newMum에 넣어주고
        setNum = str(newNum) # 레이블 값을 스트링으로 바꾼 후 setNum에 넣어준다
        if self.result.text() == "0": # (처음에 맨 앞 숫자가) 0이면
            self.result.setText(setNum) #number를 써주고
        else: # 0이 아니면
            self.result.setText(self.result.text()+setNum) # 뒤에 붙여줌

    def bDotClick(self):
        self.result.setText(self.result.text()+".")
    def bPlusClick(self):
        self.result.setText(self.result.text()+"+")
    def bMinusClick(self):
        self.result.setText(self.result.text()+"-")
    def bDevideClick(self):
        self.result.setText(self.result.text()+"/")
    def bMultClick(self):
        self.result.setText(self.result.text()+"*")
    def b00Click(self):
        self.result.setText(self.result.text()+"00")
    def bRoundBracketLeftClick(self):
        self.result.setText(self.result.text()+"(")
    def bRoundBracketRightClick(self):
        self.result.setText(self.result.text()+")")


    def bDelClick(self): # delete 버튼 누르면 숫자 하나씩 지워지도록
        n = len(self.result.text()) # length로 배열 길이 counting 해서
        self.result.setText(self.result.text()[0:n-1]) # 마지막 숫자 하나 지워줌
        if self.result.text() == "": # 아무 숫자도 없으면
            self.result.setText("0") # 0이 뜨게

    def bClearClick(self):
        self.result.setText("0")

    def bSqrtClick(self):
        self.result.setText(str(math.sqrt(float(self.result.text()))))

    def bRunClick(self):
        """
        A=self.result.text()
         for i in range(0,len(A)):
            if str(A[i]) == ".": continue
            if str(A[i]).isdigit() == False:
                leftNum=float(str(A[0:i]))
                rightNum=float(str(A[i+1:len(A)]))
                if str(A[i]) == "+": self.result.setText(str(leftNum+rightNum))
                if str(A[i]) == "-": self.result.setText(str(leftNum-rightNum))
                if str(A[i]) == "*": self.result.setText(str(leftNum*rightNum))
                if str(A[i]) == "/": self.result.setText(str(leftNum/rightNum))
        """
        self.result.setText(str(eval(self.result.text())))


app = QApplication(sys.argv)
myWindow = CalcClass(None)
myWindow.show()
app.exec_()
