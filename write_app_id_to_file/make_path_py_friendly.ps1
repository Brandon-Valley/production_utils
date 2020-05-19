$app_id_abs_path=$args[0]

#set-executionpolicy remotesigned
Write-Output "IN POWERSHELL SCRIPT"

Get-StartApps > $app_id_abs_path

