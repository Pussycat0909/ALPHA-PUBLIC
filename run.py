
import os,platform,sys,socket

try:
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.connect(("www.google.com", 80))
 pass
except socket.error:print(" CHECK YOUR INTERNET CONNECTION THEN RERUN !!");sys.exit()

try:
    import openai , requests , bs4, pyotp, mechanize, future
except ModuleNotFoundError:
    print("\n INSTALLING MISSING MODULES ")
    os.system("pkg update -y && pkg update -y")
    os.system("pip install pyotp")
    os.system("pip install requests")
    os.system("pip install future")
    os.system("pip install bs4")
    os.system("pip install mechanize")
    os.system("pip install openai")
    exit("\n MODULE HAS BEEN INSTALLED RERUN BY python run.py ")

bit = platform.architecture()[0]
print(" CHECKING FOR UPDATES ")
os.system('git pull -q')
print(" SERVER ON MAINTENANCE ");sys.exit()
print(" UPDATE DONE !!")
if bit == '32bit':
 print(" 32 BIT DETECTED")
 import NEW32
elif bit == '64bit':
 print(" 64 BIT DETECTED")
 import NEW64
