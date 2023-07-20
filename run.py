import os
print(' CHECKING FOR UPDATES ')
os.system('git pull -q')
try:
 import PUBLIC64
 PUBLIC64.login()
except ImportError:
  import PUBLIC32
  PUBLIC32.login()
