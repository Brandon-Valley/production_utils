import os, winshell
from win32com.client import Dispatch
desktop = winshell.desktop()
path = os.path.join('C:\\projects\\version_control_scripts\\CE\\sms\\production_utils', "Media Player Classic.lnk")
target = r"P:\Media\Media Player Classic\mplayerc.exe"
wDir = r"P:\Media\Media Player Classic"
icon = r"P:\Media\Media Player Classic\mplayerc.exe"
shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
# shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.write('Targetpath=P:\Media\Media Player Classic\mplayerc.exe')
shortcut.save()