from queue import Queue
from idmefv2_transport import get_transport
import logging
import threading

class ServerThread(threading.Thread):
    def __init__(self, url, queue, condition):
        super().__init__()
        self._transport = get_transport(url, queue, content_type='application/json')
        self._url = url
        self._condition = condition

    def run(self):
        logging.info("Starting thread %s on %s", str(threading.current_thread()), self._url)
        self._transport.start()
        with self._condition:
            self._condition.wait()
        self._transport.stop()

class QueueThread(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self._queue = queue

    def run(self):
        while True:
            msg = self._queue.get()
            logging.info("Received %s", str(msg))
            self._queue.task_done()
        queue.join()

logging.basicConfig(level=logging.INFO)
queue = Queue()
condition = threading.Condition()

server_thread = ServerThread('http://127.0.0.1:9999', queue, condition)
queue_thread = QueueThread(queue)

server_thread.start()
queue_thread.start()

queue_thread.join()
server_thread.join()



