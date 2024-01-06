from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QComboBox, QVBoxLayout, QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from languages import *
from googletrans import Translator



class Home(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setting()
        self.connects()
        
# What do you want to put and where?
        
    def connects(self):
        self.starttranslate.clicked.connect(self.translate_clicked)
        self.clearbutton.clicked.connect(self.clear)
        self.reversebutton.clicked.connect(self.reverse)

    def initUI(self):
        masterlayout = QHBoxLayout()
        leftlayout = QVBoxLayout()
        rightlayout = QVBoxLayout()
        self.title = QLabel("Translate 2.0")
        self.title.setObjectName("title") #setting the name for the object to edit it later
        self.combobox_1 = QComboBox()
        self.combobox_2 = QComboBox()
        self.combobox_1.addItems(values)
        self.combobox_2.addItems(values)
        self.starttranslate = QPushButton("Translate now")
        self.starttranslate.setObjectName("test")
        self.textedit_1 = QTextEdit()
        self.reversebutton = QPushButton("Reverse")
        self.textedit_2 = QTextEdit()
        self.clearbutton = QPushButton("Clear")
        self.textedit_1.setPlaceholdertext("Enter text")
        self.textedit21.setPlaceholdertext("Enter text")

        leftlayout.addWidget(self.title, alignment = Qt.AlignCenter)
        leftlayout.addWidget(self.combobox_1)
        leftlayout.addWidget(self.combobox_2)
        leftlayout.addWidget(self.starttranslate)
        leftlayout.addWidget(self.clearbutton)

        rightlayout.addWidget(self.textedit_1)
        rightlayout.addWidget(self.reversebutton)
        rightlayout.addWidget(self.textedit_2)

        masterlayout.addLayout(leftlayout, 40)
        masterlayout.addLayout(rightlayout, 60)
        
        self.setLayout(masterlayout)

        self.setStyleSheet("""
            QWidget{ 
                background-color: #076F94;
            }
            
            QPushButton{
                background-color: #E48080;
                border: 1px #333;
                border-radius: 5px;
            }
                           
            QPushButton:hover{
                    background-color: #5D3587;       
            }
                           
 """)

    def setting(self):
        self.setWindowTitle("Translater 2.0")
        self.resize(600,400)


    def translation(self, text, des_lang, src_lang):
        speaker = Translator()
        translate = speaker.translate(text, dest=src_lang, src=des_lang)
        return translate.text

    def translate_clicked(self):
        try:
            self.value_to_key1 = self.combobox_1.currentText()
            key_to_value1 = [k for k,v in LANGUAGES.items() if v == self.value_to_key1]

            self.value_to_key2 = self.combobox_2.currentText()
            key_to_value2 = [k for k,v in LANGUAGES.items() if v == self.value_to_key2]
            print(key_to_value1)
            print(key_to_value2)

            res = self.translation(self.textedit_1.toPlainText(),key_to_value1[0], key_to_value2[0])
            self.textedit_2.setText(res)
        except Exception as e:
            print(f"Error:{e}")
            self.textedit_1.setText("You must enter text.")


    def clear(self):
        self.textedit_1.clear()
        self.textedit_2.clear()

    def reverse(self):
        input_1 = self.textedit_1.toPlainText()
        output_1 = self.textedit_2.toPlainText()
        self.textedit_1.setText(output_1)
        self.textedit_2.setText(input_1)
        self.combobox_1.setCurrentText(self.value_to_key2)
        self.combobox_2.setCurrentText(self.value_to_key1)

if __name__ in "__main__":
    app = QApplication([])
    main = Home()
    main.show()
    app.exec_()