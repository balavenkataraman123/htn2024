import simpleaudio as sa
import win32gui
import time
import requests
import pyttsx3

engine = pyttsx3.init()
import soundfile as sf
import soundcard as sc
default_speaker = sc.default_speaker()

api_key = 'VF.DM.66e6a243380effe3d506deda.re9t77w7eQcP5gkk' # it should look like this: VF.DM.XXXXXXX.XXXXXX... keep this a secret!
user_id = 'random_shit'
# user_id defines who is having the conversation, e.g. steve, john.doe@gmail.com, username_464
name = "deeznuts"
todo = input("What do you want to do today? ")

def interact(user_id, request):
    response = requests.post(
        f'https://general-runtime.voiceflow.com/state/user/{user_id}/interact',
        json={ 'request': request },
        headers={ 'Authorization': api_key },
    )
    for trace in response.json():
        if trace['type'] == 'speak' or trace['type'] == 'text':
            return (trace['payload']['message'])
        elif trace['type'] == 'end':
            # an end trace means the the voiceflow dialog has ended
            return None
    return None

def get_GPTOpinion(tab):
    AIOutput = interact(name, { 'type': 'launch' })
    nextInput = tab
    AIOutput = interact(name, { 'type': 'text', 'payload': nextInput })
    nextInput = todo
    AIOutput = interact(name, { 'type': 'text', 'payload': nextInput })
    if AIOutput[0] == "Y":
        return True
    else:
        return False

productive_tabs = {}

system_windows = ["Task Switching",
"Windows PowerShell",
"New Tab - Google Chrome",
"screenspy.py - Hack_The_North_2024 - Visual Studio Code",
"Windows Shell Experience Host",
"Setup",
"Realtek Audio Console",
"Mail",
"Settings",
"Windows Input Experience",
"Program Manager"]

previous_time = time.time()
time_on_task = 0
time_off_task = 0

currently_unproducive = 0
unproductivity_window = ""


def winEnumHandler(hwnd, ctx):
    global previous_time
    global time_on_task
    global time_off_task
    global currently_unproducive    
    global unproductivity_window
    past_windows = []
    if win32gui.IsWindowVisible( hwnd ):
        s = win32gui.GetWindowText(hwnd).strip("*●  ")
        if len(s) >  0 and not s in system_windows and not s in past_windows:
            print(s)
            past_windows.append(s)
            try:
                v = productive_tabs[s]
                if v == False:
                    currently_unproducive += 1
                    unproductivity_window = s
                    if currently_unproducive == 1:
                        samples, samplerate = sf.read('nudge.wav')
                        default_speaker.play(samples, samplerate=samplerate)
                    curr_time = time.time()
                    time_off_task += (curr_time - previous_time)
                    previous_time = curr_time
                else:
                    curr_time = time.time()
                    time_on_task += (curr_time - previous_time)
                    previous_time = curr_time
            except:
                if get_GPTOpinion(s):
                    
                    productive_tabs[s] = True
                    curr_time = time.time()
                    time_on_task += (curr_time - previous_time)
                    previous_time = curr_time
                else:
                    productive_tabs[s] = False
                    unproductivity_window = s
                    currently_unproducive += 1
                    if currently_unproducive == 1:
                        samples, samplerate = sf.read('nudge.wav')
                        default_speaker.play(samples, samplerate=samplerate)
                    curr_time = time.time()
                    time_off_task += (curr_time - previous_time)
                    previous_time = curr_time

    if currently_unproducive == 20:
        samples, samplerate = sf.read(f'{unproductivity_window}.wav')
        default_speaker.play(samples, samplerate=samplerate)
        currently_unproducive = 0

while True:
    win32gui.EnumWindows( winEnumHandler, None)
    time.sleep(1)