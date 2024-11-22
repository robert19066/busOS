import os
import argparse
from tqdm import tqdm
import time
import subprocess
from pydub import AudioSegment # type: ignore
from pydub.playback import play # type: ignore


class BootFailedExeption(Exception):
    def __init__(self, age, message="Boot Failed Reason:Unknown"):
        self.age = age
        self.message = message
        super().__init__(self.message)



def play_Beep_Beep():
    audio = AudioSegment.from_mp3("C:/Users/Lenovo/Desktop/busOS/core/beep.mp3")
    
    print("""

 ____  _    _ ____   ____  ____   ____   _____ 
| __ )| |  | | __ ) / ___||  _ \ / ___| |_   _|
|  _ \| |  | |  _ \ \___ \| |_) | |  _    | |  
| |_) | |__| | |_) | ___) |  __/| |_| |   | |  
|____/ \____/|____/ |____/|_|    \____|   |_|  
                                            
  B.U.S OS - The Basic Ultra Small OS

      """)
    print("Starting comand line...")
    time.sleep(1.5)
    os.system('cls')
    startComandLine()
    play(audio)


def startComandLine():
    subprocess.run(["python", "C:/Users/Lenovo/Desktop/busOS/core/comand.py"])

os.system('cls')
for _ in tqdm(range(100), desc="BOOTING...", ascii=False, ncols=75): 
    time.sleep(0.05)

try:
    os.system('cls')
    play_Beep_Beep()
except PermissionError:
    os.system('cls')
    print("""
  ____              ____  
 / ___| _ __  _   _|  _ \ 
 \___ \| '_ \| | | | | | |
  ___) | |_) | |_| | |_| |
 |____/| .__/ \__, |____/ 
       |_|    |___/       

A problem has been detected and B.U.S OS has been shut down to prevent damage
to your computer.

The problem seems to be caused by the following file: startOS.core

If this is the first time you've seen this Stop error screen,
restart your computer. If this screen appears again, follow
these steps:

Check to make sure any new hardware or software is properly installed.
If this is a new installation, ask your hardware or software manufacturer
for any B.U.S OS updates you might need.

If problems continue, disable or remove any newly installed hardware
or software. Disable BIOS memory options such as caching or shadowing.
If you need to use Safe Mode to remove or disable components, restart
your computer, press F8 to select Advanced Startup Options, and then
select Safe Mode.

Technical Information:

*** Kernel Panic Error.
    Reason:BOOTUP_SOUND_NOT_FOUND

Beginning dump of physical memory
Physical memory dump complete.
Contact your system administrator or technical support group for further
assistance.

              """)
except Exception:
     print("""
  ____              ____  
 / ___| _ __  _   _|  _ \ 
 \___ \| '_ \| | | | | | |
  ___) | |_) | |_| | |_| |
 |____/| .__/ \__, |____/ 
       |_|    |___/       

*** B.U.S OS STOP ERROR ***

A problem has been detected and B.U.S OS has been shut down to prevent damage
to your computer.

The problem seems to be caused by the following file: BEEP.sys

STOP: 0x0000001E (0xFFFFFFFFC0000005, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000)

Your computer has been shut down to prevent damage.
If this is the first time you've seen this Stop error screen,
restart your computer. If this screen appears again, follow
these steps:

1. Check to make sure any new hardware or software is properly installed.
2. If this is a new installation, ask your hardware or software manufacturer
   for any updates you might need.

*** Technical Information ***

*** Kernel Panic Error
    Reason:UNKNOWN_CRIT_ERROR
           

Beginning dump of physical memory.
Dumping physical memory to disk....

Contact your system administrator or technical support group for further
assistance.

              """)

except BootFailedExeption:
    print("""
 ____              ____  
 / ___| _ __  _   _|  _ \ 
 \___ \| '_ \| | | | | | |
  ___) | |_) | |_| | |_| |
 |____/| .__/ \__, |____/ 
       |_|    |___/       

*** B.U.S OS STOP ERROR ***

A problem has been detected and B.U.S OS has been shut down to prevent damage
to your computer.

The problem seems to be caused by the following file: BEEP.sys

STOP: 0x0000001E (0xFFFFFFFFC0000005, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000)

Your computer has been shut down to prevent damage.
If this is the first time you've seen this Stop error screen,
restart your computer. If this screen appears again, follow
these steps:

1. Check to make sure any new hardware or software is properly installed.
2. If this is a new installation, ask your hardware or software manufacturer
   for any updates you might need.

*** Technical Information ***

*** Bootup Failed

Beginning dump of physical memory.
Dumping physical memory to disk:...

Contact your system administrator or technical support group for further
assistance.


              """)