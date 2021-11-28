from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QLineEdit, QSizePolicy


class NumberLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.__comma_enabled = False
        self.__initUi()

    def __initUi(self):
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.setValidator(QRegExpValidator(QRegExp('^([1-9][0-9]*\.?|0\.)[0-9]+$'), self))
        self.textEdited.connect(self.__textEdited)

    def __textEdited(self, text):
        if self.__comma_enabled:
            self.setCommaToText()

    def setComma(self, f: bool):
        self.__comma_enabled = f
        self.setCommaToText()

    def setCommaToText(self):
        text = self.text()
        if text:
            if self.__comma_enabled:
                if text.find('.') == -1:
                    text = text.replace(',', '')
                    self.setText('{:,}'.format(int(text)))
                else:
                    text = text.replace(',', '')
                    pre_dot, post_dot = text.split('.')
                    text = '{:,}'.format(int(pre_dot)) + '.' + post_dot
                    self.setText(text)
            else:
                self.setText(text.replace(',', ''))