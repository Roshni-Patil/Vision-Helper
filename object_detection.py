import boto3
import csv
import pyttsx3 as py 
def speak(X):
    output= list(dict.fromkeys(X))  
    x = str(output)
    print(type(x))
    py.speak("Your nearby  objects are " + x)
with open('new_user_credentials.csv' , 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

photo = "input.jpg"
client  = boto3.client('rekognition' , aws_access_key_id = access_key_id,aws_secret_access_key  =secret_access_key,region_name='us-east-1')


with open (photo , 'rb') as input_image:
    input_bytes = input_image.read()


response = client.detect_labels(Image = {'Bytes' : input_bytes} , 
MaxLabels = 7 , MinConfidence = 90)
X = []
print(response)
print(len(response))
objects=len(response)
# while(next(iter(response))):
#     X.append(response['Labels'][i]['Name'])
#     i+=1
try:

    if objects==0:
        py.speak("Image not clear")
    else:
        
        for i in range(objects):
            X.append(response['Labels'][i]['Name'])
        output= list(dict.fromkeys(X))  
        x = str(output)
        print(type(x))
        print(x)
        py.speak("Your nearby  objects are " + x)
except IndexError:
        py.speak("Image is not cleared")
        py.speak( "Please again capture the image")
py.speak("Click on the screen to go to Home page")

# try:
    
#     for i in range(objects):
#         X.append(response['Labels'][i]['Name'])

    # speak(X)

# except IndexError:
    
#     # speak(response['Labels'][0]['Name'])
#     print("error found")


# finally:
#     py.speak("Image is not cleared")
#     py.speak( "Please again capture the image")
# removing duplicates 
# output= list(dict.fromkeys(X))
# print(output)


# print(response)   
# print(output) 
# def speak(X):
