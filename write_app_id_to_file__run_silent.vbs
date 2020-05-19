Set objFS=CreateObject("Scripting.FileSystemObject")
Set objArgs = WScript.Arguments
ps1Path= objArgs(0)
ps1Arg= objArgs(1)

command = "powershell.exe -nologo -command " + ps1Path + " " + ps1Arg
 set shell = CreateObject("WScript.Shell")
 shell.Run command,0