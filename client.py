from idmefv2_transport import get_transport
from idmefv2 import Message
import sys
import time
import uuid
from datetime import datetime
import jsonschema.exceptions
import util
    
transport = get_transport('http://127.0.0.1:9999', content_type="application/json")
transport.start()

while True:
    transport.send_message(util.message1())
    time.sleep(5)

transport.stop()
