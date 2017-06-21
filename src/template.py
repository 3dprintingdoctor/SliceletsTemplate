#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Slicer Slicelets template.

This Slicelets can add/save data, search modules and load it dynamically, show 2d and 3d viewers.

Usage: slicer --no-main-window --python-script path/to/template.py
    
Author: YingLi Lu, yinglilu@gmail.com

Date: 2017-06-21

Note: tested with slicer 4.6.2

"""

#True: show 'Save Data' button
saveData=True

#True: show 'Modules Search'. Selected module will be added to modules tab dynamically.
addModule=True

#Modify/add modules you need
defaultModules=["data"]

#slicer 2D/3D layout: pick up a number
slicerLayout = 2
# SlicerLayoutInitialView = 0
# SlicerLayoutDefaultView = 1
# SlicerLayoutConventionalView = 2
# SlicerLayoutFourUpView = 3

# SlicerLayoutOneUp3DView = 4
# SlicerLayoutOneUpSliceView = 5
# SlicerLayoutOneUpRedSliceView = 6
# SlicerLayoutOneUpYellowSliceView = 7

# SlicerLayoutOneUpGreenSliceView = 8
# SlicerLayoutTabbed3DView = 9
# SlicerLayoutTabbedSliceView = 10
# SlicerLayoutLightboxView = 11

# SlicerLayoutCompareView = 12
# SlicerLayoutSideBySideLightboxView = 13
# SlicerLayoutNone = 14
# SlicerLayoutDual3DView = 15

# SlicerLayoutConventionalWidescreenView = 16
# SlicerLayoutCompareWidescreenView = 17
# SlicerLayoutSingleLightboxView = 18
# SlicerLayoutTriple3DEndoscopyView = 19

# SlicerLayout3DPlusLightboxView = 20
# SlicerLayoutThreeOverThreeView = 21
# SlicerLayoutFourOverFourView = 22
# SlicerLayoutCompareGridView = 23

# SlicerLayoutConventionalQuantitativeView = 24
# SlicerLayoutFourUpQuantitativeView = 25
# SlicerLayoutOneUpQuantitativeView = 26
# SlicerLayoutTwoOverTwoView = 27

# SlicerLayoutThreeOverThreeQuantitativeView = 28
# SlicerLayoutSideBySideView = 29
# SlicerLayoutFourByThreeSliceView = 30
# SlicerLayoutFourByTwoSliceView = 31

# SlicerLayoutFiveByTwoSliceView = 32
# SlicerLayoutThreeByThreeSliceView = 33
# SlicerLayoutFourUpTableView = 34
# SlicerLayout3DTableView = 35

# SlicerLayoutFinalView
# SlicerLayoutMaximizedView = 98
# SlicerLayoutCustomView = 99
# SlicerLayoutUserView = 100 

import qt
import __main__

def onModuleSelected(modulename):
  global tabWidget
  tabWidget.addTab(getattr(slicer.modules, modulename.lower()).widgetRepresentation(), modulename)

#splitter
splitter = qt.QSplitter()

leftWidget = qt.QWidget()
rightWidget = qt.QWidget()

splitter.addWidget(leftWidget)
splitter.addWidget(rightWidget)

#left layout for [add data,save data,search modules] and modules(tab)
leftLayout = qt.QVBoxLayout()
leftWidget.setLayout(leftLayout)

#right layout for 2d/3d viewer
rightLayout = qt.QVBoxLayout()
rightWidget.setLayout(rightLayout)

#top left layout: add data, save data,search modules
topleftLayout = qt.QHBoxLayout()
leftLayout.addLayout(topleftLayout)

#add data button
addDataButton = qt.QPushButton("Add Data")
topleftLayout.addWidget(addDataButton)
addDataButton.connect('clicked()', slicer.util.openAddDataDialog)

#save data button
if saveData:
  saveDataButton = qt.QPushButton("Save Data")
  topleftLayout.addWidget(saveDataButton)
  saveDataButton.connect('clicked()', slicer.util.openSaveDataDialog)

#dynamic add modules
if addModule:
  moduleSelector = slicer.qSlicerModuleSelectorToolBar()
  moduleSelector.setModuleManager(slicer.app.moduleManager())
  topleftLayout.addWidget(moduleSelector)
  moduleSelector.connect('moduleSelected(QString)', onModuleSelected)

tabWidget = qt.QTabWidget()
leftLayout.addWidget(tabWidget)

for module in defaultModules:
  onModuleSelected(module)

#add 2D/3D viewer to right layout
layoutManager = slicer.qMRMLLayoutWidget()
layoutManager.setMRMLScene(slicer.mrmlScene)
layoutManager.setLayout(slicerLayout)

rightLayout.addWidget(layoutManager)

splitter.show()

__main__.splitter = splitter # Keep track of the widget to avoid its premature destruction