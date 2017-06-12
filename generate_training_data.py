import os
import glob
import face_recognition as fr


data_dir= os.path.dirname(os.path.realpath(__file__))
file_name="/trained_data.txt"



# Input data consists of individual photos of one person and the filename is formatted as firstName_lastName.jpg
f = open(data_dir+file_name,'r+')

for filename in glob.glob(data_dir+"/data/*.jpg"):  
    f.write((filename.split('/')[5]).split('_')[0])
    image = fr.load_image_file(filename)
    image_face = fr.face_locations(image)
    images_encoding = fr.face_encodings(image,image_face)[0]
    for each in images_encoding:
	f.write(' '+str(each))
    f.write('\n')


f.close()    
