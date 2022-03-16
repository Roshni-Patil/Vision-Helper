import time 
import pyttsx3 as py
import cv2
import os 



# Text reader module 



# function to ccapture image and calling text-reader module 
def generate_frames():
    # img_counter=0
    camera=cv2.VideoCapture(0)
    while True:
            
        ## read the camera frame
        time.sleep(3)
        py.speak("Put document in front of camera")
        time.sleep(0.2)
        py.speak("Image is going to captured")
        py.speak("3")
        py.speak("2")
        py.speak("1")
        success,frame=camera.read()
        
        if not success:
            print(success)
            break
        else:
            # time.sleep(3)
            # py.speak("3")
            # py.speak("2")
            # py.speak("1")
            ret,buffer=cv2.imencode('.jpg',frame)
            frame1=frame
            frame=buffer.tobytes()
            os.system("rm input.jpg")
            # os.system("mkdir text-reader-images ")
            # file_name_path = 'text-reader-images/input.jpg'
            cv2.imwrite("input.jpg", frame1)
            # break
            print(ret)
            py.speak("Image is captured")
            py.speak("Wait some moments to complete the process of recognizing text")
            os.system("python text-reader.py")
            break
            
        

        # yield(b'--frame\r\n'
        #            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
#         # time.sleep(3)
#         py.speak("3")
#         py.speak("2")
#         py.speak("1")
#         file_name_path = 'E:/final trial/templates/' +  '1.jpg'
#         cv2.imwrite(file_name_path, frame1)
#         break
# # def capture_frame():
        
        # k = cv2.waitKey(1)
        # if k%256 == 27:
        #     # ESC pressed
        #     print("Escape hit, closing...")
        #     break
        # elif k%256 == 32:
            # SPACE pressed
        # img_name = "opencv_frame_{}.png".format(img_counter)
        # cv2.imwrite(img_name, frame1)
        # print("{} written!".format(img_name))
        # img_counter += 1





# object detection module 
def object_detection_frames():
    # img_counter=0
    camera=cv2.VideoCapture(0)
    while True:
            
        ## read the camera frame
        # time.sleep(3)
        py.speak("hold your device stable to capture the image")
        time.sleep(0.4)
        py.speak("Image is going to captured")
        py.speak("3")
        py.speak("2")
        py.speak("1")
        success,frame=camera.read()
        
        if not success:
            print(success)
            break
        else:
            # time.sleep(3)
            # py.speak("3")
            # py.speak("2")
            # py.speak("1")
            ret,buffer=cv2.imencode('.jpg',frame)
            frame1=frame
            frame=buffer.tobytes()
            # file_name_path = 'E:/Final Year Project/text-reader-images/input.jpg'
            cv2.imwrite(f"input.jpg", frame1)
            # break
            print(ret)
            py.speak("Image is captured")
            py.speak("Wait some moments to complete the process of detecting objects")
            os.system("python object_detection.py")
            break
            

