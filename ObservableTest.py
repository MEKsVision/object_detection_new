# import time
# class ObservableValue:
#     def __init__(self, initial_value=None):
#         self._value = initial_value
#         self._callbacks = []
#     
#     def __call__(self,initial_value=None):
#         self._value = initial_value
#         return self._value
#     
#     def __set__(self, instance, value):
#         self._value = value
#         for callback in self._callbacks:
#             callback(value)
#     
#     def register_callback(self, callback):
#         self._callbacks.append(callback)
# 
# # from ObservableValue import ObservableValue
# 
# mode = ObservableValue(1)
# time.sleep(5)
# print("working")
# mode(2)
# 
# def modeSwitched(new_value):
#     print(f"The value has changed to {new_value}")
#     
# mode.register_callback(modeSwitched)

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

# from ObservableValue import ObservableValue
mode = ObservableValue("face_recognition")
def modeSwitched(new_value):
    print(f"The value has changed to {new_value}")
    
mode.register_callback(modeSwitched)

#mode("asdfasdf")
#mode.__set__("asdf")
value = mode.get_value()
print(value)
#print(value)
#mode.__set__("asdf")




