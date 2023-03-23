import cv2
import face_recognition
import time
import pyttsx3
import threading

from simple_facerec import SimpleFacerec
from ObservableList import ObservableList

class FaceRecognition(threading.Thread):
    
    def __init__(self):
        self._isRecognizing = True
        self._stop_event = threading.Event()
        #self._cap = cv2.VideoCapture(0)
    
    def recognizeFace(self):
        sfr = SimpleFacerec()
        sfr.load_encoding_images("persons/")
        # Audio Generation
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-30)
        engine.say("System চালু holo")
        engine.runAndWait()


        cap = cv2.VideoCapture(0)

        def handle_list_change(all_name):
            

            
            text = "";
            all_person_names = [elem[0] for elem in all_name]

        #     for n in all_person_names:
        #         text += n + (" and " if (n == all_person_names[-1] and len(all_person_names)>1) else ", ")
        #     
        #     text += "is here"
            if len(all_person_names) == 2:
                text = " েএবং ".join(all_person_names) + " েএখানে"
            elif len(all_person_names) > 2:
        #         last_index = len(all_person_names) - 1
        #         except_last_value = all_person_names.pop()
        #         print("Working")
        #         print(except_last_value)
        #         print(last_index)
        #         print("hhhh")
        # #         print(except_last_value)
        #         text = " and ".join(except_last_value) + " and " + all_person_names[-1] + " are here"
                text = " , ".join(all_person_names) + " েএখানে"
            elif len(all_person_names) == 1:
                text = all_person_names[0] + " েএখানে"
            
            engine.say(text)
            engine.runAndWait()
            
            print("List changed to:", text)
        
        all_name = ObservableList([])
        all_name.register_callback(handle_list_change)

        #while self._isRecognizing:
        while cap.isOpened() and self._isRecognizing and not self._stop_event.is_set():
            _,frame = cap.read()
            
            # Detect Faces
            face_locations, face_names = sfr.detect_known_faces(frame)
            for face_loc, name in zip(face_locations, face_names):
                y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

                cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
                
                if name not in [elem[0] for elem in all_name]:
                    all_name.append((name,time.time()))
                    
                for indx,name in enumerate(all_name):
                    time_diff = time.time() - name[1]
                    
                    if time_diff > 5:
                        all_name.remove(name)
                    else:
                        all_name[indx] = (name[0],time.time())
                
        #         print(all_names)
        #             engine.say(name + " is here")
        #             engine.runAndWait()



            #    cv2.imshow("Frame",frame)
            """
                key = cv2.waitKey(1)
                if key == 27:
                    engine.say("System Stopping")
                    engine.runAndWait()
                    break
            """
            
        cap.release()

        
    def stopRecognizing(self):
        self._isRecognizing = False
        #self._cap.release()
        #cv2.destroyAllWindows(0)
