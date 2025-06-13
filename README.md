# sign-language-detector-python

# Steps:

python -m venv env 
.\env\Scripts\activate     
pip install -r requirements.txt

# Run 

"find_camera.py" to identify your camera by the index, then, change EVERY "cap = cv2.VideoCapture(number of you indice available)"
"collect_imgs.py" to start collecting the images of the gestures
"create_database.py" to create the folders with the images collected
"train_classifier.py" to train your classifier with the database, once you get the message "100.0% of samples were classified correctly !" you can start running "inference_classifier.py"

# Reference implementation:

[YouTube Video](https://www.youtube.com/watch?v=MJCSjXepaAM)
[Repository: sign-language-detector-python](https://github.com/computervisioneng/sign-language-detector-python)