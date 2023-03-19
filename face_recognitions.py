import face_recognition 
import cv2

import numpy as np

video_cap = cv2.VideoCapture(0)

barack_obama_img_dir = r"D:\MyPersonal\6.Personal_Jobs\Running_Projects\ThemisApp\ThemisAppAIPI\testing_code\fr\imge1.jpg"

obama_img = face_recognition.load_image_file(barack_obama_img_dir)
obama_img_encoding = face_recognition.face_encodings(obama_img)[0]



biden_img_dir = r"D:\MyPersonal\6.Personal_Jobs\Running_Projects\ThemisApp\ThemisAppAIPI\testing_code\fr\bb.jpg"

biden_img = face_recognition.load_image_file(biden_img_dir)
biden_img_encoding = face_recognition.face_encodings(biden_img)[0]


rana_img_dir = r"D:\MyPersonal\6.Personal_Jobs\Running_Projects\ThemisApp\ThemisAppAIPI\testing_code\fr\IMG20220106162306.jpg"

rana_img = face_recognition.load_image_file(rana_img_dir)
rana_img_encoding = face_recognition.face_encodings(rana_img)[0]

themis_img_dir = r"D:\MyPersonal\6.Personal_Jobs\Running_Projects\ThemisApp\ThemisAppAIPI\testing_code\fr\themisapp.jpg"

themis_img = face_recognition.load_image_file(themis_img_dir)
themis_img_encoding = face_recognition.face_encodings(themis_img)[0]

daren_img_dir = r"D:\MyPersonal\6.Personal_Jobs\Running_Projects\ThemisApp\ThemisAppAIPI\testing_code\fr\vp1.jpg"

daren_img = face_recognition.load_image_file(daren_img_dir)

daren_img_encoding = face_recognition.face_encodings(daren_img)[0]


known_face_encoding = [
    obama_img_encoding, 
    biden_img_encoding,
    rana_img_encoding,
    themis_img_encoding,
    daren_img_encoding
    ]


known_face_name = [
'Barack Obama',
'Joe Biden',
'Rana Sarkar',
'ThemisApp',
'Daren Scott'
    ]

face_location = []
process_this_frame = None
face_names = []
face_encoding = []

while True:

    ret, frame = video_cap.read()

    if process_this_frame:

        sm_frame = cv2.resize(frame, (0, 0), fx =.25, fy=.25)
        
        rgb_frame = sm_frame[:, :,  ::-1]


        face_location = face_recognition.face_locations(rgb_frame)
        face_encoding = face_recognition.face_encodings(rgb_frame, face_location)


        face_names = []


        for face_encod in face_encoding:
            matches = face_recognition.compare_faces(known_face_encoding, face_encod)

            name = 'Unknown'

            face_distance = face_recognition.face_distance(known_face_encoding, face_encod)

            best_match_index = np.argmin(face_distance)

            if matches[best_match_index]:
                name = known_face_name[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    for (top, right , bottom, left), name in zip(face_location, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0,0,255), 2)

        cv2.rectangle(frame, (left, bottom-35), (right, bottom), (0,0,255), cv2.FILLED)

        font = cv2.FONT_HERSHEY_DUPLEX

        cv2.putText(frame, name , (left+ 6, bottom-6), font, 1.0, (255,255,255), 1)



    cv2.imshow("Face Recognition Video", frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



video_cap.release()

cv2.destroyWindow()
        
        