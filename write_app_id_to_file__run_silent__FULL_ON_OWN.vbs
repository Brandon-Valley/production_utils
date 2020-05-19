

command = "powershell.exe -nologo -command 'Get-StartApps > $app_id_abs_path'"
 set shell = CreateObject("WScript.Shell")
 shell.Run command,0