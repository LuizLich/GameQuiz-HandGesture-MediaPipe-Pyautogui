# GameQuiz-HandGesture-MediaPipe-Pyautogui

## Project Overview

This project is an interactive game quiz system that allows users to answer questions using hand gestures, detected via the MediaPipe library. Quiz interactions are automated with PyAutoGUI, providing a unique and accessible gaming experience. The system includes functionalities to collect gesture data, train a custom classifier, and configure quiz profiles for different games across the internet. A usage demonstration is provided below. <br>
The base of this project has as reference implementation the repository of [computervisioneng](https://github.com/computervisioneng) which can be accessed via this [link](https://github.com/computervisioneng/sign-language-detector-python).

## 🕹️Features

*   **Hand Gesture Control:** Interact with the quiz using intuitive hand gestures.
*   **Data Collection and Training:** Tools to collect gesture images and train a custom gesture classifier.
*   **Quiz Profile Creation:** Easily configure new quiz profiles for your favorite websites and quiz games, adapting the system to your needs.
*   **PyAutoGUI Integration:** Automation of graphical interface interactions for a fluid experience.
*   **Image Preprocessing:** Techniques such as grayscale conversion, histogram equalization and contrast enhancement are applied to improve detection accuracy, especially in low-light environments.

## ⚙️Technologies Used

*   **Python:** Main programming language.
*   **MediaPipe:** For hand gesture detection and tracking.
*   **OpenCV (cv2):** For image manipulation, video capture, and preprocessing.
*   **PyAutoGUI:** For graphical interface automation.
*   **Scikit-learn:** For gesture classifier training.

## 📦Installation

Follow the steps below to set up the environment and install the necessary dependencies:

1.  **Create and Activate a Virtual Environment:**
    ```bash
    python -m venv env
    .\env\Scripts\activate
    ```
    You can confirm if the virtual environment is active in the prompt if (venv) appears:
    ![image](https://github.com/user-attachments/assets/2037d78e-2fc8-4160-89f7-fcc52040a08b)


3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 🔍Usage

To use the quiz system, you will need to follow a sequence of steps to configure gesture recognition and quiz profiles.

### 1. Initial Setup and Classifier Training

1.  **Identify Your Camera:**
    Run `find_camera.py` to identify your camera's index. Note down the available index number.
    ```bash
    python find_camera.py
    ```
    **Important:** After identifying the index, you need to change **ALL** occurrences of `cap = cv2.VideoCapture(your_available_index_number)` in the relevant Python files (`collect_imgs.py`, `inference_classifier.py`, etc.).

2.  **Collect Gesture Images:**
    Run `collect_imgs.py` to start collecting images of the gestures you want to use. Follow the on-screen instructions.
    ```bash
    python collect_imgs.py
    ```
    ![image](https://github.com/user-attachments/assets/6216fc52-caae-4455-8c83-d2d66221ff5a) <br>
    Press "Q" to start capturing the first gesture, try different angles for better results.
    For each saved class, change the gesture and press "Q" to capture the new one. <br>
    ![image](https://github.com/user-attachments/assets/fe7d787d-a732-48d6-9475-288e904c91eb)


4.  **Create the Image Database:**
    Run `create_database.py` to organize the collected images into folders, forming the database for training.
    ```bash
    python create_database.py
    ```

5.  **Train the Classifier:**
    Run `train_classifier.py` to train your classifier with the image database.
    ```bash
    python train_classifier.py
    ```
    Wait for the message "100.0% of samples were classified correctly!" to confirm that the training was successful. After that, you will be ready to use `inference_classifier.py`.

### 2. Configuring New Quiz Profiles

After configuring the classifier, you can create profiles for your specific quizzes:

1.  **Register New Quiz Profiles:**
    Run `register_quiz_profiles.py` and follow the prompts, answering according to the quiz you want to set up.
    ```bash
    python register_quiz_profiles.py
    ```

2.  **Verify Profile Creation:**
    After registration, check the `quiz_profiles.py` file to confirm that the new profile has been created correctly.

### 3. Running the Application

With the above steps successfully completed, you will be ready to use the application with the desired quiz profile. Instructions for starting the main quiz and selecting the profile are provided in the project's main code (`inference_classifier.py`).

## 🎮Usage Example
By default, this repository includes a profile for the quiz on the [Star Wars Quiz](https://www.starwars.com/news/category/quizzes-+-polls) website. <br>
If you want to test it, train the model to identify 5 gestures and map them.
After that, open the link above, choose a quiz, and leave it on the screen as shown below:
![image](https://github.com/user-attachments/assets/220fb1d9-3b90-4367-b678-6a69a109adf5)

Now, run `inference_classifier.py`, select the profile by typing its number and pressing "Enter": <br> <br>
![image](https://github.com/user-attachments/assets/bdf97c6c-a201-45fe-83a7-29e8b30de6db)

Wait for the camera to start and return to the quiz page (click somewhere on the page to make it the focused page) and start the gestures:
| Gestures | Automatic Responses |
| :---: | :---: |
| ![Untitled video - Made with Clipchamp](https://github.com/user-attachments/assets/7d624f3e-ee59-471c-8279-1bdffeb99669) | ![Untitled video - Made with Clipchamp (1)](https://github.com/user-attachments/assets/41259407-6705-40b3-bf33-c0bcf0d16406) |

 
## 👥Contribution

Reference implementation from [computervisioneng](https://github.com/computervisioneng) in the repository [sign-language-detector-python](https://github.com/computervisioneng/sign-language-detector-python) <br>
Video on Youtube by [computervisioneng](https://github.com/computervisioneng): [Sign language detection with Python and Scikit Learn | Landmark detection | Computer vision tutorial](https://www.youtube.com/watch?v=MJCSjXepaAM) <br>
Contributions are welcome! If you have suggestions for improvements, new features, or find any bugs, feel free to open an issue or submit a pull request.

## 📱Contact me
<a href="https://discord.com/channels/@LuizLich#5096"><img img width = '32px' align= 'center' src="https://logodownload.org/wp-content/uploads/2017/11/discord-logo-7-1.png"></a>
<a href = 'https://www.github.com/LuizLich'> <img width = '32px' align= 'center' src="https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"/></a>
<a href = 'https://www.instagram.com/luiz.lewiss/'> <img width = '32px' align= 'center' src="https://www.freepnglogos.com/uploads/instagram-icon-png/instagram-icon-suzem-limited-make-known-20.png"/></a>
<a href = 'https://www.linkedin.com/in/luiz-felipe-terra-da-silva/'> <img width = '32px' align= 'center' src="https://cdn-icons-png.flaticon.com/512/179/179330.png"/></a> 
<a href = 'https://br.pinterest.com/luizlewiss/_saved/'> <img width = '32px' align= 'center' src="https://cdn-icons-png.flaticon.com/512/145/145808.png"/></a>

<p>📫 Email: luiz.terrasilva27@gmail.com</p>

## 📄License

This project is licensed under the [MIT License](https://github.com/computervisioneng/sign-language-detector-python?tab=MIT-1-ov-file#). See the LICENSE file for more details.


