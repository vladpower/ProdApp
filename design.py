# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(616, 490)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rules_tw = QtWidgets.QTableWidget(Form)
        self.rules_tw.setLineWidth(1)
        self.rules_tw.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.rules_tw.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.rules_tw.setObjectName("rules_tw")
        self.rules_tw.setColumnCount(2)
        self.rules_tw.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.rules_tw.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.rules_tw.setHorizontalHeaderItem(1, item)
        self.rules_tw.horizontalHeader().setVisible(True)
        self.rules_tw.horizontalHeader().setCascadingSectionResizes(False)
        self.rules_tw.horizontalHeader().setDefaultSectionSize(147)
        self.rules_tw.horizontalHeader().setMinimumSectionSize(93)
        self.rules_tw.verticalHeader().setVisible(False)
        self.rules_tw.verticalHeader().setHighlightSections(False)
        self.verticalLayout.addWidget(self.rules_tw)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ruleIf_le = QtWidgets.QLineEdit(Form)
        self.ruleIf_le.setObjectName("ruleIf_le")
        self.horizontalLayout.addWidget(self.ruleIf_le)
        self.ruleThen_le = QtWidgets.QLineEdit(Form)
        self.ruleThen_le.setObjectName("ruleThen_le")
        self.horizontalLayout.addWidget(self.ruleThen_le)
        self.add_pb = QtWidgets.QPushButton(Form)
        self.add_pb.setObjectName("add_pb")
        self.horizontalLayout.addWidget(self.add_pb)
        self.delete_pb = QtWidgets.QPushButton(Form)
        self.delete_pb.setObjectName("delete_pb")
        self.horizontalLayout.addWidget(self.delete_pb)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.search_le = QtWidgets.QLineEdit(Form)
        self.search_le.setText("")
        self.search_le.setObjectName("search_le")
        self.horizontalLayout_2.addWidget(self.search_le)
        self.search_pb = QtWidgets.QPushButton(Form)
        self.search_pb.setObjectName("search_pb")
        self.horizontalLayout_2.addWidget(self.search_pb)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.load_pb = QtWidgets.QPushButton(Form)
        self.load_pb.setObjectName("load_pb")
        self.horizontalLayout_3.addWidget(self.load_pb)
        self.save_pb = QtWidgets.QPushButton(Form)
        self.save_pb.setObjectName("save_pb")
        self.horizontalLayout_3.addWidget(self.save_pb)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ProdApp"))
        item = self.rules_tw.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Если"))
        item = self.rules_tw.horizontalHeaderItem(1)
        item.setText(_translate("Form", "То"))
        self.add_pb.setText(_translate("Form", "Добавить"))
        self.delete_pb.setText(_translate("Form", "Удалить"))
        self.search_pb.setText(_translate("Form", "Поиск"))
        self.load_pb.setText(_translate("Form", "Загрузить"))
        self.save_pb.setText(_translate("Form", "Сохранить"))

