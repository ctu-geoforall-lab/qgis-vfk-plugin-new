from __future__ import absolute_import
from builtins import object
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_MainApp.ui'
#
# Created: Wed May 18 13:55:50 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from qgis.PyQt import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QSplitter, QSizePolicy, QGroupBox, QStackedWidget, QScrollArea, QHBoxLayout, QRadioButton, QSpacerItem, QPushButton, QProgressBar, QLabel, QLineEdit, QCheckBox, QVBoxLayout, QComboBox, QAction, QApplication

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


class Ui_MainApp(object):
    def setupUi(self, MainApp):
        MainApp.setObjectName(_fromUtf8("MainApp"))
        MainApp.resize(918, 332)
        MainApp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralWidget = QtWidgets.QWidget(MainApp)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.splitter = QtWidgets.QSplitter(self.centralWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.stackedWidget = QtWidgets.QStackedWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.importPage = QtWidgets.QWidget()
        self.importPage.setObjectName(_fromUtf8("importPage"))
        self.gridLayout_10 = QtWidgets.QGridLayout(self.importPage)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.scrollArea_5 = QtWidgets.QScrollArea(self.importPage)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName(_fromUtf8("scrollArea_5"))
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 409, 294))
        self.scrollAreaWidgetContents_5.setObjectName(_fromUtf8("scrollAreaWidgetContents_5"))
        self.gridLayout_11 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents_5)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_17 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_17.setMargin(0)
        self.gridLayout_17.setObjectName(_fromUtf8("gridLayout_17"))
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setContentsMargins(9, 7, -1, 0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.rb_file = QtWidgets.QRadioButton(self.groupBox)
        self.rb_file.setChecked(True)
        self.rb_file.setObjectName(_fromUtf8("rb_file"))
        self.horizontalLayout_6.addWidget(self.rb_file)
        self.rb_directory = QtWidgets.QRadioButton(self.groupBox)
        self.rb_directory.setObjectName(_fromUtf8("rb_directory"))
        self.horizontalLayout_6.addWidget(self.rb_directory)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.gridLayout_17.addWidget(self.groupBox, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_17.addItem(spacerItem1, 2, 0, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.pb_nextFile = QtWidgets.QPushButton(self.widget)
        self.pb_nextFile.setMinimumSize(QtCore.QSize(0, 0))
        self.pb_nextFile.setMaximumSize(QtCore.QSize(27, 27))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.pb_nextFile.setFont(font)
        self.pb_nextFile.setStyleSheet(_fromUtf8(""))
        self.pb_nextFile.setAutoRepeat(False)
        self.pb_nextFile.setAutoDefault(False)
        self.pb_nextFile.setDefault(False)
        self.pb_nextFile.setFlat(False)
        self.pb_nextFile.setObjectName(_fromUtf8("pb_nextFile"))
        self.gridLayout_12.addWidget(self.pb_nextFile, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_12.addWidget(self.label_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.vfkFileLineEdit = QtWidgets.QLineEdit(self.widget)
        self.vfkFileLineEdit.setObjectName(_fromUtf8("vfkFileLineEdit"))
        self.horizontalLayout_3.addWidget(self.vfkFileLineEdit)
        self.browseButton = QtWidgets.QPushButton(self.widget)
        self.browseButton.setObjectName(_fromUtf8("browseButton"))
        self.horizontalLayout_3.addWidget(self.browseButton)
        self.gridLayout_12.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.budCheckBox = QtWidgets.QCheckBox(self.widget)
        self.budCheckBox.setChecked(True)
        self.budCheckBox.setObjectName(_fromUtf8("budCheckBox"))
        self.gridLayout_12.addWidget(self.budCheckBox, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_12.addWidget(self.label, 0, 0, 1, 1)
        self.parCheckBox = QtWidgets.QCheckBox(self.widget)
        self.parCheckBox.setChecked(True)
        self.parCheckBox.setObjectName(_fromUtf8("parCheckBox"))
        self.gridLayout_12.addWidget(self.parCheckBox, 1, 1, 1, 1)
        self.l_settings = QtWidgets.QLabel(self.widget)
        self.l_settings.setMinimumSize(QtCore.QSize(69, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.l_settings.setFont(font)
        self.l_settings.setObjectName(_fromUtf8("l_settings"))
        self.gridLayout_12.addWidget(self.l_settings, 3, 0, 1, 1)
        self.overwriteCheckBox = QtWidgets.QCheckBox(self.widget)
        self.overwriteCheckBox.setChecked(False)
        self.overwriteCheckBox.setObjectName(_fromUtf8("overwriteCheckBox"))
        self.gridLayout_12.addWidget(self.overwriteCheckBox, 3, 1, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_12, 1, 0, 1, 1)
        self.labelLoading = QtWidgets.QLabel(self.widget)
        self.labelLoading.setText(_fromUtf8(""))
        self.labelLoading.setObjectName(_fromUtf8("labelLoading"))
        self.gridLayout_17.addWidget(self.labelLoading, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.loadVfkButton = QtWidgets.QPushButton(self.widget)
        self.loadVfkButton.setObjectName(_fromUtf8("loadVfkButton"))
        self.horizontalLayout_2.addWidget(self.loadVfkButton)
        self.gridLayout_17.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.gridLayout_11.addWidget(self.widget, 1, 0, 1, 1)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.gridLayout_10.addWidget(self.scrollArea_5, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.importPage)
        self.changesPage = QtWidgets.QWidget()
        self.changesPage.setObjectName(_fromUtf8("changesPage"))
        self.gridLayout_15 = QtWidgets.QGridLayout(self.changesPage)
        self.gridLayout_15.setObjectName(_fromUtf8("gridLayout_15"))
        self.scrollArea_6 = QtWidgets.QScrollArea(self.changesPage)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName(_fromUtf8("scrollArea_6"))
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 269, 194))
        self.scrollAreaWidgetContents_6.setObjectName(_fromUtf8("scrollAreaWidgetContents_6"))
        self.gridLayout_16 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_16.setObjectName(_fromUtf8("gridLayout_16"))
        self.widget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents_6)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.gridLayout_14 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_14.setMargin(0)
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_13.addWidget(self.label_4, 0, 0, 1, 1)
        self.le_mainDb = QtWidgets.QLineEdit(self.widget_3)
        self.le_mainDb.setObjectName(_fromUtf8("le_mainDb"))
        self.gridLayout_13.addWidget(self.le_mainDb, 0, 1, 1, 1)
        self.pb_mainDb = QtWidgets.QPushButton(self.widget_3)
        self.pb_mainDb.setObjectName(_fromUtf8("pb_mainDb"))
        self.gridLayout_13.addWidget(self.pb_mainDb, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_13.addWidget(self.label_5, 1, 0, 1, 1)
        self.le_amendmentDb = QtWidgets.QLineEdit(self.widget_3)
        self.le_amendmentDb.setObjectName(_fromUtf8("le_amendmentDb"))
        self.gridLayout_13.addWidget(self.le_amendmentDb, 1, 1, 1, 1)
        self.pb_amendmentDb = QtWidgets.QPushButton(self.widget_3)
        self.pb_amendmentDb.setObjectName(_fromUtf8("pb_amendmentDb"))
        self.gridLayout_13.addWidget(self.pb_amendmentDb, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_13.addWidget(self.label_6, 2, 0, 1, 1)
        self.le_exportDb = QtWidgets.QLineEdit(self.widget_3)
        self.le_exportDb.setObjectName(_fromUtf8("le_exportDb"))
        self.gridLayout_13.addWidget(self.le_exportDb, 2, 1, 1, 1)
        self.pb_exportDb = QtWidgets.QPushButton(self.widget_3)
        self.pb_exportDb.setObjectName(_fromUtf8("pb_exportDb"))
        self.gridLayout_13.addWidget(self.pb_exportDb, 2, 2, 1, 1)
        self.gridLayout_14.addLayout(self.gridLayout_13, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_14.addItem(spacerItem2, 1, 0, 1, 1)
        self.l_status = QtWidgets.QLabel(self.widget_3)
        self.l_status.setText(_fromUtf8(""))
        self.l_status.setObjectName(_fromUtf8("l_status"))
        self.gridLayout_14.addWidget(self.l_status, 2, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.progressBar_Changes = QtWidgets.QProgressBar(self.widget_3)
        self.progressBar_Changes.setProperty("value", 0)
        self.progressBar_Changes.setObjectName(_fromUtf8("progressBar_Changes"))
        self.horizontalLayout_5.addWidget(self.progressBar_Changes)
        self.pb_applyChanges = QtWidgets.QPushButton(self.widget_3)
        self.pb_applyChanges.setObjectName(_fromUtf8("pb_applyChanges"))
        self.horizontalLayout_5.addWidget(self.pb_applyChanges)
        self.gridLayout_14.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.gridLayout_16.addWidget(self.widget_3, 0, 0, 1, 1)
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)
        self.gridLayout_15.addWidget(self.scrollArea_6, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.changesPage)
        self.searchPage = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchPage.sizePolicy().hasHeightForWidth())
        self.searchPage.setSizePolicy(sizePolicy)
        self.searchPage.setObjectName(_fromUtf8("searchPage"))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.searchPage)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtWidgets.QLabel(self.searchPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.searchCombo = QtWidgets.QComboBox(self.searchPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchCombo.sizePolicy().hasHeightForWidth())
        self.searchCombo.setSizePolicy(sizePolicy)
        self.searchCombo.setObjectName(_fromUtf8("searchCombo"))
        self.horizontalLayout_4.addWidget(self.searchCombo)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.searchForms = QtWidgets.QStackedWidget(self.searchPage)
        self.searchForms.setObjectName(_fromUtf8("searchForms"))
        self.page = QtWidgets.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.gridLayout = QtWidgets.QGridLayout(self.page)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea = QtWidgets.QScrollArea(self.page)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 48, 28))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.vlastniciSearchForm = VlastniciSearchForm(self.scrollAreaWidgetContents)
        self.vlastniciSearchForm.setObjectName(_fromUtf8("vlastniciSearchForm"))
        self.gridLayout_5.addWidget(self.vlastniciSearchForm, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.searchForms.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.scrollArea_3 = QtWidgets.QScrollArea(self.page_2)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName(_fromUtf8("scrollArea_3"))
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 66, 28))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.parcelySearchForm = ParcelySearchForm(self.scrollAreaWidgetContents_2)
        self.parcelySearchForm.setObjectName(_fromUtf8("parcelySearchForm"))
        self.gridLayout_7.addWidget(self.parcelySearchForm, 0, 0, 1, 1)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_6.addWidget(self.scrollArea_3, 0, 0, 1, 1)
        self.searchForms.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.scrollArea_2 = QtWidgets.QScrollArea(self.page_3)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 66, 28))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.budovySearchForm = BudovySearchForm(self.scrollAreaWidgetContents_3)
        self.budovySearchForm.setObjectName(_fromUtf8("budovySearchForm"))
        self.gridLayout_3.addWidget(self.budovySearchForm, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_2.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.searchForms.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.scrollArea_4 = QtWidgets.QScrollArea(self.page_4)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName(_fromUtf8("scrollArea_4"))
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 66, 28))
        self.scrollAreaWidgetContents_4.setObjectName(_fromUtf8("scrollAreaWidgetContents_4"))
        self.gridLayout_9 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.jednotkySearchForm = JednotkySearchForm(self.scrollAreaWidgetContents_4)
        self.jednotkySearchForm.setObjectName(_fromUtf8("jednotkySearchForm"))
        self.gridLayout_9.addWidget(self.jednotkySearchForm, 0, 0, 1, 1)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_8.addWidget(self.scrollArea_4, 0, 0, 1, 1)
        self.searchForms.addWidget(self.page_4)
        self.verticalLayout_3.addWidget(self.searchForms)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.searchButton = QtWidgets.QPushButton(self.searchPage)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.horizontalLayout.addWidget(self.searchButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.stackedWidget.addWidget(self.searchPage)
        self.widget_2 = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.rightWidgetLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.rightWidgetLayout.setMargin(0)
        self.rightWidgetLayout.setObjectName(_fromUtf8("rightWidgetLayout"))
        self.vfkBrowser = VfkTextBrowser(self.widget_2)
        self.vfkBrowser.setObjectName(_fromUtf8("vfkBrowser"))
        self.rightWidgetLayout.addWidget(self.vfkBrowser)
        self.gridLayout_4.addWidget(self.splitter, 0, 1, 1, 1)
        MainApp.setWidget(self.centralWidget)
        self.actionVyhledavani = QtWidgets.QAction(MainApp)
        self.actionVyhledavani.setCheckable(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVyhledavani.setIcon(icon)
        self.actionVyhledavani.setObjectName(_fromUtf8("actionVyhledavani"))
        self.actionImport = QtWidgets.QAction(MainApp)
        self.actionImport.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/db-add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImport.setIcon(icon1)
        self.actionImport.setObjectName(_fromUtf8("actionImport"))
        self.actionBack = QtWidgets.QAction(MainApp)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/arrowBack.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBack.setIcon(icon2)
        self.actionBack.setObjectName(_fromUtf8("actionBack"))
        self.actionForward = QtWidgets.QAction(MainApp)
        self.actionForward.setEnabled(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/arrowForward.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionForward.setIcon(icon3)
        self.actionForward.setObjectName(_fromUtf8("actionForward"))
        self.actionExportLatex = QtWidgets.QAction(MainApp)
        self.actionExportLatex.setObjectName(_fromUtf8("actionExportLatex"))
        self.actionExportHtml = QtWidgets.QAction(MainApp)
        self.actionExportHtml.setObjectName(_fromUtf8("actionExportHtml"))
        self.actionSelectParInMap = QtWidgets.QAction(MainApp)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/selectPar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSelectParInMap.setIcon(icon4)
        self.actionSelectParInMap.setObjectName(_fromUtf8("actionSelectParInMap"))
        self.actionSelectBudInMap = QtWidgets.QAction(MainApp)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/selectBud.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSelectBudInMap.setIcon(icon5)
        self.actionSelectBudInMap.setObjectName(_fromUtf8("actionSelectBudInMap"))
        self.actionCuzkPage = QtWidgets.QAction(MainApp)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/cuzk.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCuzkPage.setIcon(icon6)
        self.actionCuzkPage.setObjectName(_fromUtf8("actionCuzkPage"))
        self.actionShowInfoaboutSelection = QtWidgets.QAction(MainApp)
        self.actionShowInfoaboutSelection.setCheckable(True)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/showInfo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShowInfoaboutSelection.setIcon(icon7)
        self.actionShowInfoaboutSelection.setObjectName(_fromUtf8("actionShowInfoaboutSelection"))
        self.actionShowHelpPage = QtWidgets.QAction(MainApp)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/vfkPlugin.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShowHelpPage.setIcon(icon8)
        self.actionShowHelpPage.setObjectName(_fromUtf8("actionShowHelpPage"))

        self.actionZpracujZmeny = QtWidgets.QAction(MainApp)
        self.actionZpracujZmeny.setCheckable(True)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/applyChanges.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZpracujZmeny.setIcon(icon9)
        self.actionZpracujZmeny.setObjectName(_fromUtf8("actionZpracujZmeny"))

        self.actionDownloadAllPosidents = QtWidgets.QAction(MainApp)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/downloadAllPosidents.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDownloadAllPosidents.setIcon(icon10)
        self.actionDownloadAllPosidents.setObjectName(_fromUtf8("actionDownloadAllPosidents"))

        self.retranslateUi(MainApp)
        self.stackedWidget.setCurrentIndex(0)
        self.searchForms.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainApp)

    def retranslateUi(self, MainApp):
        MainApp.setWindowTitle(_translate("MainApp", "Prohlížeč VFK", None))
        self.groupBox.setTitle(_translate("MainApp", "Vstupní zdroj:", None))
        self.rb_file.setToolTip(_translate("MainApp", "Načti soubor", None))
        self.rb_file.setText(_translate("MainApp", "Soubor", None))
        self.rb_directory.setToolTip(_translate("MainApp", "Načti VFK soubory z adresáře", None))
        self.rb_directory.setText(_translate("MainApp", "Adresář", None))
        self.pb_nextFile.setText(_translate("MainApp", "+", None))
        self.label_2.setText(_translate("MainApp", "Vrstvy:", None))
        self.browseButton.setText(_translate("MainApp", "Procházet", None))
        self.budCheckBox.setText(_translate("MainApp", "Budovy (BUD)", None))
        self.label.setText(_translate("MainApp", "VFK soubor:", None))
        self.parCheckBox.setText(_translate("MainApp", "Parcely (PAR)", None))
        self.l_settings.setText(_translate("MainApp", "Možnosti:", None))
        self.overwriteCheckBox.setToolTip(_translate("MainApp", "Přepiš stávající databázi SQLite", None))
        self.overwriteCheckBox.setText(_translate("MainApp", "Přepsat stávající databázi", None))
        self.loadVfkButton.setText(_translate("MainApp", "Načíst", None))
        self.label_4.setText(_translate("MainApp", "Hlavní databáze:", None))
        self.pb_mainDb.setText(_translate("MainApp", "Procházet", None))
        self.label_5.setText(_translate("MainApp", "Změnová databáze:", None))
        self.pb_amendmentDb.setText(_translate("MainApp", "Procházet", None))
        self.label_6.setText(_translate("MainApp", "Výstupní databáze:", None))
        self.pb_exportDb.setText(_translate("MainApp", "Procházet", None))
        self.pb_applyChanges.setText(_translate("MainApp", "Zpracovat změny", None))
        self.label_3.setText(_translate("MainApp", "Vyhledat:", None))
        self.searchButton.setText(_translate("MainApp", "Hledej", None))
        self.actionVyhledavani.setText(_translate("MainApp", "Vyhledávání", None))
        self.actionVyhledavani.setToolTip(_translate("MainApp", "Vyhledávání", None))
        self.actionVyhledavani.setShortcut(_translate("MainApp", "Ctrl+F", None))
        self.actionImport.setText(_translate("MainApp", "Import", None))
        self.actionImport.setToolTip(_translate("MainApp", "Import VFK", None))
        self.actionImport.setShortcut(_translate("MainApp", "Ctrl+I", None))
        self.actionBack.setText(_translate("MainApp", "back", None))
        self.actionBack.setToolTip(_translate("MainApp", "Zpět", None))
        self.actionBack.setShortcut(_translate("MainApp", "Ctrl+Z", None))
        self.actionForward.setText(_translate("MainApp", "forward", None))
        self.actionForward.setToolTip(_translate("MainApp", "Vpřed", None))
        self.actionForward.setShortcut(_translate("MainApp", "Ctrl+Shift+Z", None))
        self.actionExportLatex.setText(_translate("MainApp", "LaTeX", None))
        self.actionExportLatex.setToolTip(_translate("MainApp", "Export do LaTeXu", None))
        self.actionExportHtml.setText(_translate("MainApp", "HTML", None))
        self.actionExportHtml.setToolTip(_translate("MainApp", "Export do HTML", None))
        self.actionSelectParInMap.setText(_translate("MainApp", "selectParInMap", None))
        self.actionSelectParInMap.setToolTip(_translate("MainApp", "Označit aktuální parcely v mapě", None))
        self.actionSelectParInMap.setShortcut(_translate("MainApp", "Ctrl+P", None))
        self.actionSelectBudInMap.setText(_translate("MainApp", "selectBudInMap", None))
        self.actionSelectBudInMap.setToolTip(_translate("MainApp", "Označit aktuální budovy v mapě", None))
        self.actionSelectBudInMap.setShortcut(_translate("MainApp", "Ctrl+B", None))
        self.actionCuzkPage.setText(_translate("MainApp", "cuzkPage", None))
        self.actionCuzkPage.setToolTip(_translate("MainApp", "Otevřít v prohlížeči aplikaci Nahlížení do KN pro aktuální nemovitost", None))
        self.actionShowInfoaboutSelection.setText(_translate("MainApp", "showInfoaboutSelection", None))
        self.actionShowInfoaboutSelection.setToolTip(_translate("MainApp", "Aktivovat/deaktivovat zobrazení informací o vybraných nemovitostech", None))
        self.actionShowHelpPage.setText(_translate("MainApp", "showHelpPage", None))
        self.actionShowHelpPage.setToolTip(_translate("MainApp", "Zobrazit nápovědu", None))
        self.actionShowHelpPage.setShortcut(_translate("MainApp", "Ctrl+H", None))
        self.actionDownloadAllPosidents.setToolTip(_translate("MainApp", "Stáhnout označené posidenty z katastru", None))
        self.actionZpracujZmeny.setText(_translate("MainApp", "ZpracujZmeny", None))
        self.actionZpracujZmeny.setToolTip(_translate("MainApp", "Aplikuj změny na stavová data", None))
        self.actionZpracujZmeny.setShortcut(_translate("MainApp", "Ctrl+A", None))

from .vlastniciSearchForm import VlastniciSearchForm
from .vfkTextBrowser import VfkTextBrowser
from .jednotkySearchForm import JednotkySearchForm
from .budovySearchForm import BudovySearchForm
from .parcelySearchForm import ParcelySearchForm
from . import resources_rc
