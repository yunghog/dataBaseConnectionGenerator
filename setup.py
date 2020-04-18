#Database Connection Generator
#author : Samartha
import os
os.system('cls')
banner="""
    ██████╗ ██████╗        ██████╗ ██████╗ ███╗   ██╗███╗   ██╗███████╗ ██████╗████████╗
    ██╔══██╗██╔══██╗      ██╔════╝██╔═══██╗████╗  ██║████╗  ██║██╔════╝██╔════╝╚══██╔══╝
    ██║  ██║██████╔╝█████╗██║     ██║   ██║██╔██╗ ██║██╔██╗ ██║█████╗  ██║        ██║
    ██║  ██║██╔══██╗╚════╝██║     ██║   ██║██║╚██╗██║██║╚██╗██║██╔══╝  ██║        ██║
    ██████╔╝██████╔╝      ╚██████╗╚██████╔╝██║ ╚████║██║ ╚████║███████╗╚██████╗   ██║
    ╚═════╝ ╚═════╝        ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝ ╚═════╝   ╚═╝
    ----------create database connection for your project without any effort----------
                                -----by samartha-----
"""
print(banner)
print(':::::DB-Connect:::::')
print('dbGenCli.py - Generate DB Connection via CLI')
print('dbGenGui.py - Generate DB Connection via GUI\n')
print(':::::Checking requirements:::::')
flag=0
try:
    import PyQt5
    print('[#]PyQt5 available')
    flag=1
except ImportError as e:
    print(e)
    install=input('Do you want to download and install PyQt5 module? (y/n)')
    if install=='y':
        try:
            os.system('pip install PyQt5')
            print('Installation success')
            flag=1
        except Exception as e:
            print(e)
            print('Unable to install PyQt5. Try later manually')
            flag=0
        else:
            flag=0
if flag==0:
    print('Unable to DB-Connect')
    print(':::::Setup Failed:::::')
else:
    print('Now you can run DB-Connect')
    print(':::::Setup completed:::::')
