import json
import re
import pprint

with open('./data.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '').split("****+++****")

for i in data:
    i = i[1:]
    i = i[:-1]
    if len(i)>0:
        new = json.loads(json.dumps(i))

from io import StringIO
newio = StringIO(new)
print(json.load(newio)['statuses'][1]['created_at'])
