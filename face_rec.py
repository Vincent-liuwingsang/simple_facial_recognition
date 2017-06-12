import os
import cv2
import face_recognition as fr
import numpy as np

data_dir= os.path.dirname(os.path.realpath(__file__))
file_name="/trained_data.txt"

# import trained data
images_name = []
images_encoding = []

f = open(data_dir+file_name,"r")
for line in f:
    temp = line.split(' ')
    images_name.append(temp[0])
    temp_encoding = np.array(temp[1:129])
    images_encoding.append(temp_encoding.astype(np.float))


# 0 : default webcam (for laptop's camera or only one camera is connected)
# 1 : external webcam
cam = cv2.VideoCapture(0)


turn = True;

while cam.isOpened():
    ret, frame = cam.read()
    if turn:
	frame_small = cv2.resize(frame, (0,0), fx = 0.25, fy = 0.25)
	face_locations = fr.face_locations(frame_small)
	face_encodings = fr.face_encodings(frame_small,face_locations)

	suspect = []
	for face_encoding in face_encodings:
	    match = fr.compare_faces(images_encoding, face_encoding,0.5)
	    name = "Unknown"
	    true_matches = [i for i,x in enumerate(np.asarray(match)) if x]
	    if len(true_matches) > 1:
		print "Warning: More than 1 person are being matched to suspect(s)"
	    
	    # By default, we extract the first match
	    if len(true_matches)>0:
	        name = images_name[true_matches[0]]
            suspect.append(name)

    # uncomment turn for a smoother runtime
    #turn = not turn

    for (t,r,b,l), name in zip(face_locations,suspect):
	t*=4
	r*=4
	b*=4
	l*=4
	cv2.rectangle(frame, (l,t), (r,b), (0,0,255), 2)
	cv2.rectangle(frame, (l, b - 35), (r, b), (0, 0, 255), cv2.FILLED)
	cv2.putText(frame, name, (l+6,b-6), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255,255,255), 1)

    cv2.imshow('Recording', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
	break
	
cam.release()
cv2.destroyAllWindows

