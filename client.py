from idmefv2_transport import get_transport
import util
import time

transport = get_transport('http://127.0.0.1:9999', content_type="application/json")
transport.start()

b = True
while True:
    transport.send_message(util.message1() if b else util.message2())
    b = not b
    time.sleep(3)

transport.stop()
