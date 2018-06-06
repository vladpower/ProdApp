# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'attributes.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_attrsForm(object):
    def setupUi(self, attrsForm):
        attrsForm.setObjectName("attrsForm")
        attrsForm.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(attrsForm.sizePolicy().hasHeightForWidth())
        attrsForm.setSizePolicy(sizePolicy)
        attrsForm.setMinimumSize(QtCore.QSize(400, 300))
        attrsForm.setMaximumSize(QtCore.QSize(400, 300))
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(attrsForm)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(9, 9, 381, 251))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.attrs_lw = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attrs_lw.sizePolicy().hasHeightForWidth())
        self.attrs_lw.setSizePolicy(sizePolicy)
        self.attrs_lw.setObjectName("attrs_lw")
        self.verticalLayout_2.addWidget(self.attrs_lw)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.attr_le = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.attr_le.setObjectName("attr_le")
        self.horizontalLayout_6.addWidget(self.attr_le)
        self.addAttr_pb = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.addAttr_pb.setObjectName("addAttr_pb")
        self.horizontalLayout_6.addWidget(self.addAttr_pb)
        self.delAttr_pb = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.delAttr_pb.setObjectName("delAttr_pb")
        self.horizontalLayout_6.addWidget(self.delAttr_pb)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.saveAttrs_pb = QtWidgets.QPushButton(attrsForm)
        self.saveAttrs_pb.setGeometry(QtCore.QRect(9, 266, 381, 25))
        self.saveAttrs_pb.setObjectName("saveAttrs_pb")

        self.retranslateUi(attrsForm)
        QtCore.QMetaObject.connectSlotsByName(attrsForm)

    def retranslateUi(self, attrsForm):
        _translate = QtCore.QCoreApplication.translate
        attrsForm.setWindowTitle(_translate("attrsForm", "ProdApp"))
        self.label.setText(_translate("attrsForm", "Список признаков"))
        self.addAttr_pb.setText(_translate("attrsForm", "Добавить"))
        self.delAttr_pb.setText(_translate("attrsForm", "Удалить"))
        self.saveAttrs_pb.setText(_translate("attrsForm", "Сохранить"))

