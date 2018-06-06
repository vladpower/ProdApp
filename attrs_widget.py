# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_set_algs.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from attributes import *
import settings
import json
import ast
import nlp

class AttrsWidget(QtWidgets.QMainWindow,Ui_attrsForm):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.parent = parent
        self._attrs = set()
        self.addAttr_pb.clicked.connect(self.addAttr)
        self.delAttr_pb.clicked.connect(self.delAttr)
        self.saveAttrs_pb.clicked.connect(self.save_to_db)
        self.load_from_db()

    def addAttr(self):
        text = nlp.get_normal(self.attr_le.text())
        if(text not in self._attrs):
            self._attrs.add(text)
            self.attrs_lw.addItem(text)
        else:
            self.showErr()
            
    def showErr(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)

        msg.setText("Такой признак уже присутствует в списке")
        msg.setWindowTitle("Unsuccess")
        msg.exec_()

    def delAttr(self):
        row = self.attrs_lw.currentRow()
        if(self.attrs_lw.selectedItems()):
            item = self.attrs_lw.takeItem(row)
            self._attrs.remove(item.text())

    def load_from_db(self):
        """
        Загрузка правил из базы данных (файл формата JSON)
        """

        file_path = settings.DB_ATTRS_PATH

        with open(file_path, 'r') as infile:
            data = json.load(infile)
        self._attrs = set(data)
        for attr in self._attrs:
            self.attrs_lw.addItem(attr)
            
        print('Атрибуты "{}" загружены из {}\n'.format(self._attrs, file_path))

    def save_to_db(self):
        """
        Сохранение в базу данных (файл формата JSON)
        """
        data = list(self._attrs)
        file_path = settings.DB_ATTRS_PATH

        with open(file_path, 'w') as outfile:
            json.dump(data, outfile, indent=2, ensure_ascii=False)

        print('Атрибуты "{}" сохранены в {}\n'.format(self._attrs, file_path))
        self.parent.load_attrs_from_db()

        

