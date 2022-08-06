import requests
import json
import os
import time

url = "https://api.pushbullet.com/v2/pushes"
data = {'type': 'note', 'title': 'alert', 'body': 'Incorrect posture'}
sess = requests.Session()
sess.auth = ('o.RLH8zyoXrMi06SuU67KDy2bvTFKV2R1Y', '')
sess.headers.update({'Content-Type': 'application/json'})

data = {'type': 'note',
        'title': 'Alert',
        'body': 'Your posture has been wrong for over 5 minutes'}
print('Start')
while True:
    print('Scanning')
    file = os.listdir('.')
    if 'warning.txt' in file:
        print("Sending notification")
        r = sess.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data))
        print(r.status_code)
        os.remove('./warning.txt')
        time.sleep(30)