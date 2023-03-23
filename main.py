import threading
import time
import RPi.GPIO as GPIO

from ObservableValue import ObservableValue

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

from ObjectDetection import ObjectDetection
from FaceRecognition import FaceRecognition

objecteDetection = ObjectDetection()
faceRecognition = FaceRecognition()
t = threading.Thread(target=faceRecognition.recognizeFace)
t2 = threading.Thread(target=objecteDetection.detect)

mode = ObservableValue("face_recognition")

def modeSwitched(new_value):
    print(f"The value has changed to {new_value}")
    if new_value == "face_recognition":
        objecteDetection.stopDetecting()
        t.start()
    elif new_value == "object_detection":
        faceRecognition.stopRecognizing()
        t2.start()

    
mode.register_callback(modeSwitched)

# Main loop
while True:
    if not GPIO.input(25):
        time.sleep(0.2)
        old_value = mode.get_value()        
        if old_value !="face_recognition":
            mode.__set__("face_recognition")
            
        print("Button 1 pressed")
    if not GPIO.input(22):
        time.sleep(0.2)
        
        old_value = mode.get_value()
        if old_value !="object_detection":
            mode.__set__("object_detection")
            #Object Detection Mode Start Here
#             faceRecognition.stopRecognizing()
#             t2.start()
            #Object Detection Mode End Here
        print("Button 2 pressed")
            

# mode.__set__("aaa")
#     if not GPIO.input(24):
#         time.sleep(0.2)
#         print("Button 3 pressed")
#     if not GPIO.input(23):
#         time.sleep(0.2)
#         print("Button 4 pressed")


# t = threading.Thread(target=faceRecognition.recognizeFace)
# t.start()
# # 
# time.sleep(20)
# faceRecognition.stopRecognizing()
# 
# t2 = threading.Thread(target=objecteDetection.detect)
# t2.start()




#time.sleep(100)
# print("working")
# 
# t.join()
# t2.join()