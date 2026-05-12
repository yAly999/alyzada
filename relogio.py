import time 
import sys
import os
import platform

def shutdown():
    sistema = platform.system().lower()
    try:
        if "windows" in sistema:
            os.system("shutdown /s /t 0")
        elif "linux" in sistema or "darwin" in sistema:
            os.system("shutdown -h now")    
    except Exception as e:
        print(f"Error occurred while trying to shutdown: {e}")