import threading


class SharedData:
    """
    A class to store shared data between threads.
    """
    confirm_result = None
    lock = threading.Lock()
