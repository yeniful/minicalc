import sys

from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.uic import loadUiType

form_class = loadUiType("MiniCalc.ui")[0]
class CalcClass(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self,parent)
        self.setupUi(self)
        nums = [self.b0, self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9]
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

    def Nums(self):
        global num
        sender = self.sender()
        newNum = int(sender.text())
        setNum = str(newNum)
        if self.result.text() == "0":
            self.result.setText(setNum)
        else:
            self.result.setText(self.result.text()+setNum)

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

    def bDelClick(self):
        n=len(self.result.text())
        self.result.setText(self.result.text()[0:n-1])

    def bClearClick(self):
        self.result.setText("0")

    def bRunClick(self):
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

app=QApplication(sys.argv)
myWindow=CalcClass(None)
myWindow.show()
app.exec_()
