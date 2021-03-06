import requests
import json
import datetime

def getlisteners(url):
    stats = json.loads(requests.get(url).text)
    print(stats)
    for source in stats['icestats']['source']:
        if source['listenurl'] == 'http://nebula.shoutca.st:8491/stream':
            listeners = source['listeners']
    #except KeyError:
     #   listeners = stats['icestats']['source']['listeners']
    return listeners

def now():
    return datetime.datetime.utcnow()

newdata = {}
newdata['time'] = str(now())
newdata['listeners'] = getlisteners('https://phantommedia.radioca.st/status-json.xsl')
print(newdata)

try:
    with open('_data/PhantomListeners.json','r', encoding='utf-8', newline='\n') as f:
        olddata = json.loads(f.read())
except FileNotFoundError:
    old_data = []

olddata.append(newdata)

with open('_data/PhantomListeners.json','wt', encoding='utf-8', newline='\n') as f:
    f.write(json.dumps(olddata,indent=4)+"\n")
    print(now(),"PhantomListeners.json saved")

with open('_data/PhantomListeners.csv','a', encoding='utf-8', newline='\n') as f:
    f.write(str(newdata['time'])+','+str(newdata['listeners'])+'\n')
    print(now(),"PhantomListeners.csv saved")
