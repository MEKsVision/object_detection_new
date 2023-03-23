class ObservableValue:
    def __init__(self, initial_value=None):
        self._value = initial_value
        self._callbacks = []
    
    def __call__(self, initial_value=None):
        return self._value
    
    def get_value(self):
        return self._value
    
    def __set__(self,value):
        self._value = value
        for callback in self._callbacks:
            callback(value)
    
    def register_callback(self, callback):
        self._callbacks.append(callback)