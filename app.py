# import cv2
# import time
# import os 
# import json
# import re
import pyttsx3 as py
from flask import Flask , render_template , request , Response
import speech_recognition as sr
import modules
# camera=cv2.VideoCapture(0)
app = Flask("visionhelper")

@app.route("/")
def home():
        py.speak("Please Click on the Screen and tell me how may i help you ")
        return render_template( "input.html" )
        # return None
@app.route('/result', methods=['POST'])
def result():
        query=request.form["x"]
        query=query.lower()
        print(query)
        if 'road detection ' in query:
                py.speak("Ok Starting road detection")
                py.speak("road lane function is called")
                # os.system(python lane.py)

        elif "object detection " in query :
                py.speak("Ok Starting object detection")
                py.speak("object detection function is called")
                # os.system(python object.py)
                

        elif "text reader" in query:
                py.speak("Ok Starting text reader ")
                return render_template('text-reader.html')
   
        else:
                py.speak("We are not able to recognize the command")
                py.speak("Please try something else ")
        
        
        return render_template('output.html' , query=query)
        return None

@app.route('/video')
def video():
    return Response(modules.generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')







app.run(host="localhost" , port=8080, debug=True)

