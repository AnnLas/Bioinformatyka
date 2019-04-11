from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from venv.fastaRead.DotPlot import Dotplot
from venv.fastaRead.FastaParser import FastaParser
from venv.fastaRead.FastaReader import FastaReader


class Ui_MainWindow(object):
    """
            A class used to show GUI. User have three options to provide sequence: by hand, from file, from web.
            When one option is selected with combobox, other are disabled.

            On "Show charts" button two plots show, one is 'base', next is filtered with given parameters of window
            and treshold.


            """

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(847, 636)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 841, 481))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.open_file_button_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.open_file_button_1.setObjectName("open_file_button_1")
        self.verticalLayout.addWidget(self.open_file_button_1)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.sequence_1_txt = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.sequence_1_txt.setObjectName("sequence_1_txt")
        self.verticalLayout.addWidget(self.sequence_1_txt)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.id_1_txt = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.id_1_txt.setObjectName("id_1_txt")
        self.verticalLayout.addWidget(self.id_1_txt)
        self.search_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.search_1.setObjectName("search_1")
        self.verticalLayout.addWidget(self.search_1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_2)
        self.open_file_button_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.open_file_button_2.setObjectName("open_file_button_2")
        self.verticalLayout_3.addWidget(self.open_file_button_2)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.sequence_2_txt = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.sequence_2_txt.setObjectName("sequence_2_txt")
        self.verticalLayout_3.addWidget(self.sequence_2_txt)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.id_2_txt = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.id_2_txt.setObjectName("id_2_txt")
        self.verticalLayout_3.addWidget(self.id_2_txt)
        self.search_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.search_2.setObjectName("search_2")
        self.verticalLayout_3.addWidget(self.search_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(300, 520, 221, 71))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.show_charts_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.show_charts_button.setObjectName("show_charts_button")
        self.verticalLayout_4.addWidget(self.show_charts_button)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(120, 500, 141, 111))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.window_size_txt = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_4)
        self.window_size_txt.setDecimals(0)
        self.window_size_txt.setValue(7)
        self.window_size_txt.setObjectName("window_size_txt")
        self.verticalLayout_5.addWidget(self.window_size_txt)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.treshold_txt = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_4)
        self.treshold_txt.setDecimals(0)
        self.treshold_txt.setValue(3)
        self.treshold_txt.setObjectName("treshold_txt")
        self.verticalLayout_5.addWidget(self.treshold_txt)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "First sequence:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "User input"))
        self.comboBox.setItemText(1, _translate("MainWindow", "From file"))
        self.comboBox.setItemText(2, _translate("MainWindow", "From web"))
        self.open_file_button_1.setText(_translate("MainWindow", "Open file"))
        self.label_4.setText(_translate("MainWindow", "sequence:"))
        self.label_3.setText(_translate("MainWindow", "id:"))
        self.search_1.setText(_translate("MainWindow", "Search"))
        self.label_2.setText(_translate("MainWindow", "Second sequence:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "User input"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "From file"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "From web"))
        self.open_file_button_2.setText(_translate("MainWindow", "Open file"))
        self.label_6.setText(_translate("MainWindow", "sequence:"))
        self.label_5.setText(_translate("MainWindow", "id"))
        self.search_2.setText(_translate("MainWindow", "Search"))
        self.show_charts_button.setText(_translate("MainWindow", "Show charts"))
        self.label_7.setText(_translate("MainWindow", "Window size"))
        self.label_8.setText(_translate("MainWindow", "Treshold"))

        self.open_file_button_1.clicked.connect(self.open_file1)
        self.open_file_button_2.clicked.connect(self.open_file2)
        self.show_charts_button.clicked.connect(self.make_plot)
        self.search_1.clicked.connect(self.search_by_id1)
        self.search_2.clicked.connect(self.search_by_id2)
        self.combobox_changed()
        self.combobox_2_changed()
        self.comboBox.currentTextChanged.connect(self.combobox_changed)
        self.comboBox_2.currentTextChanged.connect(self.combobox_2_changed)

    def combobox_changed(self):
        self.open_file_button_1.setDisabled(True)
        self.sequence_1_txt.setReadOnly(True)
        self.id_1_txt.setReadOnly(True)
        self.search_1.setDisabled(True)
        if self.comboBox.currentText().__eq__("User input"):
            self.sequence_1_txt.setReadOnly(False)
            self.id_1_txt.setReadOnly(False)
        elif self.comboBox.currentText().__eq__("From file"):
            self.open_file_button_1.setDisabled(False)
        else:
            self.search_1.setDisabled(False)
            self.id_1_txt.setReadOnly(False)

    def combobox_2_changed(self):
        self.open_file_button_2.setDisabled(True)
        self.sequence_2_txt.setReadOnly(True)
        self.id_2_txt.setReadOnly(True)
        self.search_2.setDisabled(True)
        if self.comboBox_2.currentText().__eq__("User input"):
            self.sequence_2_txt.setReadOnly(False)
            self.id_2_txt.setReadOnly(False)
        elif self.comboBox_2.currentText().__eq__("From file"):
            self.open_file_button_2.setDisabled(False)
        else:
            self.search_2.setDisabled(False)
            self.id_2_txt.setReadOnly(False)

    def open_file1(self):
        self.get_file_dir(1)

    def open_file2(self):
        self.get_file_dir(2)

    def make_plot(self):
        if self.comboBox.currentText().__eq__("User input"):
            content = '>' + self.id_1_txt.text() + '\n'
            content = content + self.sequence_1_txt.toPlainText()
            fastaList = FastaParser.parse_fasta(content)
            self.fasta1 = fastaList.__getitem__(0)
        if self.comboBox_2.currentText().__eq__("User input"):
            content = '>' + self.id_2_txt.text() + '\n'
            content = content + self.sequence_2_txt.toPlainText()
            fastaList = FastaParser.parse_fasta(content)
            self.fasta2 = fastaList.__getitem__(0)

        Dotplot.show_plots(self.fasta1, self.fasta2, int(self.treshold_txt.text()), int(self.window_size_txt.text()))

    def search_by_id1(self):
        self.search_by_id(1)

    def search_by_id2(self):
        self.search_by_id(2)

    def search_by_id(self, number):
        if number == 1:
            id = self.id_1_txt.text()
            content = FastaReader.fasta_from_url(id)
            fastaList = FastaParser.parse_fasta(content)
            self.fasta1 = fastaList.__getitem__(0)
            self.id_1_txt.setText(self.fasta1.get_id())
            self.sequence_1_txt.setPlainText(self.fasta1.get_sequence())

        else:
            id = self.id_2_txt.text()
            content = FastaReader.fasta_from_url(id)
            fastaList = FastaParser.parse_fasta(content)
            self.fasta2 = fastaList.__getitem__(0)
            self.id_2_txt.setText(self.fasta2.get_id())
            self.sequence_2_txt.setPlainText(self.fasta2.get_sequence())

    def get_file_dir(self, seq_number):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None, "Choose Contact Icon", "", "Text Files (*.txt *.fasta)",
                                                  options=options)
        if fileName != '':
            content = FastaReader.fasta_from_file(fileName)
            fastaList = FastaParser.parse_fasta(content)
            fasta = fastaList.__getitem__(0)
            id = fasta.get_id()
            sequence = fasta.get_sequence()
            if seq_number == 1:
                self.fasta1 = fasta
                self.id_1_txt.setText(id)
                self.sequence_1_txt.setPlainText(sequence)
            else:
                self.fasta2 = fasta
                self.id_2_txt.setText(id)
                self.sequence_2_txt.setPlainText(sequence)
        else:
            print("wrong file directory choosen")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
