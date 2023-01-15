import sys

from PyQt5.Qt import *
from PyQt5 import QtGui
class Calc(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.my_input='0' #результат
        self.oper1=0 #первое число для операции
        self.oper2=0 #второе число для операции
        self.operation=''
    def initUI(self): #внешний вид калькулятора
        self.setGeometry(0,0,230,380)
        self.setWindowTitle('Калькулятор')
        self.setStyleSheet('background-color: pink')
        self.label = QLabel(self) #создаем поле для вывода результата
        self.label.setText('0') #установили начальное значение в окне
        self.label.resize(210,80) #установили размеры окна
        self.label.move(8,10)
        self.label.setStyleSheet('background-color: white')
        self.label.setFont(QtGui.QFont('SansSerif', 25))
        self.num1=QPushButton('1', self) #создали кнопку и дали ей название - имя
        self.num1.resize(50,50) #установили размер кнопки
        self.num1.move(5,100)
        self.num2 = QPushButton('2', self)
        self.num2.resize(50, 50)
        self.num2.move(60, 100)
        self.num3 = QPushButton('3', self)
        self.num3.resize(50, 50)
        self.num3.move(115, 100)
        self.num4 = QPushButton('4', self)
        self.num4.resize(50, 50)
        self.num4.move(5, 155)
        self.num5 = QPushButton('5', self)
        self.num5.resize(50, 50)
        self.num5.move(60, 155)
        self.num6 = QPushButton('6', self)
        self.num6.resize(50, 50)
        self.num6.move(115, 155)
        self.num7 = QPushButton('7', self)
        self.num7.resize(50, 50)
        self.num7.move(5, 210)
        self.num8 = QPushButton('8', self)
        self.num8.resize(50, 50)
        self.num8.move(60, 210)
        self.num9 = QPushButton('9', self)
        self.num9.resize(50, 50)
        self.num9.move(115, 210)
        self.num0 = QPushButton('0', self)
        self.num0.resize(50, 50)
        self.num0.move(5, 265)
        self.plus = QPushButton('+', self)
        self.plus.resize(50, 50)
        self.plus.move(170, 210)
        self.plus.setStyleSheet('background-color: yellow')
        self.minus = QPushButton('-', self)
        self.minus.resize(50, 50)
        self.minus.move(60, 265)
        self.minus.setStyleSheet('background-color: yellow')
        self.div = QPushButton('/', self)
        self.div.resize(50, 50)
        self.div.move(170, 100)
        self.div.setStyleSheet('background-color: yellow')
        self.mul = QPushButton('*', self)
        self.mul.resize(50, 50)
        self.mul.move(170, 155)
        self.mul.setStyleSheet('background-color: yellow')
        self.ravn = QPushButton('=', self)
        self.ravn.resize(50, 50)
        self.ravn.move(5, 320)
        self.ravn.setStyleSheet('background-color: orange')
        self.clear = QPushButton('C', self)
        self.clear.resize(105, 50)
        self.clear.move(115, 320)
        self.clear.setStyleSheet('background-color: grey')
        self.sqrt = QPushButton('√', self)
        self.sqrt.resize(50, 50)
        self.sqrt.move(170, 265)
        self.sqrt.setStyleSheet('background-color: yellow')
        self.sqr = QPushButton('a²', self)
        self.sqr.resize(50, 50)
        self.sqr.move(115, 265)
        self.sqr.setStyleSheet('background-color: yellow')
        self.ext = QPushButton('a^', self)
        self.ext.resize(50, 50)
        self.ext.move(60, 320)
        self.ext.setStyleSheet('background-color: yellow')

        self.num1.clicked.connect(self.one)
        self.num2.clicked.connect(self.two)
        self.num3.clicked.connect(self.three)
        self.num4.clicked.connect(self.four)
        self.num5.clicked.connect(self.five)
        self.num6.clicked.connect(self.six)
        self.num7.clicked.connect(self.seven)
        self.num8.clicked.connect(self.eight)
        self.num9.clicked.connect(self.nine)
        self.num0.clicked.connect(self.zero)
        self.plus.clicked.connect(self.plus_1)
        self.minus.clicked.connect(self.minus_1)
        self.div.clicked.connect(self.div_1)
        self.mul.clicked.connect(self.mul_1)
        self.clear.clicked.connect(self.clean)
        self.ravn.clicked.connect(self.ravn_1)
        self.sqrt.clicked.connect(self.sqroot)
        self.sqr.clicked.connect(self.sqr1)
        self.ext.clicked.connect(self.ext1)

    def enter_val(self):
        if self.label.text()=='0':
            self.label.setText('')
        self.label.setText(str(self.label.text())+str(self.my_input))

    def one(self):
        self.my_input=1
        self.enter_val()
    def two(self):
        self.my_input=2
        self.enter_val()
    def three(self):
        self.my_input=3
        self.enter_val()
    def four(self):
        self.my_input=4
        self.enter_val()
    def five(self):
        self.my_input=5
        self.enter_val()
    def six(self):
        self.my_input=6
        self.enter_val()
    def seven(self):
        self.my_input=7
        self.enter_val()
    def eight(self):
        self.my_input=8
        self.enter_val()
    def nine(self):
        self.my_input=9
        self.enter_val()
    def zero(self):
        self.my_input=0
        self.enter_val()
    def plus_1(self):
        self.operation='+'
        self.oper1=float(self.label.text())
        self.label.setText('0')
    def minus_1(self):
        self.operation='-'
        self.oper1=float(self.label.text())
        self.label.setText('0')
    def mul_1(self):
        self.operation='*'
        self.oper1=float(self.label.text())
        self.label.setText('0')
    def div_1(self):
        self.operation='/'
        self.oper1=float(self.label.text())
        self.label.setText('0')
    def clean(self):
        self.label.setText('0')
    def sqroot(self):
        self.operation='√'
        self.oper1=float(self.label.text())
        self.label.setText(str(self.oper1**0.5))
    def sqr1(self):
        self.operation='a²'
        self.oper1=float(self.label.text())
        self.label.setText(str(self.oper1*self.oper1))
    def ext1(self):
        self.operation='a^'
        self.oper1=float(self.label.text())
        self.label.setText('0')
    def ravn_1(self):
        self.oper2=float(self.label.text())
        if self.operation=='+':
            self.label.setText(str(self.oper1+self.oper2))
        if self.operation=='-':
            self.label.setText(str(self.oper1-self.oper2))
        if self.operation=='*':
            self.label.setText(str(self.oper1*self.oper2))
        if self.operation=='/':
            try:
                self.label.setText(str(self.oper1/self.oper2))
            except ZeroDivisionError:
                self.label.setText('Error')
        if self.operation=='a^':
            self.label.setText(str(self.oper1**self.oper2))
app=QApplication(sys.argv)
my_calc=Calc()
my_calc.show()
sys.exit(app.exec())


