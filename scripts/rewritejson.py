#!/usr/bin/python

# rewritejson.py reads in a NWR timeline json file and extracts the events, their participants and times
# and writes it to a format that elasticsearch can read in 

# Author: Marieke van Erp
# Date: 3 November 2015

import sys
import json
from pprint import pprint

corpus=sys.argv[1]
with open('/Users/filipilievski/phd/y3demos/data/timeline-data/json/' + corpus  + '_contextual.timeline.json') as data_file:    
    data = json.load(data_file)
   
eid = 1
events = {}
for event in data['timeline']['events']:
    events['id'] = str(eid)
    events['event'] = event['event']
    events['climax'] = event['climax']
    events['time'] = event['time'][:4] + '-' + event['time'][4:6] + '-' + event["time"][6:] + 'T00:00:00.000Z'
    events['size'] = event['size']
    events['label'] = event['labels']
    events['fnsuperframes'] = event['fnsuperframes']
    events['actors'] = []
    for actor in event['actors'].keys():
        if 'fn' in actor:
            for value in event['actors'].values():
                events['actors'].append(value)
    eid = eid + 1
    print '{ "index" : { "_index" : "stock", "_type" : "events", "_id" :', eid, '} }'
    print json.dumps(events)


#pprint(data)
