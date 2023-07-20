import os, platform
bit = platform.architecture()[0]
print(" CHECKING FOR UPDATES")
os.system('git pull -q')
if bit == '32bit' :
	print(" 32 BIT DETECTED")
	import new32
	new32.login()
elif bit == '64bit' :
	print(" 64 BIT DETECTED ")
	import new64
	new64.login()
