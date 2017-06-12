#!/bin/bash

if [ $# -eq 1 ]
then
	if [ $1 == "train" ] || [ $1 == "webcam" ] 
	then
		if [ $1 == "train" ]
		then
			echo "Training..."		
			python generate_training_data.py
		elif [ $1 == "webcam" ]
		then
			echo "Opening webcam for facial recognization..."		
			python face_rec.py
		else
			echo "Incorrect arguements or number of arguements"
		fi
	fi
elif [ $# -eq 2 ]
then
	if [ $1 == "train" ] && [ $2 == "webcam" ] 
	then
		echo "Training..."		
		python generate_training_data.py		
		echo "Opening webcam for facial recognization..."		
		python face_rec.py
	else
		echo "Incorrect arguements or number of arguements"
	fi
else
	echo "Incorrect arguements or number of arguements"
fi
