from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import re
import design  # Это наш конвертированный файл дизайна
import json
import ast

import settings


class ProdApp(QtWidgets.QWidget, design.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.add_pb.clicked.connect(self.addRule)
        self.delete_pb.clicked.connect(self.deleteRule)
        self.search_pb.clicked.connect(self.searchAnswer)
        self.save_pb.clicked.connect(self.save_to_db)
        self.load_pb.clicked.connect(self.load_from_db)

        self._rules = {}

        header = self.rules_tw.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

    def addRule(self):
        textIf = self.ruleIf_le.text()
        textThen = self.ruleThen_le.text()
        if(textIf not in self._rules):
            i = self.rules_tw.rowCount()
            self._rules[textIf] = textThen
            self.rules_tw.setRowCount(i+1)
            newIf = QtWidgets.QTableWidgetItem(textIf)
            self.rules_tw.setItem(i, 0, newIf)
            newThen = QtWidgets.QTableWidgetItem(textThen)
            self.rules_tw.setItem(i, 1, QtWidgets.QTableWidgetItem(newThen))

    def deleteRule(self):
        if(self.rules_tw.selectedItems()):
            rule_item = self.rules_tw.selectedItems()[0]
            row = self.rules_tw.row(rule_item)
            ifItem = self.rules_tw.itemAt(0, row)
            ifText = ifItem.text()
            del self._rules[ifText]
            self.rules_tw.removeRow(row)

    def searchAnswer(self):
        question = self.search_le.text()
        terms = self.sentense_to_terms(question)
        for rule_if, rule_then in self._rules.items():
            rule_terms = self.sentense_to_terms(rule_if)
            if(self.check_rule(terms, rule_terms)):
                self.showMsg("Рекомендуемое растение: "+rule_then, str(rule_if))
                return
        self.showMsg("Ответ на заданный вопрос отсутствует в базе знаний!", str(terms))
        

    def showMsg(self, info, details):
       msg = QtWidgets.QMessageBox()
       msg.setIcon(QtWidgets.QMessageBox.Information)

       msg.setText(info)
       msg.setWindowTitle("Экспертное заключение")
       msg.setDetailedText(details)
       msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
       msg.exec_()

    def check_rule(self, terms, rule_terms):
        for or_term in terms:
            for or_rule_term in rule_terms:
                if(len(or_rule_term)>len(or_term)):
                    break
                is_right = True
                for and_term in or_term:
                    if(and_term not in or_rule_term):
                        is_right = False
                        break
                if(is_right):
                    return True
        return False
                            

    def sentense_to_terms(self, sentense):
        sentense = sentense.lower()
        or_strings = self.split_or(sentense)
        or_terms = []
        for or_str in or_strings:
            and_terms = self.split_and(or_str)
            or_terms.append(and_terms)
        return or_terms


    def split_or(self,sentense):
        return re.split(r" или ", sentense)

    def split_and(self,sentense):
        str_list = re.split(r" и ", sentense)
        return self.list_to_dict(str_list)

    def list_to_dict(self, list):
        dict = set()
        for str in list:
            dict.add(str)
        return dict

    def load_from_db(self):
        """
        Загрузка правил из базы данных (файл формата JSON)
        """

        file_path = settings.DB_FILE_PATH

        with open(file_path, 'r') as infile:
            data = json.load(infile)
        self._rules = data
        self.rules_tw.setRowCount(len(data))
        i=0
        for rule_key, rule_value in data.items():
            self.rules_tw.setItem(i, 0, QtWidgets.QTableWidgetItem(rule_key))
            self.rules_tw.setItem(i, 1, QtWidgets.QTableWidgetItem(rule_value))
            i+=1
            
        print('Правила "{}" загружены из {}\n'.format(self._rules, file_path))

    def save_to_db(self):
        """
        Сохранение в базу данных (файл формата JSON)
        """
        data = self._rules
        file_path = settings.DB_FILE_PATH

        with open(file_path, 'w') as outfile:
            json.dump(data, outfile, indent=2)

        print('Правила "{}" сохранены в {}\n'.format(self._rules, file_path))
