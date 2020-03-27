from globals import *
import threading
import time


class Master:
    _next_block_start = 0
    slave_messages = []

    def __init__(self,starting_value):
        self._next_block_start = starting_value



    def send_work(self):
        # dest = (COLLEAGUE, COLLEAGUE_LISTEN_PORT)
        if Master.slave_messages == [()]:
            # print("WARN: Attempt to process message on empty message queue in master")
            time.sleep(1)
            return

        print("message list size", len(Master.slave_messages))

        print(Master.slave_messages)
        message, sender = Master.slave_messages.pop()
        sender_addr = sender[0]
        print("Handeling message from:", sender_addr)

        if message == SLAVE_REQ_WORK:
            print("Sending work to slave: ", sender_addr)

            dest = (sender_addr, FROM_MASTER_PORT)

            msg = str(self._next_block_start)
            self._next_block_start = self._next_block_start + WORK_BLOCK_SIZE
            print("Sending message to slave:", sender)
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            s.sendto(msg.encode(), dest)

    def _listen_thread(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.bind(('', MASTER_DIRECT_PORT))
        print("Listening for chatter from slaves on port:", MASTER_DIRECT_PORT)
        while True:
            message, address = s.recvfrom(COLLEAGUE_LISTEN_PORT)
            print("Received message from slave", message.decode(), " from ", address)
            Master.slave_messages.append((message.decode(), address))

    def listen(self):
        thread_exit = threading.Thread(target=self._listen_thread).start()
        if thread_exit is not None:
            print("Failed to spawn thread to listen for messages to master with error string: ", thread_exit)
            exit(1)
        else:
            print("Master listener thread running on port:",MASTER_DIRECT_PORT)

        thread_exit = threading.Thread(target=self._message_handeler).start()
        if thread_exit is not None:
            print("Failed to spawn thread to handle messages to master with error string: ", thread_exit)
            exit(1)
        else:
            print("Master handeler thread running")

    def _message_handeler(self):
        while True:
            if len(Master.slave_messages) != 0:
                self.send_work()

