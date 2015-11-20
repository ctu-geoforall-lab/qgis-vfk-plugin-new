# -*- coding: utf-8 -*-

"""
/***************************************************************************
 vfkPluginDialog
                                 A QGIS plugin
 Plugin umoznujici praci s daty katastru nemovitosti
                             -------------------
        begin                : 2015-06-11
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Stepan Bambula
        email                : stepan.bambula@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import QFile, QIODevice, QUrl
from PyQt4.QtSql import QSqlDatabase


class Coordinates:
    x = 0.0
    y = 0.0

    def __init__(self):
        pass


class HistoryRecord:
    def __init__(self):
        self.html = ""
        self.parIds = []
        self.budIds = []
        self.definitionPoint = Coordinates()


class vfkTextBrowser(QTextBrowser):

    def __init__(self):
        self.mCurrentUrl = QUrl()
        self.mCurrentRecord = HistoryRecord()

    def exportDocument(self, task, fileName, format):
        fileOut = QFile(fileName)

        if fileOut.open(QIODevice.WriteOnly | QIODevice.Text) is False:
            return False

        taskMap = {}

    def parseTask(self, task):
        task = QUrl(task)
        taskList = []
        taskList.append(task.encodedQueryItems())

        taskMap = {}
        taskMap['action'] = task.path()

        for i in taskList:
            taskMap['']

    def goBack(self):
        pass

    def goForth(self):
        pass

    def currentUrl(self):
        return self.mCurrentUrl

    def currentDefinitionPoint(self):
        return self.mCurrentRecord.definitionPoint

    def setConnectionName(self, connectionName):
        pass
