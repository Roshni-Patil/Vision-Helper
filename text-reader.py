# import cv2
import easyocr
import pyttsx3
# %matplotlib inline
im_5_path = 'input.jpg'
# text detected 
def recognize_text(img_path):
    '''loads an image and recognizes text.'''
    
    reader = easyocr.Reader(['en'])
    return reader.readtext(img_path)
result = recognize_text(im_5_path)

sentence = ''
for (bbox, text, prob) in result:
    sentence += f'{text} '


print(sentence)
# it will read the text 

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.say(sentence)
engine.say("Click on the screen to go to Home page")
engine.runAndWait()
