import threading

class SharedData:
    confirm_result = None
    lock = threading.Lock()