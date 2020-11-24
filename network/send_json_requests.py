import requests
import json
import sys

address = "http://127.0.0.1:60001" 
headers = {'content-type': 'application/json', 'Accept': 'text/plain'}

# with open(sys.path[0]+'\\task_cmds.json','r') as f:
with open(sys.path[0]+'\\request.json','r') as f:
    cmds = json.load(f)
    for cmd in cmds:
        url = address + cmd["url"]
        # print(cmd)
        r = requests.post(url, json=cmd,headers=headers)
        print(r)
        print(r.text)
