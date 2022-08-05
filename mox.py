import requests
import json
import os
import time

url = "https://api.pushbullet.com/v2/pushes"
data = {'type': 'note', 'title': 'alert', 'body': 'Incorrect posture'}
sess = requests.Session()
sess.auth = ('o.JIYB9LelVfWIJEeL8ovfxTbDDxjwRcAu', '')
sess.headers.update({'Content-Type': 'application/json'})

data = {'type': 'note',
        'title': 'Alert',
        'body': 'Your posture has been wrong for over 5 minutes'}
while True:
    file = os.listdir('.')
    if 'warning.txt' in file:
        r = sess.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data))
        os.remove('./warning.txt')

