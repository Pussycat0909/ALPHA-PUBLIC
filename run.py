
import os,platform,sys,socket
os.system("clear")
try:
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.connect(("www.google.com", 80))
 pass
except socket.error:print(" CHECK YOUR INTERNET CONNECTION BROOO !!");sys.exit()

try:
    import requests , bs4, pyotp, mechanize, future, stdiomask
except ModuleNotFoundError:
    print("\n INSTALLING MISSING MODULES ")
    os.system("pkg update -y && pkg update -y")
    os.system("pip install pyotp")
    os.system("pip install requests")
    os.system("pip install future")
    os.system("pip install bs4")
    os.system("pip install mechanize")
    os.system("pip install stdiomask")
    exit("\n MODULE HAS BEEN INSTALLED RERUN BY python run.py ")

bit = platform.architecture()[0]
print(" CHECKING FOR UPDATES")
os.system('xdg-open https://www.facebook.com/profile.php?id=100094705456296')
os.system('git pull')
print(" UPDATE DONE !!")
if bit == '32bit':
 print(" 32 BIT DETECTED")
 import RESUM32
elif bit == '64bit':
 print(" 64 BIT DETECTED")
 import RESUM64
