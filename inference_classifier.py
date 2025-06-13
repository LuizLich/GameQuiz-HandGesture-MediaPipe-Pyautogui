import pickle
import cv2
import mediapipe as mp
import numpy as np
import pyautogui
import time
from quiz_profiles import profiles

# ---------------------
# Quiz Profile Selection
# ---------------------
print("Selecione o site/quiz:")
profile_names = list(profiles.keys())
for idx, name in enumerate(profile_names):
    print(f"{idx + 1}. {name}")

choice = int(input("Digite o número correspondente ao site: ")) - 1
selected_profile = profile_names[choice]
config = profiles[selected_profile]

alternatives = config["alternatives"]
cooldown_seconds = config["cooldown"]
gesture_map = config["gesture_map"]

# ---------------------
# Starting the model and MediaPipe
# ---------------------
model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

last_press_time = 0

labels_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}  # It depends on your trained model

while True:
    data_aux = []
    x_ = []
    y_ = []

    ret, frame = cap.read()
    if not ret:
        break

    H, W, _ = frame.shape
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )

            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                x_.append(x)
                y_.append(y)

            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x - min(x_))
                data_aux.append(y - min(y_))

        if len(data_aux) == 42:
            prediction = model.predict([np.asarray(data_aux)])
            gesture_index = int(prediction[0])
            predicted_character = labels_dict[gesture_index].lower()
            mapped_key = gesture_map.get(str(gesture_index))  # Uses the numeric key as string
            
            print(f"[DEBUG] Previsão: {predicted_character}, Mapeado para: {mapped_key}, Coordenadas: {alternatives.get(mapped_key)}")

            if mapped_key in alternatives:
                current_time = time.time()
                if (current_time - last_press_time) > cooldown_seconds:
                    x, y = alternatives[mapped_key]
                    pyautogui.click(x=x, y=y)
                    print(f"Clique enviado: '{mapped_key.upper()}' em ({x}, {y})")
                    last_press_time = current_time

            # Draw in the screen
            x1 = int(min(x_) * W) - 10
            y1 = int(min(y_) * H) - 10
            x2 = int(max(x_) * W) + 10
            y2 = int(max(y_) * H) + 10

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
            cv2.putText(frame, predicted_character.upper(), (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3, cv2.LINE_AA)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()