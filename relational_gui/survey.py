# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'relational_gui/survey.ui'
#
# Created: Sun Jun  7 13:34:01 2015
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(422, 313)
        Form.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QGridLayout()
        self.formLayout.setObjectName("formLayout")
        self.txtSystem = QtWidgets.QLineEdit(Form)
        self.txtSystem.setObjectName("txtSystem")
        self.formLayout.addWidget(self.txtSystem, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label.setObjectName("label")
        self.formLayout.addWidget(self.label, 1, 0, 1, 1)
        self.txtCountry = QtWidgets.QLineEdit(Form)
        self.txtCountry.setObjectName("txtCountry")
        self.formLayout.addWidget(self.txtCountry, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_2.setObjectName("label_2")
        self.formLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.txtSchool = QtWidgets.QLineEdit(Form)
        self.txtSchool.setObjectName("txtSchool")
        self.formLayout.addWidget(self.txtSchool, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_3.setObjectName("label_3")
        self.formLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.txtAge = QtWidgets.QLineEdit(Form)
        self.txtAge.setObjectName("txtAge")
        self.formLayout.addWidget(self.txtAge, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_4.setObjectName("label_4")
        self.formLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.txtFind = QtWidgets.QLineEdit(Form)
        self.txtFind.setObjectName("txtFind")
        self.formLayout.addWidget(self.txtFind, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_5.setObjectName("label_5")
        self.formLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.formLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.txtComments = QtWidgets.QTextEdit(Form)
        self.txtComments.setTabChangesFocus(True)
        self.txtComments.setObjectName("txtComments")
        self.formLayout.addWidget(self.txtComments, 6, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.formLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.txtEmail = QtWidgets.QLineEdit(Form)
        self.txtEmail.setObjectName("txtEmail")
        self.formLayout.addWidget(self.txtEmail, 5, 1, 1, 1)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cmdCancel = QtWidgets.QPushButton(Form)
        self.cmdCancel.setObjectName("cmdCancel")
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.cmdClear = QtWidgets.QPushButton(Form)
        self.cmdClear.setObjectName("cmdClear")
        self.horizontalLayout.addWidget(self.cmdClear)
        self.cmdSend = QtWidgets.QPushButton(Form)
        self.cmdSend.setDefault(True)
        self.cmdSend.setObjectName("cmdSend")
        self.horizontalLayout.addWidget(self.cmdSend)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label.setBuddy(self.txtCountry)
        self.label_2.setBuddy(self.txtSchool)
        self.label_3.setBuddy(self.txtAge)
        self.label_4.setBuddy(self.txtFind)
        self.label_5.setBuddy(self.txtSystem)
        self.label_6.setBuddy(self.txtComments)
        self.label_7.setBuddy(self.txtEmail)

        self.retranslateUi(Form)
        self.cmdCancel.clicked.connect(Form.close)
        self.cmdClear.clicked.connect(self.txtComments.clear)
        self.cmdClear.clicked.connect(self.txtFind.clear)
        self.cmdClear.clicked.connect(self.txtAge.clear)
        self.cmdClear.clicked.connect(self.txtSchool.clear)
        self.cmdClear.clicked.connect(self.txtCountry.clear)
        self.cmdClear.clicked.connect(self.txtSystem.clear)
        self.txtSystem.returnPressed.connect(self.txtCountry.setFocus)
        self.txtCountry.returnPressed.connect(self.txtSchool.setFocus)
        self.txtSchool.returnPressed.connect(self.txtAge.setFocus)
        self.txtAge.returnPressed.connect(self.txtFind.setFocus)
        self.cmdSend.clicked.connect(Form.send)
        self.cmdClear.clicked.connect(self.txtEmail.clear)
        self.txtFind.returnPressed.connect(self.txtEmail.setFocus)
        self.txtEmail.returnPressed.connect(self.txtComments.setFocus)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.txtSystem, self.txtCountry)
        Form.setTabOrder(self.txtCountry, self.txtSchool)
        Form.setTabOrder(self.txtSchool, self.txtAge)
        Form.setTabOrder(self.txtAge, self.txtFind)
        Form.setTabOrder(self.txtFind, self.txtEmail)
        Form.setTabOrder(self.txtEmail, self.txtComments)
        Form.setTabOrder(self.txtComments, self.cmdSend)
        Form.setTabOrder(self.cmdSend, self.cmdClear)
        Form.setTabOrder(self.cmdClear, self.cmdCancel)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Survey"))
        self.label.setText(_translate("Form", "Country"))
        self.label_2.setText(_translate("Form", "School"))
        self.label_3.setText(_translate("Form", "Age"))
        self.label_4.setText(_translate("Form", "How did you find relational"))
        self.label_5.setText(_translate("Form", "System"))
        self.label_6.setText(_translate("Form", "Comments"))
        self.label_7.setText(_translate("Form", "Email (only if you want a reply)"))
        self.cmdCancel.setText(_translate("Form", "Cancel"))
        self.cmdClear.setText(_translate("Form", "Clear"))
        self.cmdSend.setText(_translate("Form", "Send"))

