class ObservableList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.callbacks = []

#     def __setitem__(self, index, value):
#         super().__setitem__(index, value)
#         for callback in self.callbacks:
#             callback(self)
            
    def append(self, item):
        super(ObservableList, self).append(item)
        for callback in self.callbacks:
            callback(self)

    def register_callback(self, callback):
        self.callbacks.append(callback)
