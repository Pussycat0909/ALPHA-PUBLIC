import os, platform
print(' CHECKING FOR UPDATES ')
os.system('git pull -q')
bit = platform.architecture()[0]
print(" CHECKING FOR UPDATES")
os.system('git pull -q')
if bit == '32bit' :
	print(" 32 BIT DETECTED")
	import PUBLIC32
 PUBLIC32.login()
elif bit == '64bit' :
	print(" 64 BIT DETECTED ")
	import PUBLIC64
 PUBLIC64.login()
