from pywinauto import application
import os
searchpath = r'C:\Users\User\Downloads\Note8\images'
app = application.Application()
path = r'C:\Program Files (x86)\Qualcomm\QPST\bin\QFIL.exe'
app.start(path)
FlatBuildForm = app[u'WindowsForms10.Window.8.app.0.190610d_r9_ad1']
FlatBuildForm.wait('ready')
FlatBuildButton = FlatBuildForm.Button3
FlatBuildButton.click()
FlatBuildSelect = FlatBuildForm.Edit2
FlatBuildSelect.select()

[u'C:\\', u'C:\\']
