# coding: utf-8
from orgparse import load
from datetime import datetime, date
import configparser

config = configparser.ConfigParser()
print(config.sections())
config.read('config.ini')
print(config.sections())

assert 'AGENDAS' in config

now = datetime.now()
for section in config["AGENDAS"]:
    path = config["AGENDAS"][section]
    print(path)
    root = load(path)

    
    for node in root[1:]:
        if node.scheduled:
            start = node.scheduled.start
            args = start.timetuple()[:6]
            start = datetime(*args)
            delta = now - start 
            if delta.days <= 0:
                print(node)
                print(node.scheduled.start)
    
