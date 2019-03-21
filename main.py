from pywinauto import application
from pywinauto import keyboard
import os
searchpath = r'C:\Users\User\Downloads\Note8\images'
app = application.Application()
path = r'C:\Program Files (x86)\Qualcomm\QPST\bin\QFIL.exe'
app.start(path)
qfill = app[u'WindowsForms10.Window.8.app.0.190610d_r9_ad1']
qfill.wait('ready')

FlatBuildButton = qfill.Button3
FlatBuildButton.click()

FlatBuildSelect = qfill.Edit2
FlatBuildSelect.select()

SelectProgPath = qfill.Button5
SelectProgPath.click()

win = app[r'Открыть файл']
win.type_keys(searchpath+"\prog_emmc_firehose_8953_ddr.mbn{ENTER}")

LoadXML = qfill.Button7
LoadXML.click()

win = app[r'Select RawProgramm File']
win.type_keys("rawprogram0{ENTER}")

win = app[r'Select Patch File']
win.type_keys("patch0{ENTER}")


