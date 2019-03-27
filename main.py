# Automatic 
from pywinauto import application, keyboard

path = r'C:\Program Files (x86)\Qualcomm\QPST\bin\QFIL.exe'
searchpath = r'C:\Users\User\Downloads\Note8\images'

def runwindow(app_name, keys):
    """
    Open window by Window_Name and type some text in window from keyboard
    :param app_name: window name
    :param keys: enter data from keyboard to window
    """
    win = app[app_name]
    win.type_keys(keys)

app = application.Application()
app.start(path)
qfill = app[u'WindowsForms10.Window.8.app.0.190610d_r9_ad1']
qfill.wait('ready')
FlatBuildButton = qfill.Button3
FlatBuildButton.click()
FlatBuildSelect = qfill.Edit2
FlatBuildSelect.select()
SelectProgPath = qfill.Button5
SelectProgPath.click()
mbn = searchpath+"\prog_emmc_firehose_8953_ddr.mbn{ENTER}"
runwindow(r'Открыть файл', mbn)
LoadXML = qfill.Button7
LoadXML.click()
runwindow(r'Select RawProgramm File', "rawprogram0{ENTER}")
runwindow(r'Select Patch File', "patch0{ENTER}")


