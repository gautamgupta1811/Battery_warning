import getpass
import os
user = getpass.getuser()


dir_path = os.path.dirname(os.path.realpath(__file__))
data = """
:loop
start python {}\\Battery_check.py
Timeout /t 30 /nobreak
goto :loop""".format(dir_path)

f = open("battery.txt", "w")
f.write(data)
f.close()

f = open("battery.txt", "rb")
data = f.read()
f.close()

os.chdir(r"C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup".format(user))

file = open("battery.bat", "wb")
file.write(data)
file.close()
