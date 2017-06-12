# simple_facial_recognition

This is a programme that recognizes faces through your webcam based on the input photos you put in in the data/ folder.\

It utlizes face_recognition which is based on dlib library.

Pre-requisites:
webcam
Opencv
face_recognition
python 2.7
dlib

Instruction:
1) import photos that contain only 1 person per photo into the data folder. Naming etiquitte would be FirstName_LastName.jpg.
2) type bash ./faceRec.sh [train/webcam] or bash ./faceRec.sh [train/webcam] [webcam] in the terminal
        train: generate facial encodings based on the photos in data folder
        webcam: recognize know faces based of the generated facial encodings through webcam.
        
Tips:
1) You can switch to videos from webcam by switching to cv2.VideoCapture(video_name.format) instead of cv2.VideoCapture(0/1).
2) Change the float parameter in compare_faces to suit different environmental needs

