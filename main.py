from pywinauto import application
import os

app = application.Application()
path = r'C:\Program Files (x86)\Qualcomm\QPST\bin\QFIL.exe'
app.start(path)