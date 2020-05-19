import traceback
import subprocess
import os

if __name__ == "__main__": 
    from   usms.msg_box_utils import msg_box_utils as mbu 
    import                           util_tools    as ut
else:
    from . usms.msg_box_utils import msg_box_utils as mbu
    from .                    import util_tools    as ut
    

APPS_ID_FILE_PATH                          = os.path.dirname(os.path.abspath(__file__)) + '\app_ids.txt'
WRITE_APP_ID_TO_FILE__RUN_SILENT__VBS_PATH = os.path.dirname(os.path.abspath(__file__)) + '\write_app_id_to_file__run_silent.vbs'
WRITE_APP_ID_TO_FILE__PS1_PATH             = os.path.dirname(os.path.abspath(__file__)) + '\write_app_id_to_file.ps1'


def show_popup_on_uncaught_exception__if__is_production(func, is_production = True):
    
    def show_error_msg_box(e):
        title = 'Unspecified Exception'
        msg = 'An uncaught exception has occurred:\n\n' + str(e)
        
        msg_box_result = mbu.msg_box__OK(title, msg, icon = 'stop')
        
        
    try:
        func()
    except:
        error_info = traceback.format_exc()
        
        if is_production:
            show_error_msg_box(error_info)
        else:
            raise
        

        
def get_app_id_of__file__(file_obj):
    ''' must be passed __file__ '''
    exe_name_no_ext = ut.get_basename_from_path(file_obj, include_ext = False) 
    exe_name = exe_name_no_ext + '.exe'
    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
#     cmd = 'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe ' + WRITE_APP_ID_TO_FILE_PS1_PATH
#     cmd = '{} {} {} '.format(WRITE_APP_ID_TO_FILE__RUN_SILENT__VBS_PATH, WRITE_APP_ID_TO_FILE__PS1_PATH, APPS_ID_FILE_PATH)
#     print(cmd)#``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
#     subprocess.Popen(cmd, shell = False)
#     os.system("C:\\projects\\version_control_scripts\\CE\\sms\\production_utils\\write_app_id_to_file__run_silent.vbs" "C:\\projects\\version_control_scripts\\CE\\sms\\production_utils\\write_app_id_to_file.ps1" "C:\\projects\\version_control_scripts\\CE\\sms\\production_utilspp_ids.txt" 
#     os.system(cmd)

#     cmd = "C:\\projects\\version_control_scripts\\CE\\sms\\production_utils\\write_app_id_to_file__run_silent.lnk.lnk"
    cmd = 'cscript "C:\\projects\\version_control_scripts\\CE\\sms\\production_utils\\write_app_id_to_file__run_silent__NO_ARGS_TEST.vbs"'
    subprocess.call(cmd, shell = False)
#     subprocess.Popen(cmd, shell = False)
#     os.system(cmd)


    
#     lines = ut.read(APPS_ID_FILE_PATH)
#     
#     for line in lines:
#         print('line: ', line)
#         if line.startswith(exe_name):
#             print('line: ', line)
            
    
    
    

if __name__ == '__main__':
    print('In Main:  Production_utils')
    get_app_id_of__file__('aaa//main.py')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    print('End of Main: Production_utils')