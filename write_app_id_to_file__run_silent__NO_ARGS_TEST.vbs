Wscript.Echo "in vbs script"

command = "powershell.exe -nologo -command C:\projects\version_control_scripts\CE\sms\production_utils\write_app_id_to_file.ps1 C:\\projects\\version_control_scripts\\CE\\sms\\production_utils\\app_ids.txt"
 set shell = CreateObject("WScript.Shell")
 shell.Run command,0