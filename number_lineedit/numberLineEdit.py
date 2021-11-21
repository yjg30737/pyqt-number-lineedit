from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QLineEdit, QSizePolicy


class NumberLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.__comma_flag = True
        self.__initUi()

    def __initUi(self):
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.setValidator(QRegExpValidator(QRegExp('^([1-9][0-9]+\.?|0\.)[0-9]+$'), self))

    def textChanged(self, a0: str) -> None:
        if self.__comma_flag:
            self.__setCommaToLineEditNumber(self.__comma_flag)
        return super().textChanged(a0)

    def setComma(self, f: bool):
        self.__comma_flag = f

    def __setCommaToLineEditNumber(self, f: bool):
        text = self.text()
        if text:
            if f:
                if text.find('.') == -1:
                    self.setText('{:,}'.format(int(text)))
                else:
                    pre_dot, post_dot = text.split('.')
                    text = '{:,}'.format(int(pre_dot)) + '.' + post_dot
                    self.setText(text)
            else:
                self.setText(text.replace(',', ''))