import threading
import time

class MyClass:
    def __init__(self):
        self._running = True
        
    def my_loop(self):
        while self._running and True:
            print("Running...")
            time.sleep(1)
        
    def stop(self):
        self._running = False
        
my_object = MyClass()

# Start the loop in a new thread
thread = threading.Thread(target=my_object.my_loop)
thread.start()

# Wait for 5 seconds
time.sleep(5)


# Stop the loop by calling stop() on the object from the main thread
my_object.stop()
print("stopped")

# Wait for the thread to finish
thread.join()
