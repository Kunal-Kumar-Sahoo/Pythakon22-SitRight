import requests
import json

url = "https://api.pushbullet.com/v2/pushes"
data = {'type': 'note', 'title': 'alert', 'body': 'Incorrect posture'}
sess = requests.Session()
sess.auth = ('o.otJ6smKZPxOokYuq9Gsm3R1FqzheyORM', '')
sess.headers.update({'Content-Type': 'application/json'})

data = {'type': 'note',
        'title': 'Alert',
        'body': 'Your posture has been wrong for over a minute'}
r = sess.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data))
print(r.text)
