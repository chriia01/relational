# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'relational_gui/maingui.ui'
#
# Created: Sat Oct 22 15:25:32 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 612)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.splitter_4 = QtGui.QSplitter(self.centralwidget)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.layoutWidget = QtGui.QWidget(self.splitter_4)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_11.setMargin(0)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.groupBox_3 = QtGui.QGroupBox(self.layoutWidget)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.cmdAbout = QtGui.QPushButton(self.groupBox_3)
        self.cmdAbout.setObjectName(_fromUtf8("cmdAbout"))
        self.verticalLayout_5.addWidget(self.cmdAbout)
        self.cmdSurvey = QtGui.QPushButton(self.groupBox_3)
        self.cmdSurvey.setObjectName(_fromUtf8("cmdSurvey"))
        self.verticalLayout_5.addWidget(self.cmdSurvey)
        self.verticalLayout_11.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(self.layoutWidget)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.cmdProduct = QtGui.QPushButton(self.groupBox_4)
        self.cmdProduct.setObjectName(_fromUtf8("cmdProduct"))
        self.verticalLayout_10.addWidget(self.cmdProduct)
        self.cmdDifference = QtGui.QPushButton(self.groupBox_4)
        self.cmdDifference.setObjectName(_fromUtf8("cmdDifference"))
        self.verticalLayout_10.addWidget(self.cmdDifference)
        self.cmdUnion = QtGui.QPushButton(self.groupBox_4)
        self.cmdUnion.setObjectName(_fromUtf8("cmdUnion"))
        self.verticalLayout_10.addWidget(self.cmdUnion)
        self.cmdIntersection = QtGui.QPushButton(self.groupBox_4)
        self.cmdIntersection.setObjectName(_fromUtf8("cmdIntersection"))
        self.verticalLayout_10.addWidget(self.cmdIntersection)
        self.cmdDivision = QtGui.QPushButton(self.groupBox_4)
        self.cmdDivision.setObjectName(_fromUtf8("cmdDivision"))
        self.verticalLayout_10.addWidget(self.cmdDivision)
        self.cmdJoin = QtGui.QPushButton(self.groupBox_4)
        self.cmdJoin.setObjectName(_fromUtf8("cmdJoin"))
        self.verticalLayout_10.addWidget(self.cmdJoin)
        self.cmdOuterLeft = QtGui.QPushButton(self.groupBox_4)
        self.cmdOuterLeft.setObjectName(_fromUtf8("cmdOuterLeft"))
        self.verticalLayout_10.addWidget(self.cmdOuterLeft)
        self.cmdOuterRight = QtGui.QPushButton(self.groupBox_4)
        self.cmdOuterRight.setObjectName(_fromUtf8("cmdOuterRight"))
        self.verticalLayout_10.addWidget(self.cmdOuterRight)
        self.cmdOuter = QtGui.QPushButton(self.groupBox_4)
        self.cmdOuter.setObjectName(_fromUtf8("cmdOuter"))
        self.verticalLayout_10.addWidget(self.cmdOuter)
        self.cmdProjection = QtGui.QPushButton(self.groupBox_4)
        self.cmdProjection.setObjectName(_fromUtf8("cmdProjection"))
        self.verticalLayout_10.addWidget(self.cmdProjection)
        self.cmdSelection = QtGui.QPushButton(self.groupBox_4)
        self.cmdSelection.setObjectName(_fromUtf8("cmdSelection"))
        self.verticalLayout_10.addWidget(self.cmdSelection)
        self.cmdRename = QtGui.QPushButton(self.groupBox_4)
        self.cmdRename.setObjectName(_fromUtf8("cmdRename"))
        self.verticalLayout_10.addWidget(self.cmdRename)
        self.cmdArrow = QtGui.QPushButton(self.groupBox_4)
        self.cmdArrow.setObjectName(_fromUtf8("cmdArrow"))
        self.verticalLayout_10.addWidget(self.cmdArrow)
        spacerItem = QtGui.QSpacerItem(20, 25, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem)
        self.verticalLayout_11.addWidget(self.groupBox_4)
        self.splitter_3 = QtGui.QSplitter(self.splitter_4)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.splitter_2 = QtGui.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.table = QtGui.QTreeWidget(self.splitter_2)
        self.table.setMinimumSize(QtCore.QSize(450, 400))
        self.table.setSizeIncrement(QtCore.QSize(0, 0))
        self.table.setRootIsDecorated(False)
        self.table.setObjectName(_fromUtf8("table"))
        self.table.headerItem().setText(0, _fromUtf8("Empty relation"))
        self.layoutWidget1 = QtGui.QWidget(self.splitter_2)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.lstHistory = QtGui.QListWidget(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lstHistory.sizePolicy().hasHeightForWidth())
        self.lstHistory.setSizePolicy(sizePolicy)
        self.lstHistory.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lstHistory.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.lstHistory.setFont(font)
        self.lstHistory.setObjectName(_fromUtf8("lstHistory"))
        self.verticalLayout_6.addWidget(self.lstHistory)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.cmdOptimize = QtGui.QPushButton(self.layoutWidget1)
        self.cmdOptimize.setObjectName(_fromUtf8("cmdOptimize"))
        self.horizontalLayout_3.addWidget(self.cmdOptimize)
        self.cmdUndoOptimize = QtGui.QPushButton(self.layoutWidget1)
        self.cmdUndoOptimize.setObjectName(_fromUtf8("cmdUndoOptimize"))
        self.horizontalLayout_3.addWidget(self.cmdUndoOptimize)
        self.cmdClearHistory = QtGui.QPushButton(self.layoutWidget1)
        self.cmdClearHistory.setObjectName(_fromUtf8("cmdClearHistory"))
        self.horizontalLayout_3.addWidget(self.cmdClearHistory)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.splitter = QtGui.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.groupBox = QtGui.QGroupBox(self.splitter)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lstRelations = QtGui.QListWidget(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lstRelations.sizePolicy().hasHeightForWidth())
        self.lstRelations.setSizePolicy(sizePolicy)
        self.lstRelations.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lstRelations.setObjectName(_fromUtf8("lstRelations"))
        self.verticalLayout.addWidget(self.lstRelations)
        self.cmdNew = QtGui.QPushButton(self.groupBox)
        self.cmdNew.setObjectName(_fromUtf8("cmdNew"))
        self.verticalLayout.addWidget(self.cmdNew)
        self.cmdLoad = QtGui.QPushButton(self.groupBox)
        self.cmdLoad.setObjectName(_fromUtf8("cmdLoad"))
        self.verticalLayout.addWidget(self.cmdLoad)
        self.cmdSave = QtGui.QPushButton(self.groupBox)
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.verticalLayout.addWidget(self.cmdSave)
        self.cmdEdit = QtGui.QPushButton(self.groupBox)
        self.cmdEdit.setObjectName(_fromUtf8("cmdEdit"))
        self.verticalLayout.addWidget(self.cmdEdit)
        self.cmdUnload = QtGui.QPushButton(self.groupBox)
        self.cmdUnload.setObjectName(_fromUtf8("cmdUnload"))
        self.verticalLayout.addWidget(self.cmdUnload)
        self.groupBox_2 = QtGui.QGroupBox(self.splitter)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.lstAttributes = QtGui.QListWidget(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lstAttributes.sizePolicy().hasHeightForWidth())
        self.lstAttributes.setSizePolicy(sizePolicy)
        self.lstAttributes.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lstAttributes.setObjectName(_fromUtf8("lstAttributes"))
        self.verticalLayout_3.addWidget(self.lstAttributes)
        self.verticalLayout_7.addWidget(self.splitter_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.txtResult = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtResult.sizePolicy().hasHeightForWidth())
        self.txtResult.setSizePolicy(sizePolicy)
        self.txtResult.setObjectName(_fromUtf8("txtResult"))
        self.horizontalLayout_2.addWidget(self.txtResult)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.txtQuery = QtGui.QLineEdit(self.centralwidget)
        self.txtQuery.setObjectName(_fromUtf8("txtQuery"))
        self.horizontalLayout_2.addWidget(self.txtQuery)
        self.cmdClearQuery = QtGui.QPushButton(self.centralwidget)
        self.cmdClearQuery.setObjectName(_fromUtf8("cmdClearQuery"))
        self.horizontalLayout_2.addWidget(self.cmdClearQuery)
        self.cmdExecute = QtGui.QPushButton(self.centralwidget)
        self.cmdExecute.setObjectName(_fromUtf8("cmdExecute"))
        self.horizontalLayout_2.addWidget(self.cmdExecute)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName(_fromUtf8("action"))
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setMenuRole(QtGui.QAction.AboutRole)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.action_Load_relation = QtGui.QAction(MainWindow)
        self.action_Load_relation.setObjectName(_fromUtf8("action_Load_relation"))
        self.action_Save_relation = QtGui.QAction(MainWindow)
        self.action_Save_relation.setObjectName(_fromUtf8("action_Save_relation"))
        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setMenuRole(QtGui.QAction.QuitRole)
        self.action_Quit.setObjectName(_fromUtf8("action_Quit"))
        self.actionCheck_for_new_versions = QtGui.QAction(MainWindow)
        self.actionCheck_for_new_versions.setObjectName(_fromUtf8("actionCheck_for_new_versions"))
        self.actionNew_relation = QtGui.QAction(MainWindow)
        self.actionNew_relation.setObjectName(_fromUtf8("actionNew_relation"))
        self.actionEdit_relation = QtGui.QAction(MainWindow)
        self.actionEdit_relation.setObjectName(_fromUtf8("actionEdit_relation"))
        self.menuFile.addAction(self.actionNew_relation)
        self.menuFile.addAction(self.action_Load_relation)
        self.menuFile.addAction(self.action_Save_relation)
        self.menuFile.addAction(self.actionEdit_relation)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_Quit)
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addAction(self.actionCheck_for_new_versions)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.label.setBuddy(self.txtQuery)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.cmdClearQuery, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtQuery.clear)
        QtCore.QObject.connect(self.cmdClearHistory, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lstHistory.clear)
        QtCore.QObject.connect(self.txtQuery, QtCore.SIGNAL(_fromUtf8("returnPressed()")), MainWindow.execute)
        QtCore.QObject.connect(self.cmdExecute, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.execute)
        QtCore.QObject.connect(self.cmdAbout, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.showAbout)
        QtCore.QObject.connect(self.cmdSurvey, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.showSurvey)
        QtCore.QObject.connect(self.cmdProduct, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.addProduct)
        QtCore.QObject.connect(self.cmdDifference, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.addDifference)
        QtCore.QObject.connect(self.cmdArrow, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.addArrow)
        QtCore.QObject.connect(self.cmdRename, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.addRename)
        QtCore.QObject.connect(self.cmdSelection, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.addSelection)
        QtCore.QObject.connect(self.cmdProjection, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.addProjection)
        QtCore.QObject.connect(self.cmdUnload, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.unloadRelation)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.saveRelation)
        QtCore.QObject.connect(self.cmdLoad, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.loadRelation)
        QtCore.QObject.connect(self.cmdOptimize, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.optimize)
        QtCore.QObject.connect(self.cmdUndoOptimize, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.undoOptimize)
        QtCore.QObject.connect(self.txtResult, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.txtQuery.setFocus)
        QtCore.QObject.connect(self.cmdOuterRight, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.addORight)
        QtCore.QObject.connect(self.cmdOuter, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.addOuter)
        QtCore.QObject.connect(self.cmdOuterLeft, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.addOLeft)
        QtCore.QObject.connect(self.cmdJoin, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.addJoin)
        QtCore.QObject.connect(self.cmdDivision, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.addDivision)
        QtCore.QObject.connect(self.cmdIntersection, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.addIntersection)
        QtCore.QObject.connect(self.cmdUnion, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.addUnion)
        QtCore.QObject.connect(self.lstRelations, QtCore.SIGNAL(_fromUtf8("itemDoubleClicked(QListWidgetItem*)")), MainWindow.printRelation)
        QtCore.QObject.connect(self.lstRelations, QtCore.SIGNAL(_fromUtf8("itemClicked(QListWidgetItem*)")), MainWindow.showAttributes)
        QtCore.QObject.connect(self.cmdClearQuery, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtQuery.setFocus)
        QtCore.QObject.connect(self.lstHistory, QtCore.SIGNAL(_fromUtf8("itemDoubleClicked(QListWidgetItem*)")), MainWindow.resumeHistory)
        QtCore.QObject.connect(self.actionAbout, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.showAbout)
        QtCore.QObject.connect(self.action_Load_relation, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.loadRelation)
        QtCore.QObject.connect(self.action_Save_relation, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.saveRelation)
        QtCore.QObject.connect(self.action_Quit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.actionCheck_for_new_versions, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.checkVersion)
        QtCore.QObject.connect(self.cmdEdit, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.editRelation)
        QtCore.QObject.connect(self.actionEdit_relation, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.editRelation)
        QtCore.QObject.connect(self.cmdNew, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.newRelation)
        QtCore.QObject.connect(self.actionNew_relation, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.newRelation)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.cmdAbout, self.cmdSurvey)
        MainWindow.setTabOrder(self.cmdSurvey, self.cmdProduct)
        MainWindow.setTabOrder(self.cmdProduct, self.cmdDifference)
        MainWindow.setTabOrder(self.cmdDifference, self.cmdUnion)
        MainWindow.setTabOrder(self.cmdUnion, self.cmdIntersection)
        MainWindow.setTabOrder(self.cmdIntersection, self.cmdDivision)
        MainWindow.setTabOrder(self.cmdDivision, self.cmdJoin)
        MainWindow.setTabOrder(self.cmdJoin, self.cmdOuterLeft)
        MainWindow.setTabOrder(self.cmdOuterLeft, self.cmdOuterRight)
        MainWindow.setTabOrder(self.cmdOuterRight, self.cmdOuter)
        MainWindow.setTabOrder(self.cmdOuter, self.cmdProjection)
        MainWindow.setTabOrder(self.cmdProjection, self.cmdSelection)
        MainWindow.setTabOrder(self.cmdSelection, self.cmdRename)
        MainWindow.setTabOrder(self.cmdRename, self.cmdArrow)
        MainWindow.setTabOrder(self.cmdArrow, self.table)
        MainWindow.setTabOrder(self.table, self.lstHistory)
        MainWindow.setTabOrder(self.lstHistory, self.cmdOptimize)
        MainWindow.setTabOrder(self.cmdOptimize, self.cmdUndoOptimize)
        MainWindow.setTabOrder(self.cmdUndoOptimize, self.cmdClearHistory)
        MainWindow.setTabOrder(self.cmdClearHistory, self.lstRelations)
        MainWindow.setTabOrder(self.lstRelations, self.cmdLoad)
        MainWindow.setTabOrder(self.cmdLoad, self.cmdSave)
        MainWindow.setTabOrder(self.cmdSave, self.cmdUnload)
        MainWindow.setTabOrder(self.cmdUnload, self.lstAttributes)
        MainWindow.setTabOrder(self.lstAttributes, self.txtResult)
        MainWindow.setTabOrder(self.txtResult, self.txtQuery)
        MainWindow.setTabOrder(self.txtQuery, self.cmdClearQuery)
        MainWindow.setTabOrder(self.cmdClearQuery, self.cmdExecute)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Relational", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSurvey.setText(QtGui.QApplication.translate("MainWindow", "Survey", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "Operators", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdProduct.setText(QtGui.QApplication.translate("MainWindow", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDifference.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdUnion.setText(QtGui.QApplication.translate("MainWindow", "ᑌ", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdIntersection.setText(QtGui.QApplication.translate("MainWindow", "ᑎ", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDivision.setText(QtGui.QApplication.translate("MainWindow", "÷", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdJoin.setText(QtGui.QApplication.translate("MainWindow", "ᐅᐊ", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdOuterLeft.setText(QtGui.QApplication.translate("MainWindow", "ᐅLEFTᐊ", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdOuterRight.setText(QtGui.QApplication.translate("MainWindow", "ᐅRIGHTᐊ", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdOuter.setText(QtGui.QApplication.translate("MainWindow", "ᐅFULLᐊ", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdProjection.setText(QtGui.QApplication.translate("MainWindow", "π", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSelection.setText(QtGui.QApplication.translate("MainWindow", "σ", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdRename.setText(QtGui.QApplication.translate("MainWindow", "ρ", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdArrow.setText(QtGui.QApplication.translate("MainWindow", "➡", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdOptimize.setText(QtGui.QApplication.translate("MainWindow", "Optimize", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdUndoOptimize.setText(QtGui.QApplication.translate("MainWindow", "Undo optimize", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdClearHistory.setText(QtGui.QApplication.translate("MainWindow", "Clear history", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Relations", None, QtGui.QApplication.UnicodeUTF8))
        self.lstRelations.setSortingEnabled(True)
        self.cmdNew.setText(QtGui.QApplication.translate("MainWindow", "New relation", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdLoad.setText(QtGui.QApplication.translate("MainWindow", "Load relation", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("MainWindow", "Save relation", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdEdit.setText(QtGui.QApplication.translate("MainWindow", "Edit relation", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdUnload.setText(QtGui.QApplication.translate("MainWindow", "Unload relation", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Attributes", None, QtGui.QApplication.UnicodeUTF8))
        self.txtResult.setText(QtGui.QApplication.translate("MainWindow", "_last1", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdClearQuery.setText(QtGui.QApplication.translate("MainWindow", "⌫", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdExecute.setText(QtGui.QApplication.translate("MainWindow", "Execute", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Load_relation.setText(QtGui.QApplication.translate("MainWindow", "&Load relation", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Load_relation.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save_relation.setText(QtGui.QApplication.translate("MainWindow", "&Save relation", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save_relation.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCheck_for_new_versions.setText(QtGui.QApplication.translate("MainWindow", "Check for new versions", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_relation.setText(QtGui.QApplication.translate("MainWindow", "New relation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_relation.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_relation.setText(QtGui.QApplication.translate("MainWindow", "Edit relation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_relation.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))

