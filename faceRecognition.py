import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

devangi_img = face_recognition.load_image_file("faces/devangi.jpeg")

# Encoding-> convert image into numbers
devangi_encoding = face_recognition.face_encodings(devangi_img)[0]

devid_img = face_recognition.load_image_file("faces/devid.jpg")
devid_encoding = face_recognition.face_encodings(devid_img)[0]

Shivi_img = face_recognition.load_image_file("faces/Shivi.jpg")
Shivi_encoding = face_recognition.face_encodings(Shivi_img)[0]

known_face_encodings = [devangi_encoding , devid_encoding , Shivi_encoding]
known_face_names = ["Devangi" , "Devid" , "Shivi"]

#list of known students
students = known_face_names.copy()

face_locations = []
face_encodings = []

# get the current date and time

present_time = datetime.now()
current_date = present_time.strftime("%Y-%m-%d")

f = open(f"{current_date}.csv" , "w+" , newline="")
lnwriter = csv.writer(f)

while True:
    _, frame = video_capture.read()
    
    if not _:
        print("Failed to grab frame")
        break
    
    small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    name = "Unknown"
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)
        
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            
    # Add the text if the Student is present
    if name in known_face_names:
        font=cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (10,100)
        fontScale = 1.5
        fontColor = (255,0,0)
        thickness = 2
        lineType = 2
        cv2.putText(frame, name +" Present ",bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)

        if name in students:
            students.remove(name)
            current_time = present_time.strftime("%H-%M-%S")
            lnwriter.writerow([name, current_time])
            
    cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()


























