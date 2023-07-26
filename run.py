
import os,platform

try:
    import openai , requests , bs4, pyotp, mechanize, future
except ModuleNotFoundError:
    print("\n INSTALLING MISSING MODULES ")
    os.system('pip install pyotp -q && pip install mechanize -q && pip install future -q && pip install openai -q && pip install requests --quiet && pip install bs4 --quiet')
    exit("\n MODULE HAS BEEN INSTALLED RERUN BY python run.py ")

bit = platform.architecture()[0]
print(" CHECKING FOR UPDATES ")
os.system('git pull -q')
if bit == '32bit':
 print(" 32 BIT DETECTED")
 import NEW32
 NEW32.login()
elif bit == '64bit':
 print(" 64 BIT DETECTED")
 import NEW64
 NEW64.login()