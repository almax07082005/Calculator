import sys
import PyQt5.QtWidgets as w
from PyQt5.QtGui import QFont, QColor, QIcon, QKeySequence
import math
import operator

sys.set_int_max_str_digits(2000000000)

def pow(a, b):
    if not a and not b:
        raise ValueError
    return a ** b


def root(a, b):
    if a < 0 or not b:
        raise ValueError
    return pow(a, 1 / b)


class MainWindow(w.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.BUTTON_SIZE = 70
        self.WINDOW_SIZE = 700
        self.FONT_SIZE = 13
        self.LABEL_SIZE = (self.WINDOW_SIZE, self.WINDOW_SIZE - 5 * self.BUTTON_SIZE)
        self.OPERATIONS = '+-%log_base n_root^fact()1/' + '\u00F7' + '\u00D7'
        self.DICT_OPERATIONS = {
            '+': operator.add,
            '-': operator.sub,
            '\u00D7': operator.mul,
            '\u00F7': operator.truediv,
            '%': operator.mod,
            '^': pow,
            'log_base': math.log,
            'n_root': root
        }

        self.setWindowTitle('Calculator')
        self.setGeometry(600, 200, self.WINDOW_SIZE, self.WINDOW_SIZE)
        self.setMinimumSize(self.WINDOW_SIZE, self.WINDOW_SIZE)
        self.setMaximumSize(self.WINDOW_SIZE, self.WINDOW_SIZE)
        self.setWindowIcon(QIcon('icon.ico'))

        self.button_0 = w.QPushButton('0', self)
        self.button_0.resize(self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.button_0.move(self.BUTTON_SIZE, self.WINDOW_SIZE - self.BUTTON_SIZE)
        self.button_0.setFont(QFont('Lucida Console', self.FONT_SIZE))
        self.button_0.clicked.connect(self.take_digit)
        self.button_0.setStyleSheet('background: #FFFFFF')

        self.button_1 = w.QPushButton('1', self)
        self.button_1.resize(self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.button_1.move(self.BUTTON_SIZE, self.WINDOW_SIZE - 2 * self.BUTTON_SIZE)
        self.button_1.setFont(QFont('Lucida Console', self.FONT_SIZE))
        self.button_1.clicked.connect(self.take_digit)
        self.button_1.setStyleSheet('background: #FFFFFF')

        self.button_2 = w.QPushButton('2', self)
        self.button_2.resize(self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.button_2.move(2 * self.BUTTON_SIZE, self.WINDOW_SIZE - 2 * self.BUTTON_SIZE)
        self.button_2.setFont(QFont('Lucida Console', self.FONT_SIZE))
        self.button_2.clicked.connect(self.take_digit)
        self.button_2.setStyleSheet('background: #FFFFFF')

        self.button_3 = w.QPushButton('3', self)
        self.button_3.resize(self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.button_3.move(3 * self.BUTTON_SIZE, self.WINDOW_SIZE - 2 * self.BUTTON_SIZE)
        self.button_3.setFont(QFont('Lucida Console', self.FONT_SIZE))
        self.button_3.clicked.connect(self.take_digit)
        self.button_3.setStyleSheet('background: #FFFFFF')

        self.button_4 = w.QPushButton('4', self)
        self.button_4.resize(self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.button_4.move(self.BUTTON_SIZE, self.WINDOW_SIZE - 3 * self.BUTTON_SIZE)
        self.button_4.setFont(QFont('Lucida Console', self.FONT_SIZE))
        self.button_4.clicked.connect(self.take_digit)
        self.button_4.setStyleSheet('background: #FFFFFF')

        self.button_5 = w.QPushButton('5', self)
        self.button_5.resize(self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.button_5.move(2 * self.BUTTON_SIZE, self.WINDOW_SIZE - 3 * self.BUTTON_SIZE)
        self.button_5.setFont(QFont('Lucida Console', self.FONT_SIZE))
        self.button_5.clicked.connect(self.take_digit)
        self.button_5.setStyleSheet('background: #FFFFFF')

        self.button_6 = w.QPushButton('6', self)
        self.button_6.resize(self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.button_6.move(3 * self.BUTTON_SIZE, self.WINDOW_SIZE - 3 * self.BUTTON_SIZE)
        self.button_6.setFont(QFont('Lucida Console', self.FONT_SIZE))
        self.button_6.clicked.connect(self.take_digit)
        self.button_6.setStyleSheet('background: #FFFFFF')

        self.button_7 = w.QPushButton('7', self)
        self.button_7.resize(self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.button_7.move(self.BUTTON_SIZE, self.WINDOW_SIZE - 4 * self.BUTTON_SIZE)
        self.button_7.setFont(QFont('Lucida Console', self.FONT_SIZE))
        self.button_7.clicked.connect(self.take_digit)
        self.button_7.setStyleSheet('background: #FFFFFF')

        self.button_8 = w.QPushButton('8', self)
        self.button_8.resize(self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.button_8.move(2 * self.BUTTON_SIZE, self.WINDOW_SIZE - 4 * self.BUTTON_SIZE)
        self.button_8.setFont(QFont('Lucida Console', self.FONT_SIZE))
        self.button_8.clicked.connect(self.take_digit)
        self.button_8.setStyleSheet('background: #FFFFFF')

        self.button_9 = w.QPushButton('9', self)
        self.button_9.resize(self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.button_9.move(3 * self.BUTTON_SIZE, self.WINDOW_SIZE - 4 * self.BUTTON_SIZE)
        self.button_9.setFont(QFont('Lucida Console', self.FONT_SIZE))
        self.button_9.clicked.connect(self.take_digit)
        self.button_9.setStyleSheet('background: #FFFFFF')

        self.button_sign = w.QPushButton('\u00B1', self)
        self.button_sign.resize(self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.button_sign.move(3 * self.BUTTON_SIZE, self.WINDOW_SIZE - self.BUTTON_SIZE)
        self.button_sign.setFont(QFont('Lucida Console', self.FONT_SIZE))
        self.button_sign.clicked.connect(self.sign)
        self.button_sign.setStyleSheet('background: #EBEBEB')

        self.button_dot = w.QPushButton('.', self)
        self.button_dot.resize(self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.button_dot.move(2 * self.BUTTON_SIZE, self.WINDOW_SIZE - self.BUTTON_SIZE)
        self.button_dot.setFont(QFont('Lucida Console', self.FONT_SIZE))
        self.button_dot.clicked.connect(self.dot)
        self.button_dot.setStyleSheet('background: #EBEBEB')

        self.button_equal = w.QPushButton('=', self)
        self.button_equal.resize(self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.button_equal.move(4 * self.BUTTON_SIZE, self.WINDOW_SIZE - self.BUTTON_SIZE)
        self.button_equal.setFont(QFont('Lucida Console', self.FONT_SIZE))
        self.button_equal.clicked.connect(self.equal)
        self.button_equal.setStyleSheet('background: #63A3FF')

        self.button_add = w.QPushButton('+', self)
        self.button_add.resize(self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.button_add.move(4 * self.BUTTON_SIZE, self.WINDOW_SIZE - 2 * self.BUTTON_SIZE)
        self.button_add.setFont(QFont('Lucida Console', self.FONT_SIZE))
        self.button_add.clicked.connect(self.operations)
        self.button_add.setStyleSheet('background: #EBEBEB')

        self.button_dif = w.QPushButton('-', self)
        self.button_dif.resize(self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.button_dif.move(4 * self.BUTTON_SIZE, self.WINDOW_SIZE - 3 * self.BUTTON_SIZE)
        self.button_dif.setFont(QFont('Lucida Console', self.FONT_SIZE))
        self.button_dif.clicked.connect(self.operations)
        self.button_dif.setStyleSheet('background: #EBEBEB')

        self.button_mult = w.QPushButton('\u00D7', self)
        self.button_mult.resize(self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.button_mult.move(4 * self.BUTTON_SIZE, self.WINDOW_SIZE - 4 * self.BUTTON_SIZE)
        self.button_mult.setFont(QFont('Lucida Console', self.FONT_SIZE))
        self.button_mult.clicked.connect(self.operations)
        self.button_mult.setStyleSheet('background: #EBEBEB')

        self.button_div = w.QPushButton('\u00F7', self)
        self.button_div.resize(self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.button_div.move(4 * self.BUTTON_SIZE, self.WINDOW_SIZE - 5 * self.BUTTON_SIZE)
        self.button_div.setFont(QFont('Lucida Console', self.FONT_SIZE))
        self.button_div.setStyleSheet('background: #EBEBEB')
        self.button_div.clicked.connect(self.operations)

        self.button_pop = w.QPushButton('\u232B', self)
        self.button_pop.resize(self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.button_pop.move(5 * self.BUTTON_SIZE, self.WINDOW_SIZE - 5 * self.BUTTON_SIZE)
        self.button_pop.setFont(QFont('Lucida Console', self.FONT_SIZE))
        self.button_pop.setStyleSheet('background: #CFCFCF')
        self.button_pop.clicked.connect(self.pop)

        self.button_erase = w.QPushButton('C', self)
        self.button_erase.resize(self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.button_erase.move(5 * self.BUTTON_SIZE, self.WINDOW_SIZE - 4 * self.BUTTON_SIZE)
        self.button_erase.setFont(QFont('Lucida Console', self.FONT_SIZE))
        self.button_erase.setStyleSheet('background: #CFCFCF')
        self.button_erase.clicked.connect(self.erase)

        self.button_mod = w.QPushButton('%', self)
        self.button_mod.resize(self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.button_mod.move(3 * self.BUTTON_SIZE, self.WINDOW_SIZE - 5 * self.BUTTON_SIZE)
        self.button_mod.setFont(QFont('Lucida Console', self.FONT_SIZE))
        self.button_mod.setStyleSheet('background: #EBEBEB')
        self.button_mod.clicked.connect(self.operations)

        self.button_factorial = w.QPushButton('x!', self)
        self.button_factorial.resize(self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.button_factorial.move(2 * self.BUTTON_SIZE, self.WINDOW_SIZE - 5 * self.BUTTON_SIZE)
        self.button_factorial.setFont(QFont('Lucida Console', self.FONT_SIZE))
        self.button_factorial.setStyleSheet('background: #EBEBEB')
        self.button_factorial.clicked.connect(self.factorial)

        self.button_reverse = w.QPushButton('\u00B9' + '\u2044' + '\u2093', self)
        self.button_reverse.resize(self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.button_reverse.move(self.BUTTON_SIZE, self.WINDOW_SIZE - 5 * self.BUTTON_SIZE)
        self.button_reverse.setFont(QFont('Lucida Console', self.FONT_SIZE))
        self.button_reverse.setStyleSheet('background: #EBEBEB')
        self.button_reverse.clicked.connect(self.reverse)

        self.button_root = w.QPushButton('\u207F' + '\u221A' + 'x', self)
        self.button_root.resize(self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.button_root.move(0, self.WINDOW_SIZE - 5 * self.BUTTON_SIZE)
        self.button_root.setFont(QFont('Lucida Console', self.FONT_SIZE))
        self.button_root.setStyleSheet('background: #EBEBEB')
        self.button_root.clicked.connect(self.root)

        self.button_pow = w.QPushButton('x' + '\u207F', self)
        self.button_pow.resize(self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.button_pow.move(0, self.WINDOW_SIZE - 4 * self.BUTTON_SIZE)
        self.button_pow.setFont(QFont('Lucida Console', self.FONT_SIZE))
        self.button_pow.setStyleSheet('background: #EBEBEB')
        self.button_pow.clicked.connect(self.pow)

        self.button_log = w.QPushButton('log' + '\u2090' + 'x', self)
        self.button_log.resize(self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.button_log.move(0, self.WINDOW_SIZE - 3 * self.BUTTON_SIZE)
        self.button_log.setFont(QFont('Lucida Console', self.FONT_SIZE - 2))
        self.button_log.setStyleSheet('background: #EBEBEB')
        self.button_log.clicked.connect(self.log)

        self.button_pi = w.QPushButton('\u03C0', self)
        self.button_pi.resize(self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.button_pi.move(0, self.WINDOW_SIZE - 2 * self.BUTTON_SIZE)
        self.button_pi.setFont(QFont('Lucida Console', self.FONT_SIZE))
        self.button_pi.setStyleSheet('background: #FFFFFF')
        self.button_pi.clicked.connect(self.pi)

        self.button_e = w.QPushButton('e', self)
        self.button_e.resize(self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.button_e.move(0, self.WINDOW_SIZE - self.BUTTON_SIZE)
        self.button_e.setFont(QFont('Lucida Console', self.FONT_SIZE))
        self.button_e.setStyleSheet('background: #FFFFFF')
        self.button_e.clicked.connect(self.e)

        self.shortcut_0 = w.QShortcut(QKeySequence('0'), self)
        self.shortcut_0.activated.connect(self.take_digit)

        self.shortcut_1 = w.QShortcut(QKeySequence('1'), self)
        self.shortcut_1.activated.connect(self.take_digit)

        self.shortcut_2 = w.QShortcut(QKeySequence('2'), self)
        self.shortcut_2.activated.connect(self.take_digit)

        self.shortcut_3 = w.QShortcut(QKeySequence('3'), self)
        self.shortcut_3.activated.connect(self.take_digit)

        self.shortcut_4 = w.QShortcut(QKeySequence('4'), self)
        self.shortcut_4.activated.connect(self.take_digit)

        self.shortcut_5 = w.QShortcut(QKeySequence('5'), self)
        self.shortcut_5.activated.connect(self.take_digit)

        self.shortcut_6 = w.QShortcut(QKeySequence('6'), self)
        self.shortcut_6.activated.connect(self.take_digit)

        self.shortcut_7 = w.QShortcut(QKeySequence('7'), self)
        self.shortcut_7.activated.connect(self.take_digit)

        self.shortcut_8 = w.QShortcut(QKeySequence('8'), self)
        self.shortcut_8.activated.connect(self.take_digit)

        self.shortcut_9 = w.QShortcut(QKeySequence('9'), self)
        self.shortcut_9.activated.connect(self.take_digit)

        self.shortcut_pop = w.QShortcut(QKeySequence('Backspace'), self)
        self.shortcut_pop.activated.connect(self.pop)

        self.shortcut_erase = w.QShortcut(QKeySequence('Escape'), self)
        self.shortcut_erase.activated.connect(self.erase)

        self.shortcut_equal = w.QShortcut(QKeySequence('Return'), self)
        self.shortcut_equal.activated.connect(self.equal)

        self.shortcut_equal2 = w.QShortcut(QKeySequence('='), self)
        self.shortcut_equal2.activated.connect(self.equal)

        self.shortcut_add = w.QShortcut(QKeySequence('+'), self)
        self.shortcut_add.activated.connect(self.operations)

        self.shortcut_dif = w.QShortcut(QKeySequence('-'), self)
        self.shortcut_dif.activated.connect(self.operations)

        self.shortcut_mult = w.QShortcut(QKeySequence('*'), self)
        self.shortcut_mult.activated.connect(self.operations)

        self.shortcut_div = w.QShortcut(QKeySequence('/'), self)
        self.shortcut_div.activated.connect(self.operations)

        self.shortcut_mod = w.QShortcut(QKeySequence('%'), self)
        self.shortcut_mod.activated.connect(self.operations)

        self.shortcut_sign = w.QShortcut(QKeySequence('S'), self)
        self.shortcut_sign.activated.connect(self.sign)

        self.shortcut_dot = w.QShortcut(QKeySequence('.'), self)
        self.shortcut_dot.activated.connect(self.dot)

        self.shortcut_pi = w.QShortcut(QKeySequence('P'), self)
        self.shortcut_pi.activated.connect(self.pi)

        self.shortcut_e = w.QShortcut(QKeySequence('E'), self)
        self.shortcut_e.activated.connect(self.e)

        self.shortcut_log = w.QShortcut(QKeySequence('L'), self)
        self.shortcut_log.activated.connect(self.log)

        self.shortcut_pow = w.QShortcut(QKeySequence('Ctrl+P'), self)
        self.shortcut_pow.activated.connect(self.pow)

        self.shortcut_root = w.QShortcut(QKeySequence('R'), self)
        self.shortcut_root.activated.connect(self.root)

        self.shortcut_reverse = w.QShortcut(QKeySequence('Ctrl+R'), self)
        self.shortcut_reverse.activated.connect(self.reverse)

        self.shortcut_factorial = w.QShortcut(QKeySequence('F'), self)
        self.shortcut_factorial.activated.connect(self.factorial)

        self.shortcut = w.QShortcut(QKeySequence('Alt+Return'), self)
        self.shortcut.activated.connect(self.shortcuts)

        self.screen = w.QTextBrowser(self)
        self.screen.setText('0')
        self.screen.resize(self.LABEL_SIZE[0], self.LABEL_SIZE[1])
        self.screen.move(0, 0)
        self.screen.setFont(QFont('Lucida Console', self.FONT_SIZE))
        self.screen.setStyleSheet('background-color: #F0F0F0; border-style: outset; border-width: 1px')

        self.second_screen = w.QTextBrowser(self)
        self.second_screen.setTextColor(QColor('#777777'))
        self.second_screen.resize(self.WINDOW_SIZE - 6 * self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.second_screen.move(6 * self.BUTTON_SIZE, 5 * self.BUTTON_SIZE)
        self.second_screen.setFont(QFont('Lucida Console', self.FONT_SIZE - 2))
        self.second_screen.setStyleSheet('background-color: #F0F0F0; border-style: outset; border-width: 1px')

        self.history = w.QTextBrowser(self)
        self.history.resize(self.WINDOW_SIZE - 5 * self.BUTTON_SIZE, 3 * self.BUTTON_SIZE)
        self.history.move(5 * self.BUTTON_SIZE, self.WINDOW_SIZE - 3 * self.BUTTON_SIZE)
        self.history.setFont(QFont('Lucida Console', self.FONT_SIZE))
        self.history.setStyleSheet('background-color: #F0F0F0; border-style: outset; border-width: 1px')

        self.information = w.QLabel('\u2191' + ' Current operation\nFor shortcuts \'Alt+Enter\'\n' + '\u2193' + ' History', self)
        self.information.resize(self.WINDOW_SIZE - 6 * self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.information.move(6 * self.BUTTON_SIZE, self.WINDOW_SIZE - 4 * self.BUTTON_SIZE)
        self.information.setFont(QFont('Lucida Console', self.FONT_SIZE - 2))
        self.information.setStyleSheet('color: #777777; background-color: #F0F0F0; border-style: outset; border-width: 1px')

    def shortcuts(self):
        if self.button_pop.text() == 'Backspace':
            self.button_0.setText('0')
            self.button_0.setFont(QFont('Lucida Console', self.FONT_SIZE))

            self.button_1.setText('1')
            self.button_1.setFont(QFont('Lucida Console', self.FONT_SIZE))

            self.button_2.setText('2')
            self.button_2.setFont(QFont('Lucida Console', self.FONT_SIZE))

            self.button_3.setText('3')
            self.button_3.setFont(QFont('Lucida Console', self.FONT_SIZE))

            self.button_4.setText('4')
            self.button_4.setFont(QFont('Lucida Console', self.FONT_SIZE))

            self.button_5.setText('5')
            self.button_5.setFont(QFont('Lucida Console', self.FONT_SIZE))

            self.button_6.setText('6')
            self.button_6.setFont(QFont('Lucida Console', self.FONT_SIZE))

            self.button_7.setText('7')
            self.button_7.setFont(QFont('Lucida Console', self.FONT_SIZE))

            self.button_8.setText('8')
            self.button_8.setFont(QFont('Lucida Console', self.FONT_SIZE))

            self.button_9.setText('9')
            self.button_9.setFont(QFont('Lucida Console', self.FONT_SIZE))

            self.button_sign.setText('-')
            self.button_sign.setFont(QFont('Lucida Console', self.FONT_SIZE))

            self.button_dot.setText('.')
            self.button_dot.setFont(QFont('Lucida Console', self.FONT_SIZE))

            self.button_equal.setText('=')
            self.button_equal.setFont(QFont('Lucida Console', self.FONT_SIZE))

            self.button_add.setText('+')
            self.button_add.setFont(QFont('Lucida Console', self.FONT_SIZE))

            self.button_dif.setText('-')
            self.button_dif.setFont(QFont('Lucida Console', self.FONT_SIZE))

            self.button_mult.setText('\u00D7')
            self.button_mult.setFont(QFont('Lucida Console', self.FONT_SIZE))

            self.button_div.setText('\u00F7')
            self.button_div.setFont(QFont('Lucida Console', self.FONT_SIZE))

            self.button_pop.setText('\u232B')
            self.button_pop.setFont(QFont('Lucida Console', self.FONT_SIZE))

            self.button_erase.setText('C')
            self.button_erase.setFont(QFont('Lucida Console', self.FONT_SIZE))

            self.button_mod.setText('%')
            self.button_mod.setFont(QFont('Lucida Console', self.FONT_SIZE))

            self.button_factorial.setText('x!')
            self.button_factorial.setFont(QFont('Lucida Console', self.FONT_SIZE))

            self.button_reverse.setText('\u00B9' + '\u2044' + '\u2093')
            self.button_reverse.setFont(QFont('Lucida Console', self.FONT_SIZE))

            self.button_root.setText('\u207F' + '\u221A' + 'x')
            self.button_root.setFont(QFont('Lucida Console', self.FONT_SIZE))

            self.button_pow.setText('x' + '\u207F')
            self.button_pow.setFont(QFont('Lucida Console', self.FONT_SIZE))

            self.button_log.setText('log' + '\u2090' + 'x')
            self.button_log.setFont(QFont('Lucida Console', self.FONT_SIZE - 2))

            self.button_pi.setText('\u03C0')
            self.button_pi.setFont(QFont('Lucida Console', self.FONT_SIZE))

            self.button_e.setText('e')
            self.button_e.setFont(QFont('Lucida Console', self.FONT_SIZE))
        else:
            self.button_0.setText(self.shortcut_0.key().toString())
            self.button_0.setFont(QFont('Lucida Console', self.FONT_SIZE - 4))

            self.button_1.setText(self.shortcut_1.key().toString())
            self.button_1.setFont(QFont('Lucida Console', self.FONT_SIZE - 4))

            self.button_2.setText(self.shortcut_2.key().toString())
            self.button_2.setFont(QFont('Lucida Console', self.FONT_SIZE - 4))

            self.button_3.setText(self.shortcut_3.key().toString())
            self.button_3.setFont(QFont('Lucida Console', self.FONT_SIZE - 4))

            self.button_4.setText(self.shortcut_4.key().toString())
            self.button_4.setFont(QFont('Lucida Console', self.FONT_SIZE - 4))

            self.button_5.setText(self.shortcut_5.key().toString())
            self.button_5.setFont(QFont('Lucida Console', self.FONT_SIZE - 4))

            self.button_6.setText(self.shortcut_6.key().toString())
            self.button_6.setFont(QFont('Lucida Console', self.FONT_SIZE - 4))

            self.button_7.setText(self.shortcut_7.key().toString())
            self.button_7.setFont(QFont('Lucida Console', self.FONT_SIZE - 4))

            self.button_8.setText(self.shortcut_8.key().toString())
            self.button_8.setFont(QFont('Lucida Console', self.FONT_SIZE - 4))

            self.button_9.setText(self.shortcut_9.key().toString())
            self.button_9.setFont(QFont('Lucida Console', self.FONT_SIZE - 4))

            self.button_pop.setText(self.shortcut_pop.key().toString())
            self.button_pop.setFont(QFont('Lucida Console', self.FONT_SIZE - 6))

            self.button_erase.setText(self.shortcut_erase.key().toString())
            self.button_erase.setFont(QFont('Lucida Console', self.FONT_SIZE - 4))

            self.button_equal.setText(self.shortcut_equal.key().toString() + '\n\n' + self.shortcut_equal2.key().toString())
            self.button_equal.setFont(QFont('Lucida Console', self.FONT_SIZE - 4))

            self.button_add.setText(self.shortcut_add.key().toString())
            self.button_add.setFont(QFont('Lucida Console', self.FONT_SIZE - 4))

            self.button_dif.setText(self.shortcut_dif.key().toString())
            self.button_dif.setFont(QFont('Lucida Console', self.FONT_SIZE - 4))

            self.button_mult.setText(self.shortcut_mult.key().toString())
            self.button_mult.setFont(QFont('Lucida Console', self.FONT_SIZE - 4))

            self.button_div.setText(self.shortcut_div.key().toString())
            self.button_div.setFont(QFont('Lucida Console', self.FONT_SIZE - 4))

            self.button_mod.setText(self.shortcut_mod.key().toString())
            self.button_mod.setFont(QFont('Lucida Console', self.FONT_SIZE - 4))

            self.button_sign.setText(self.shortcut_sign.key().toString())
            self.button_sign.setFont(QFont('Lucida Console', self.FONT_SIZE - 4))

            self.button_dot.setText(self.shortcut_dot.key().toString())
            self.button_dot.setFont(QFont('Lucida Console', self.FONT_SIZE - 4))

            self.button_pi.setText(self.shortcut_pi.key().toString())
            self.button_pi.setFont(QFont('Lucida Console', self.FONT_SIZE - 4))

            self.button_e.setText(self.shortcut_e.key().toString())
            self.button_e.setFont(QFont('Lucida Console', self.FONT_SIZE - 4))

            self.button_log.setText(self.shortcut_log.key().toString())
            self.button_log.setFont(QFont('Lucida Console', self.FONT_SIZE - 4))

            self.button_pow.setText(self.shortcut_pow.key().toString())
            self.button_pow.setFont(QFont('Lucida Console', self.FONT_SIZE - 4))

            self.button_root.setText(self.shortcut_root.key().toString())
            self.button_root.setFont(QFont('Lucida Console', self.FONT_SIZE - 4))

            self.button_reverse.setText(self.shortcut_reverse.key().toString())
            self.button_reverse.setFont(QFont('Lucida Console', self.FONT_SIZE - 4))

            self.button_factorial.setText(self.shortcut_factorial.key().toString())
            self.button_factorial.setFont(QFont('Lucida Console', self.FONT_SIZE - 4))

    def optim(self):
        if self.screen.toPlainText().find('.') == -1:
            return
        if all([self.screen.toPlainText()[self.screen.toPlainText().find('.') + 1:].find(i) == -1 for i in '123456789']):
            self.screen.setText(self.screen.toPlainText()[:self.screen.toPlainText().find('.')])

    def take_digit(self):
        current = self.sender()
        try:
            digit = current.key().toString()
        except:
            digit = current.text()
        self.screen.setText((self.screen.toPlainText()[1:] if self.screen.toPlainText() == '0' else self.screen.toPlainText()) + digit)

    def operations(self):
        if not all([i not in self.second_screen.toPlainText() for i in self.OPERATIONS]):
            return
        current = self.sender()
        try:
            oper = current.key().toString()
        except:
            oper = current.text()
        if oper == '*':
            oper = '\u00D7'
        elif oper == '/':
            oper = '\u00F7'
        self.optim()
        self.second_screen.setText(self.screen.toPlainText() + ' ' + oper + ' ')
        self.screen.setText('0')

    def e(self):
        self.screen.setText(str(math.e))

    def pi(self):
        self.screen.setText(str(math.pi))

    def log(self):
        if not all([i not in self.second_screen.toPlainText() for i in self.OPERATIONS]):
            return
        self.optim()
        if float(self.screen.toPlainText()) <= 0:
            self.screen.setText('Invalid input')
            return
        self.second_screen.setText(self.screen.toPlainText() + ' log_base ')
        self.screen.setText('0')

    def pow(self):
        if not all([i not in self.second_screen.toPlainText() for i in self.OPERATIONS]):
            return
        self.optim()
        self.second_screen.setText(self.screen.toPlainText() + ' ^ ')
        self.screen.setText('0')

    def root(self):
        if not all([i not in self.second_screen.toPlainText() for i in self.OPERATIONS]):
            return
        self.optim()
        if float(self.screen.toPlainText()) <= 0:
            self.screen.setText('Invalid input')
            return
        self.second_screen.setText(self.screen.toPlainText() + ' n_root ')
        self.screen.setText('0')

    def factorial(self):
        if not all([i not in self.second_screen.toPlainText() for i in self.OPERATIONS]):
            return
        self.optim()
        self.second_screen.setText(f'fact({self.screen.toPlainText()}) = ')
        try:
            self.screen.setText(str(math.factorial(int(self.screen.toPlainText()))))
            self.history.setText(self.history.toPlainText() + ('\n* ' if self.history.toPlainText() else '* ') + self.second_screen.toPlainText() + self.screen.toPlainText())
        except (ValueError, TypeError):
            self.screen.setText('Invalid input')
            self.second_screen.setText('')
        except OverflowError:
            self.screen.setText('Overflow')
            self.second_screen.setText('')

    def reverse(self):
        if not all([i not in self.second_screen.toPlainText() for i in self.OPERATIONS]):
            return
        self.optim()
        self.second_screen.setText(f'1/({self.screen.toPlainText()}) = ')
        try:
            self.screen.setText(str(1 / float(self.screen.toPlainText())))
            self.optim()
            self.history.setText(self.history.toPlainText() + ('\n* ' if self.history.toPlainText() else '* ') + self.second_screen.toPlainText() + self.screen.toPlainText())
        except (ValueError, ZeroDivisionError):
            self.screen.setText('Invalid input')
            self.second_screen.setText('')
        except OverflowError:
            self.screen.setText('Overflow')
            self.second_screen.setText('')

    def equal(self):
        if not self.second_screen.toPlainText() or self.second_screen.toPlainText().find('=') != -1:
            return
        self.optim()
        oper = self.second_screen.toPlainText()[self.second_screen.toPlainText().find(' ') + 1:self.second_screen.toPlainText().rfind(' ')]
        self.second_screen.setText(self.second_screen.toPlainText() + self.screen.toPlainText() + ' = ')
        try:
            if self.screen.toPlainText().find('.') == -1 and self.second_screen.toPlainText().find('.') == -1:
                self.screen.setText(str(self.DICT_OPERATIONS[oper](int(self.second_screen.toPlainText()[:self.second_screen.toPlainText().find(oper) - 1]), int(self.screen.toPlainText()))))
            else:
                self.screen.setText(str(self.DICT_OPERATIONS[oper](float(self.second_screen.toPlainText()[:self.second_screen.toPlainText().find(oper) - 1]), float(self.screen.toPlainText()))))
            self.optim()
            self.history.setText(self.history.toPlainText() + ('\n* ' if self.history.toPlainText() else '* ') + self.second_screen.toPlainText() + self.screen.toPlainText())
        except(ValueError, ZeroDivisionError, TypeError):
            self.screen.setText('Invalid input')
            self.second_screen.setText('')
        except OverflowError:
            self.screen.setText('Overflow')
            self.second_screen.setText('')

    def pop(self):
        if self.screen.toPlainText() == '0':
            return
        self.screen.setText('0' if (self.screen.toPlainText()[0] == '-' and len(self.screen.toPlainText()) == 2) or not self.screen.toPlainText()[:-1] else self.screen.toPlainText()[:-1])

    def erase(self):
        self.screen.setText('0')
        self.second_screen.setText('')

    def sign(self):
        if self.screen.toPlainText() == '0':
            return
        self.screen.setText(self.screen.toPlainText()[1:] if self.screen.toPlainText()[0] == '-' else '-' + self.screen.toPlainText())

    def dot(self):
        if self.screen.toPlainText().find('.') == -1:
            self.screen.setText(self.screen.toPlainText() + '.')


if __name__ == '__main__':
    app = w.QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
