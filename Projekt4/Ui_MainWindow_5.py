# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zad5.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!


from FastaParser import FastaParser
from FastaReader import FastaReader
from MultipleSequenceMatch import MultipleSequenceMatch
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_MainWindow_5(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(888, 751)
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
        self.verticalLayout.addWidget(self.comboBox)
        self.open_file_button_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.open_file_button_1.setObjectName("open_file_button_1")
        self.verticalLayout.addWidget(self.open_file_button_1)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.sequence_1_txt = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.sequence_1_txt.setReadOnly(True)
        self.sequence_1_txt.setObjectName("sequence_1_txt")
        self.verticalLayout.addWidget(self.sequence_1_txt)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.id_1_txt = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.id_1_txt.setObjectName("id_1_txt")
        self.verticalLayout.addWidget(self.id_1_txt)
        self.search_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.search_button.setObjectName("search_button")
        self.verticalLayout.addWidget(self.search_button)
        self.add_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.add_button.setObjectName("add_button")
        self.verticalLayout.addWidget(self.add_button)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.sequence_2_txt = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.sequence_2_txt.setReadOnly(True)
        self.sequence_2_txt.setObjectName("sequence_2_txt")
        self.verticalLayout_3.addWidget(self.sequence_2_txt)
        self.clear_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.clear_button.setObjectName("clear_button")
        self.verticalLayout_3.addWidget(self.clear_button)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(310, 490, 221, 31))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.show_match_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.show_match_button.setObjectName("show_match_button")
        self.verticalLayout_4.addWidget(self.show_match_button)
        self.substitution_matrix = QtWidgets.QTableWidget(self.centralwidget)
        self.substitution_matrix.setGeometry(QtCore.QRect(10, 540, 411, 151))
        self.substitution_matrix.setObjectName("substitution_matrix")
        self.substitution_matrix.setColumnCount(4)
        self.substitution_matrix.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.substitution_matrix.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.substitution_matrix.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.substitution_matrix.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.substitution_matrix.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.substitution_matrix.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.substitution_matrix.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.substitution_matrix.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.substitution_matrix.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.substitution_matrix.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.substitution_matrix.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.substitution_matrix.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.substitution_matrix.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.substitution_matrix.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.substitution_matrix.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.substitution_matrix.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.substitution_matrix.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.substitution_matrix.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.substitution_matrix.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.substitution_matrix.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.substitution_matrix.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.substitution_matrix.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.substitution_matrix.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.substitution_matrix.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.substitution_matrix.setItem(3, 3, item)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 520, 161, 17))
        self.label_7.setObjectName("label_7")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(430, 530, 132, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_2.addWidget(self.label_13)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.gap_txt = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.gap_txt.setMinimum(-100)
        self.gap_txt.setMaximum(100)
        self.gap_txt.setProperty("value", 2)
        self.gap_txt.setObjectName("gap_txt")
        self.verticalLayout_2.addWidget(self.gap_txt)
        self.results_txt = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.results_txt.setGeometry(QtCore.QRect(600, 530, 241, 181))
        self.results_txt.setReadOnly(True)
        self.results_txt.setObjectName("results_txt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "From File"))
        self.comboBox.setItemText(1, _translate("MainWindow", "From Web"))
        self.open_file_button_1.setText(_translate("MainWindow", "Open file"))
        self.label_4.setText(_translate("MainWindow", "sequence:"))
        self.label_3.setText(_translate("MainWindow", "id:"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.label_6.setText(_translate("MainWindow", "Sequences:"))
        self.clear_button.setText(_translate("MainWindow", "Clear"))
        self.show_match_button.setText(_translate("MainWindow", "Show aligment"))
        item = self.substitution_matrix.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "A"))
        item = self.substitution_matrix.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "C"))
        item = self.substitution_matrix.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "G"))
        item = self.substitution_matrix.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "T"))
        item = self.substitution_matrix.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "A"))
        item = self.substitution_matrix.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "C"))
        item = self.substitution_matrix.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "G"))
        item = self.substitution_matrix.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "T"))
        __sortingEnabled = self.substitution_matrix.isSortingEnabled()
        self.substitution_matrix.setSortingEnabled(False)
        item = self.substitution_matrix.item(0, 0)
        item.setText(_translate("MainWindow", "0"))
        item = self.substitution_matrix.item(0, 1)
        item.setText(_translate("MainWindow", "1"))
        item = self.substitution_matrix.item(0, 2)
        item.setText(_translate("MainWindow", "1"))
        item = self.substitution_matrix.item(0, 3)
        item.setText(_translate("MainWindow", "1"))
        item = self.substitution_matrix.item(1, 0)
        item.setText(_translate("MainWindow", "1"))
        item = self.substitution_matrix.item(1, 1)
        item.setText(_translate("MainWindow", "0"))
        item = self.substitution_matrix.item(1, 2)
        item.setText(_translate("MainWindow", "1"))
        item = self.substitution_matrix.item(1, 3)
        item.setText(_translate("MainWindow", "1"))
        item = self.substitution_matrix.item(2, 0)
        item.setText(_translate("MainWindow", "1"))
        item = self.substitution_matrix.item(2, 1)
        item.setText(_translate("MainWindow", "1"))
        item = self.substitution_matrix.item(2, 2)
        item.setText(_translate("MainWindow", "0"))
        item = self.substitution_matrix.item(2, 3)
        item.setText(_translate("MainWindow", "1"))
        item = self.substitution_matrix.item(3, 0)
        item.setText(_translate("MainWindow", "1"))
        item = self.substitution_matrix.item(3, 1)
        item.setText(_translate("MainWindow", "1"))
        item = self.substitution_matrix.item(3, 2)
        item.setText(_translate("MainWindow", "1"))
        item = self.substitution_matrix.item(3, 3)
        item.setText(_translate("MainWindow", "0"))
        self.substitution_matrix.setSortingEnabled(__sortingEnabled)
        self.label_7.setText(_translate("MainWindow", "Substitution matrix"))
        self.label_13.setText(_translate("MainWindow", "Global match score"))
        self.label_8.setText(_translate("MainWindow", "Gap:"))

        self.open_file_button_1.clicked.connect(self.open_file1)
        self.show_match_button.clicked.connect(self.show_aligment)
        self.search_button.clicked.connect(self.search_by_id)
        self.add_button.clicked.connect(self.add_sequence)
        self.clear_button.clicked.connect(self.remove_sequences)

        self.combobox_changed()
        self.comboBox.currentTextChanged.connect(self.combobox_changed)

    def combobox_changed(self):

        self.sequence_1_txt.setReadOnly(True)
        self.id_1_txt.setReadOnly(True)

        if self.comboBox.currentText().__eq__("From file"):
            self.open_file_button_1.setDisabled(False)
        else:
            self.search_button.setDisabled(False)
            self.id_1_txt.setReadOnly(False)

    def open_file1(self):
        self.get_file_dir()

    def search_by_id(self):
        id = self.id_1_txt.text()
        content = FastaReader.fasta_from_url(id)
        fastaList = FastaParser.parse_fasta(content)
        text = ''
        for sequence in fastaList:
            text += sequence.get("id") + '\n'
            text += sequence.get("sequence") + '\n'

        self.sequence_1_txt.setPlainText(text)

    def add_sequence(self):
        text = self.sequence_1_txt.toPlainText() + self.sequence_2_txt.toPlainText()
        self.sequence_2_txt.setPlainText(text)

    def remove_sequences(self):
        self.sequence_2_txt.setPlainText("")

    def get_file_dir(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None, "", "", "Text Files (*.txt *.fasta)",
                                                  options=options)
        if fileName != '':
            content = FastaReader.fasta_from_file(fileName)
            fastaList = FastaParser.parse_fasta(content)
            text = ''
            for sequence in fastaList:
                text += sequence.get("id") + '\n'
                text += sequence.get("sequence") + '\n'

            self.sequence_1_txt.setPlainText(text)

        else:
            print("wrong file directory choosen")

    def sub_matrix_values(self):
        model = self.substitution_matrix.model()
        data = []
        i = 0
        data.append([])
        data[0].append('#')
        for j in range(model.columnCount()):
            data[0].append(self.substitution_matrix.verticalHeaderItem(j).text())
        for row in range(model.rowCount()):
            data.append([])
            i += 1
            data[i].append(data[0][i])
            for column in range(model.columnCount()):
                index = model.index(row, column)
                data[row + 1].append(int(model.data(index)))
        return data

    def show_aligment(self):

        multipleSeqMatch = MultipleSequenceMatch(int(self.gap_txt.text()), self.sub_matrix_values())
        fastas = self.sequence_2_txt.toPlainText()
        sequences = FastaParser.parse_fasta(fastas)
        matrix = multipleSeqMatch.match_multiple_arrays(sequences)

        starCentre = multipleSeqMatch.calculate_star_centre(matrix)
        multipleSeqMatch.centerSeq = starCentre.index(min(starCentre))

        aligment = multipleSeqMatch.aligment_to_center()
        multipleSeqMatch.calculate_total_score(aligment)
        multipleSeqMatch.print_result(aligment)
        multipleSeqMatch.print_fasta(aligment)
        self.results_txt.setPlainText(multipleSeqMatch.print_result(aligment))


        with open("ResultFasta.txt", "w") as tf:
            print(multipleSeqMatch.print_result(aligment), file=tf)

        with open("ResultFile.txt", "w") as text_file:
            print(multipleSeqMatch.print_fasta(aligment), file=text_file)

    def search_by_id1(self):
        self.search_by_id(1)

    def search_by_id2(self):
        self.search_by_id(2)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_5()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
