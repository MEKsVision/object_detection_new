import threading
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

from ObjectDetection import ObjectDetection
from FaceRecognition import FaceRecognition
# Set up code for object detection and face recognition threads

objecteDetection = ObjectDetection()
faceRecognition = FaceRecognition()
t_face = threading.Thread(target=faceRecognition.recognizeFace)
t_obj = threading.Thread(target=objecteDetection.detect)

# Start threads
t_face.start()
t_obj.start()

# Main loop
while True:
    # Check for button 1 press
    if not GPIO.input(25):
        time.sleep(0.2)
        if mode != "face_recognition":
            mode = "face_recognition"
            # Stop object detection thread
            objecteDetection.stopDetecting()
            # Set face_done flag to False
            face_done = False

    # Check for button 2 press
    if not GPIO.input(22):
        time.sleep(0.2)
        if mode != "object_detection":
            mode = "object_detection"
            # Stop face recognition thread
            faceRecognition.stopRecognizing()
            # Set obj_done flag to False
            obj_done = False

    # Check if threads have completed
    if t_face.is_alive() == False:
        face_done = True
    if t_obj.is_alive() == False:
        obj_done = True

    # Exit loop if both threads have completed
#     if face_done and obj_done:
#         break

# Join threads
t_face.join()
t_obj.join()

