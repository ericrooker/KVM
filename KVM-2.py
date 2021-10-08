from guizero import App, PushButton
from PIL import Image
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

path = '/home/pi/TouchScreenRelayPanel/'
DPS_state = 1
USHMM_state = 0
XRAY_state = 0
CROSSMATCH_state = 0

def DPS_callback():
    global DPS_state, DPS_button
    DPS_state = 1
    DPS_button.image = path + 'DPS_on.png'
    GPIO.setup(29, GPIO.OUT)
    GPIO.output(29, GPIO.HIGH)
    USHMM_button.image = path + 'USHMM_off.png'
    GPIO.setup(31, GPIO.OUT)
    GPIO.output(31, GPIO.LOW)
    XRay_button.image = path + 'XRay_off.png'
    GPIO.setup(33, GPIO.OUT)
    GPIO.output(33, GPIO.LOW)
    CrossMatch_button.image = path + 'CrossMatch_off.png'
    GPIO.setup(37, GPIO.OUT)
    GPIO.output(37, GPIO.LOW)

def USHMM_callback():
    global USHMM_state, USHMM_button
    USHMM_state = 1
    USHMM_button.image = path + 'USHMM_on.png'
    GPIO.setup(31, GPIO.OUT)
    GPIO.output(31, GPIO.HIGH)
    DPS_button.image = path + 'DPS_off.png'
    GPIO.setup(29, GPIO.OUT)
    GPIO.output(29, GPIO.LOW)
    XRay_button.image = path + 'XRay_off.png'
    GPIO.setup(33, GPIO.OUT)
    GPIO.output(33, GPIO.LOW)
    CrossMatch_button.image = path + 'CrossMatch_off.png'
    GPIO.setup(37, GPIO.OUT)
    GPIO.output(37, GPIO.LOW)

def XRAY_callback():
    global XRAY_state, XRay_button
    XRAY_state = 1
    XRay_button.image = path + 'XRay_on.png'
    GPIO.setup(33, GPIO.OUT)
    GPIO.output(33, GPIO.HIGH)
    DPS_button.image = path + 'DPS_off.png'
    GPIO.setup(29, GPIO.OUT)
    GPIO.output(29, GPIO.LOW)
    USHMM_button.image = path + 'USHMM_off.png'
    GPIO.setup(31, GPIO.OUT)
    GPIO.output(31, GPIO.LOW)
    CrossMatch_button.image = path + 'CrossMatch_off.png'
    GPIO.setup(37, GPIO.OUT)
    GPIO.output(37, GPIO.LOW)

def CROSSMATCH_callback():
    global CROSSMATCH_state, CrossMatch_button
    CROSSMATCH_state = 1
    CrossMatch_button.image = path + 'CrossMatch_on.png'
    GPIO.setup(37, GPIO.OUT)
    GPIO.output(37, GPIO.HIGH)
    DPS_button.image = path + 'DPS_off.png'
    GPIO.setup(29, GPIO.OUT)
    GPIO.output(29, GPIO.LOW)
    USHMM_button.image = path + 'USHMM_off.png'
    GPIO.setup(31, GPIO.OUT)
    GPIO.output(31, GPIO.LOW)
    XRay_button.image = path + 'XRay_off.png'
    GPIO.setup(33, GPIO.OUT)
    GPIO.output(33, GPIO.LOW)

app = App(title="KVM", width=800, height=480, layout="grid")
app.bg='black'
DPS_button = PushButton(app, command=DPS_callback, grid=[0,0], align='left', image = path + 'DPS_on.png')
USHMM_button = PushButton(app, command=USHMM_callback, grid=[1,0], align='left',image = path + 'USHMM_off.png')
XRay_button  = PushButton(app, command=XRAY_callback, grid=[0,1], align='left',image = path + 'XRay_off.png')
CrossMatch_button  = PushButton(app, command=CROSSMATCH_callback, grid=[1,1], align='left',image = path + 'CrossMatch_off.png')

def main():
    app.tk.attributes("-fullscreen",True)
    app.tk.config(cursor='none')
    app.display()

if __name__ == '__main__':
    main()



