import os
import time

timer = int(input('Shutdown your computer after the given minutes :'))
print('Cumputer is shutdown in ', timer, 'minutes!')
time.sleep(timer*60)
os.system('cmd /c "shutdown /p /f"')
