from datetime import datetime
from idmefv2 import Message
import uuid
import sys

def now():
    return datetime.now().isoformat('T')

def new_uuid():
    return str(uuid.uuid4())

def message1():
    msg = Message()
    msg['Version'] = '2.0.3'
    msg['ID'] = new_uuid()
    msg['CreateTime'] = now()
    msg['Analyzer'] = {
        'IP':'127.0.0.1',
        'Name':'foobar',
        'Model':'generic',
        'Category':['LOG'],
        'Data':['Log'],
        'Method':['Monitor'],
    }
    return msg

    
def message2():
    msg = Message()
    msg['Version'] = '2.0.3'
    msg['ID'] = new_uuid()
    msg['CreateTime'] = now()
    msg['Analyzer'] = {
        'IP':'127.0.0.1',
        'Name':'foobar',
        'Model':'generic',
        'Category':['LOG'],
        'Data':['Log'],
        'Method':['Monitor'],
    }
    msg['Sensor'] = [
        {
            'IP':'192.168.1.1',
            'Name':'TheSensor',
            'Model':'TheSensorModel',
        },
        {
            'IP':'192.168.1.2',
            'Name':'TheSensor2',
            'Model':'TheSensor2Model',
        },
    ]
    return msg
