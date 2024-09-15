import requests # pip install requests

api_key = 'VF.DM.66e6a243380effe3d506deda.re9t77w7eQcP5gkk' # it should look like this: VF.DM.XXXXXXX.XXXXXX... keep this a secret!

# user_id defines who is having the conversation, e.g. steve, john.doe@gmail.com, username_464
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

name = "deeznuts"

AIOutput = interact(name, { 'type': 'launch' })

for i in range(2):
    nextInput = input('> Say something\n')
    AIOutput = interact(name, { 'type': 'text', 'payload': nextInput })
    print(AIOutput)

