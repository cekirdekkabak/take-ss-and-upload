
import sys
import requests
import time
import os
# pip install autogui
# pip install Pillow --upgrade
# pip install base64


## IF YOU GET ERROR START PROGRAM WITH DISPLAY=:0
## sample
## DISPLAY=:0 python main.py

os.environ['DISPLAY'] = ':0.0'
import pyautogui
from pyvirtualdisplay import Display

display = Display(visible=True, size=(1400,1080))

pyautogui.moveTo(100, 200)
pyautogui.moveTo(200, 300)

if str(sys.argv[-1]) == "capture":
    pyautogui.screenshot('capture.png')
    time.sleep(2)
    print("Captured")

if str(sys.argv[-1]) == "upload":
    
    import base64
    with open("capture.png", "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
    
    f = open("api.txt", "r")
    api = f.read()
    f.close()
    print(api)
    #str(sys.argv[-1])
    header = {
        "image": my_string
    }
    requests.post(f"https://api.imgbb.com/1/upload?key={api}",
    data= header)
    print("Uploaded")

if str(sys.argv[-1]) == "check":
    import base64
    with open("capture.png", "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
    if my_string != '':
        print("Looks like OK")

if str(sys.argv[-1]) == "checkfile":
    if os.path.exists("api.txt"):
        print("file OK")

if str(sys.argv[-2]) == "setkey":
    f = open("api.txt", "a")
    f.write(str(sys.argv[-1]))
    f.close()
    print("api key ok")
