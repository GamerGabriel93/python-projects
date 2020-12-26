import os
import time

timer = int(input('Leállítás ennyi idő után (percben) :'))
print('A számítógép', timer, 'perc múlva kikapcsol!')
time.sleep(timer*60)
os.system('cmd /c "shutdown /p /f"')
