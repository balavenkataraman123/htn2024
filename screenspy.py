import win32gui
import time
import requests

# defining the api-endpoint
API_ENDPOINT = "http://pastebin.com/api/api_post.php"

# your API key here
API_KEY = "XXXXXXXXXXXXXXXXX"

# your source code here
source_code = '''
print("Hello, world!")
a = 1
b = 2
print(a + b)
'''

productive_tabs = {}
system_windows = []


def get_GPTOpinion(s):
    # data to be sent to api
    data = {'api_dev_key': API_KEY,
            'api_option': 'paste',
            'api_paste_code': source_code,
            'api_paste_format': 'python'}

    # sending post request and saving response as response object
    r = requests.post(url=API_ENDPOINT, data=data)["response"]
    return r
    

previous_time = time.time()
time_on_task = 0
time_off_task = 0

def winEnumHandler(hwnd, ctx):
    global time_on_task
    global time_off_task    
    if win32gui.IsWindowVisible( hwnd ):
            s = win32gui.GetWindowText(hwnd)
            if len(s) >  0 and not s in system_windows:
                print(s)
                try:
                    v = productive_tabs[s]
                    if v == False:
                        print("unproductive")
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
                        print("unproductive")
                        curr_time = time.time()
                        time_off_task += (curr_time - previous_time)
                        previous_time = curr_time
while True:

    win32gui.EnumWindows( winEnumHandler, None)
    print("-------------------------")
    time.sleep(1)